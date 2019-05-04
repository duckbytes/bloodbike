from app import db
from datetime import datetime
from enum import IntEnum, auto
from sqlalchemy_utils import EmailType
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Objects(IntEnum):
    USER = auto()
    SESSION = auto()
    TASK = auto()
    VEHICLE = auto()

class Deliverable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    #notes = db.relationship('Note', backref='note', lazy='dynamic')
    task = db.Column(UUID(as_uuid=True), db.ForeignKey('task.uuid'))

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(10000))
    #task = db.Column(UUID(as_uuid=True), db.ForeignKey('task.uuid'))
    #user = db.Column(UUID(as_uuid=True), db.ForeignKey('user.uuid'))
    #session = db.Column(UUID(as_uuid=True), db.ForeignKey('session.uuid'))
    #vehicle = db.Column(UUID(as_uuid=True), db.ForeignKey('vehicle.uuid'))
    #deliverable = db.Column(db.Integer, db.ForeignKey('deliverable.id'))

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address1 = db.Column(db.String(64))
    address2 = db.Column(db.String(64))
    town = db.Column(db.String(64))
    county = db.Column(db.String(64))
    country = db.Column(db.String(64))
    postcode = db.Column(db.String(7))

    def updateFromDict(self, **entries):
        self.__dict__.update(entries)
        for entry in entries:
            flag_modified(self, entry)  # without this the database doesn't update


class Task(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    pickupAddress_id = db.Column(db.Integer, db.ForeignKey("address.id"))
    dropoffAddress_id = db.Column(db.Integer, db.ForeignKey("address.id"))

    pickupAddress = db.relationship("Address", foreign_keys=[pickupAddress_id])
    dropoffAddress = db.relationship("Address", foreign_keys=[dropoffAddress_id])


    pickupAddress1 = db.Column(db.String(64))
    pickupAddress2 = db.Column(db.String(64))
    pickupTown = db.Column(db.String(64))
    pickupPostcode = db.Column(db.String(7))
    destinationAddress1 = db.Column(db.String(64))
    destinationAddress2 = db.Column(db.String(64))
    destinationTown = db.Column(db.String(64))
    destinationPostcode = db.Column(db.String(7))
    patch = db.Column(db.String(64))
    contactName = db.Column(db.String(64))
    contactNumber = db.Column(db.Integer)
    priority = db.Column(db.Integer)
    finalDuration = db.Column(db.Time)
    miles = db.Column(db.Integer)
    flaggedForDeletion = db.Column(db.Boolean, default=False)
    session = db.Column(UUID(as_uuid=True), db.ForeignKey('session.uuid'))
    #notes = db.relationship('Note', backref='note', lazy='dynamic')


    def updateFromDict(self, **entries):
        self.__dict__.update(entries)
        for entry in entries:
            flag_modified(self, entry)  # without this the database doesn't update

    def __repr__(self):
        return '<Task ID {} taken at {} with priority {}>'.format(str(self.uuid), str(self.timestamp), str(self.priority))


class Vehicle(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    manufacturer = db.Column(db.String(64))
    model = db.Column(db.String(64))
    dateOfManufacture = db.Column(db.Date)
    dateOfRegistration = db.Column(db.Date)
    registrationNumber = db.Column(db.String(10))
    flaggedForDeletion = db.Column(db.Boolean, default=False)
    #notes = db.relationship('Note', backref='note', lazy='dynamic')

    def updateFromDict(self, **entries):
        self.__dict__.update(entries)
        for entry in entries:
            flag_modified(self, entry)  # without this the database doesn't update

    def __repr__(self):
        return '<Vehicle {} {} with registration {}>'.format(self.manufacturer, self.model, self.registrationNumber)


class User(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    address_id = db.Column(db.Integer, db.ForeignKey("address.id"))

    address = db.relationship("Address", foreign_keys=[address_id])
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(EmailType)
    password = db.Column(db.String(128))
    name = db.Column(db.String(64))
    dob = db.Column(db.Date)
    sessions = db.relationship('Session', backref='coordinator', lazy='dynamic')
    assignedVehicle = db.Column(UUID(as_uuid=True), db.ForeignKey('vehicle.uuid'))
    patch = db.Column(db.String(64))
    status = db.Column(db.String(64))
    flaggedForDeletion = db.Column(db.Boolean, default=False)
    roles = db.Column(db.String())
    is_active = db.Column(db.Boolean, default=True, server_default='true')
    #notes = db.relationship('Note', backref='note', lazy='dynamic')


    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()
    @classmethod
    def identify(cls, uuid):
        return cls.query.get(uuid)
    @property
    def identity(self):
        return self.uuid

    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    def updateFromDict(self, **entries):
        self.__dict__.update(entries)
        for entry in entries:
            flag_modified(self, entry)  # without this the database doesn't update

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Session(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.uuid'))
    tasks = db.relationship('Task', backref='sess', lazy='dynamic')
    flaggedForDeletion = db.Column(db.Boolean, default=False)
    #notes = db.relationship('Note', backref='note', lazy='dynamic')

    def __repr__(self):
        return '<Session {} {}>'.format(self.id, self.timestamp)
    

class DeleteFlags(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    objectId = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    timeToDelete = db.Column(db.Integer)
    objectType = db.Column(db.Integer)

class SavedLocations(Address, db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    name = db.Column(db.String(64))
    contact = db.Column(db.String(64))
    phoneNumber = db.Column(db.Integer())
    flaggedForDeletion = db.Column(db.Boolean, default=False)
    address_id = db.Column(db.Integer, db.ForeignKey("address.id"))

    address = db.relationship("Address", foreign_keys=[address_id])
    #notes = db.relationship('Note', backref='note', lazy='dynamic')

