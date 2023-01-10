from mongoengine import Document, StringField, DateField

from settings import app_settings

AN_HOUR = 3600


class FileStored(Document):
    filename = StringField(required=True)
    file_url = StringField(required=True)
    created_at = DateField(required=True)
    meta = {
        'indexes': [
            {'fields': ['created_at'], 'expireAfterSeconds': app_settings.default_hours * AN_HOUR}
        ]
    }
