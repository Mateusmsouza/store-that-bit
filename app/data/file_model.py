from mongoengine import Document, StringField, DateField


class FileStored(Document):
    filename = StringField(required=True)
    file_url = StringField(required=True)
    live_until = DateField(required=True)
    created_at = DateField(required=True)
