from mongoengine import StringField, DateTimeField, EmailField, Document

class User(Document):
    meta = {
        'collection': 'users',
        'allow_inheritance': False,
        'index_background': True,
        'indexes' : [
            {'fields': ['email'], 'unique': True}
        ]
    }
    createdAt = DateTimeField()
    email = EmailField()
    firstName = StringField()
    lastName = StringField()
    lastUpdated = DateTimeField()
