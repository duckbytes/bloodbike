from app import db
from datetime import datetime
from enum import IntEnum, auto
from sqlalchemy_utils import EmailType
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Objects(IntEnum):
    USER = auto()
    SESSION = auto()
    TASK = auto()
    VEHICLE = auto()
    NOTE = auto()
    DELIVERABLE = auto()


class Note(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    body = db.Column(db.String(10000))
    subject = db.Column(db.String(200))
    task = db.Column(UUID(as_uuid=True), db.ForeignKey('task.uuid'))
    user = db.Column(UUID(as_uuid=True), db.ForeignKey('user.uuid'))
    session = db.Column(UUID(as_uuid=True), db.ForeignKey('session.uuid'))
    vehicle = db.Column(UUID(as_uuid=True), db.ForeignKey('vehicle.uuid'))
    deliverable = db.Column(UUID(as_uuid=True), db.ForeignKey('deliverable.uuid'))

class Deliverable(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    name = db.Column(db.String(64))
    task = db.Column(UUID(as_uuid=True), db.ForeignKey('task.uuid'))
    notes = db.relationship('Note', backref='deliverable_parent', lazy='dynamic')

class Address(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    line1 = db.Column(db.String(64))
    line2 = db.Column(db.String(64))
    town = db.Column(db.String(64))
    county = db.Column(db.String(64))
    country = db.Column(db.String(64))
    postcode = db.Column(db.String(64))


class Task(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    pickup_address_id = db.Column(UUID(as_uuid=True), db.ForeignKey('address.uuid'))
    dropoff_address_id = db.Column(UUID(as_uuid=True), db.ForeignKey('address.uuid'))

    pickup_address = db.relationship("Address", foreign_keys=[pickup_address_id])
    dropoff_address = db.relationship("Address", foreign_keys=[dropoff_address_id])

    patch = db.Column(db.String(64))
    contact_name = db.Column(db.String(64))
    contact_number = db.Column(db.Integer)
    priority = db.Column(db.Integer)
    final_duration = db.Column(db.Time)
    miles = db.Column(db.Integer)
    flagged_for_deletion = db.Column(db.Boolean, default=False)
    session = db.Column(UUID(as_uuid=True), db.ForeignKey('session.uuid'))
    deliverables = db.relationship('Deliverable', backref='deliverable_task', lazy='dynamic')
    notes = db.relationship('Note', backref='task_parent', lazy='dynamic')

    def __repr__(self):
        return '<Task ID {} taken at {} with priority {}>'.format(str(self.uuid), str(self.timestamp), str(self.priority))


class Vehicle(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    manufacturer = db.Column(db.String(64))
    model = db.Column(db.String(64))
    date_of_manufacture = db.Column(db.Date)
    date_of_registration = db.Column(db.Date)
    registration_number = db.Column(db.String(10))
    flagged_for_deletion = db.Column(db.Boolean, default=False)
    notes = db.relationship('Note', backref='vehicle_parent', lazy='dynamic')

    def __repr__(self):
        return '<Vehicle {} {} with registration {}>'.format(self.manufacturer, self.model, self.registrationNumber)


class User(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    address_id = db.Column(UUID(as_uuid=True), db.ForeignKey('address.uuid'))

    address = db.relationship("Address", foreign_keys=[address_id])
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(EmailType)
    password = db.Column(db.String())
    name = db.Column(db.String(64))
    dob = db.Column(db.Date)
    sessions = db.relationship('Session', backref='coordinator', lazy='dynamic')
    assigned_vehicle = db.Column(UUID(as_uuid=True), db.ForeignKey('vehicle.uuid'))
    patch = db.Column(db.String(64))
    status = db.Column(db.String(64))
    flagged_for_deletion = db.Column(db.Boolean, default=False)
    roles = db.Column(db.String())
    is_active = db.Column(db.Boolean, default=True, server_default='true')
    notes = db.relationship('Note', backref='user_parent', lazy='dynamic')

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

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Session(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.uuid'))
    tasks = db.relationship('Task', backref='sess', lazy='dynamic')
    flagged_for_deletion = db.Column(db.Boolean, default=False)
    notes = db.relationship('Note', backref='session_parent', lazy='dynamic')

    def __repr__(self):
        return '<Session {} {}>'.format(self.uuid, self.timestamp)
    

class DeleteFlags(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    object_uuid = db.Column(UUID(as_uuid=True))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    time_to_delete = db.Column(db.Integer)
    time_deleted = db.Column(db.DateTime, index=True)
    object_type = db.Column(db.Integer)
    active = db.Column(db.Boolean, default=True)

class SavedLocations(Address, db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    name = db.Column(db.String(64))
    contact = db.Column(db.String(64))
    phoneNumber = db.Column(db.Integer())
    flagged_for_deletion = db.Column(db.Boolean, default=False)
    address_id = db.Column(UUID(as_uuid=True), db.ForeignKey('address.uuid'))
    address = db.relationship("Address", foreign_keys=[address_id])

