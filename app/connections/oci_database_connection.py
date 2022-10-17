import oracledb

from settings import app_settings


class Database:

    def __init__(self) -> None:
        self.connection = oracledb.connect(
            user=app_settings.oci_database_user,
            password=app_settings.oci_database_password,
            dsn=app_settings.oci_database_connection_string,
            encoding=app_settings.oci_encoding
        )
    
    def get(self):
        cursor =  self.connection.cursor()
        cursor.
        cur.execute("select sysdate from dual")
        res = cur.fetchall()
        for row in res:
            print(row)
        cur.close()