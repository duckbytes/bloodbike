from app import db
from datetime import datetime

class Address(object):
    address1 = db.Column(db.String(64))
    address2 = db.Column(db.String(64))
    town = db.Column(db.String(64))
    county = db.Column(db.String(64))
    country = db.Column(db.String(64))
    postcode = db.Column(db.String(7))


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    pickupAddress1 = db.Column(db.String(64))
    pickupAddress2 = db.Column(db.String(64))
    pickupTown = db.Column(db.String(64))
    pickupPostcode = db.Column(db.String(7))
    destinationAddress1 = db.Column(db.String(64))
    destinationAddress2 = db.Column(db.String(64))
    destinationTown = db.Column(db.String(64))
    destinationPostcode = db.Column(db.String(7))
    patch = db.Column(db.String(64))
    priority = db.Column(db.Integer)
    finalDuration = db.Column(db.Time)
    miles = db.Column(db.Integer)
    session = db.Column(db.Integer, db.ForeignKey('session.id'))

    def __repr__(self):
        return '<Task ID {} taken at {} with priority {}>'.format(str(self.id), str(self.timestamp), str(self.priority))


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    manufacturer = db.Column(db.String(64))
    model = db.Column(db.String(64))
    dateOfManufacture = db.Column(db.Date)
    dateOfRegistration = db.Column(db.Date)
    registrationNumber = db.Column(db.String(10))

    def __repr__(self):
        return '<Vehicle {} {} with registration {}>'.format(self.manufacturer, self.model, self.registrationNumber)


class User(Address, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120))
    passwordHash = db.Column(db.String(128))
    name = db.Column(db.String(64))
    dob = db.Column(db.Date)
    status = db.Column(db.String(64))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Rider(User):
   # id = db.Column(db.Integer, primary_key=True)
   # timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    assignedVehicle = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    patch = db.Column(db.String(64))

    def __repr__(self):
        return '<Rider {} in patch {} with vehicle {}>'.format(self.name, self.patch, self.assignedVehicle)

class Coordinator(User):
    sessions = db.relationship('Session', backref='coordinator', lazy='dynamic')


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tasks = db.relationship('Task', backref='sess', lazy='dynamic')

    def __repr__(self):
        return '<Session {} {}>'.format(self.id, self.timestamp)
