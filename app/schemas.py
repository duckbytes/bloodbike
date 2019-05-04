from app import ma
from flask_marshmallow import fields
from app import models

class AddressSchema(ma.Schema):
    class Meta:
        model = models.Address

        fields = ('address1', 'address2', 'town',
                  'county', 'country', 'postcode')

    #postcode = ma.Function(lambda obj: obj.postcode.upper())

class UserSchema(ma.Schema):
    class Meta:
        model = models.User
        fields = ('uuid', 'username', 'address', 'password', 'name', 'email',
                  'dob', 'patch', 'roles')

    username = ma.Str(required=True)
    email = ma.Email()
    dob = ma.DateTime(format='%d/%m/%Y')
    address = fields.fields.Nested(AddressSchema)


class UserUsernameSchema(ma.Schema):
    class Meta:
        model = models.User
        fields = ('uuid', 'username')

    username = ma.Str(required=True)


class UserAddressSchema(ma.Schema):
    class Meta:
        model = models.User
        fields = ('uuid', 'name', 'address1', 'address2', 'town',
                  'county', 'country', 'postcode')

    postcode = ma.Function(lambda obj: obj.postcode.upper())


class SessionSchema(ma.Schema):
    class Meta:
        model = models.Session
        fields = ('uuid', 'user_id', 'timestamp')


class TaskSchema(ma.Schema):
    class Meta:
        model = models.Task
        fields = ('pickupAddress1', 'pickupAddress2', 'pickupTown', 'pickupPostcode',
                  'destinationAddress1', 'destinationAddress2', 'destinationTown', 'destinationPostcode',
                  'patch', 'contactName', 'contactNumber', 'priority', 'session', 'timestamp')

    contactNumber = ma.Int()
    pickupPostcode = ma.Function(lambda obj: obj.postcode.upper())
    destinationPostcode = ma.Function(lambda obj: obj.postcode.upper())


class VehicleSchema(ma.Schema):
    class Meta:
        model = models.Task
        fields = ('manufacturer', 'model', 'dateOfManufacture', 'dateOfRegistration',
                  'registrationNumber')

    dateOfManufacture = ma.DateTime(format='%d/%m/%Y')
    dateOfRegistration = ma.DateTime(format='%d/%m/%Y')
    registrationNumber = ma.Function(lambda obj: obj.registrationNumber.upper())

