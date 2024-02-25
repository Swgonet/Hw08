from mongoengine import Document, StringField, ListField, ReferenceField

class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

    meta = {'collection': 'authors'}


class Quotes(Document):
    author = ReferenceField(Authors, required=True)
    tags = ListField(StringField())
    quote = StringField()
    
    meta = {'collection': 'quotes'}
