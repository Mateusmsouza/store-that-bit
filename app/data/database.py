from mongoengine import connect

from settings import app_settings


class Database:

    def __init__(self) -> None:
        self.connection = connect(
            app_settings.oci_database_connection_string
        )
