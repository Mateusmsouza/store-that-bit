from pydantic import BaseSettings


class Settings(BaseSettings):

    oci_user_ocid: str
    oci_keyfile_path: str
    oci_fingerprint: str
    oci_region: str
    oci_tenancy: str

    oci_bucket_namespace: str
    oci_bucket_name: str

    app_is_debug: bool = True

    class Config:
        env_file = '.env'

app_settings = Settings()
