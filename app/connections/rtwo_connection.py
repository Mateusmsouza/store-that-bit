import boto3


class R2Connection():

    def __init__(self,
        endpoint: str,
        key_id: str,
        access_key: str,
        bucket_name: str):

        r2 = boto3.resource('s3',
        endpoint_url=endpoint,
        aws_access_key_id=key_id,
        aws_secret_access_key=access_key)

        self.__bucket_name = bucket_name
        self.__bucket = r2.Bucket(bucket_name)

    def get_pre_authorized_upload(self, filename):
        response = self.__bucket.generate_presigned_post(
            self.__bucket_name,
            object_name=filename,
            ExpiresIn=30)

        return response["url"], response["fields"]