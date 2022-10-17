from pydantic import BaseSettings


class Settings(BaseSettings):

    oci_user_ocid: str
    oci_keyfile_path: str
    oci_fingerprint: str
    oci_region: str
    oci_tenancy: str

    oci_bucket_namespace: str
    oci_bucket_name: str

    #oci_database_user: str
    #oci_database_password: str
    #oci_encoding: str
    oci_database_connection_string: str


    app_is_debug: bool = True
    app_logger_name: str = 'sLogger'
    server_host: str = '0.0.0.0'
    server_port: int = 8000

    class Config:
        env_file = '.env'

app_settings = Settings()
