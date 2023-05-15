import boto3
import mimetypes
from dataclasses import dataclass

from interfaces.provider import ProviderInterface


@dataclass(slots=True)
class DigitalOcean(ProviderInterface):
    secret_access_key: str = ""
    access_key_id: str = ""
    bucket_name: str = ""
    region: str = ""
    endpoint_url: str = ""

    def get_spaces_client(self):
        session = boto3.session.Session()

        return session.client(
            's3',
            region_name=self.region,
            endpoint_url=self.endpoint_url,
            aws_access_key_id=self.access_key_id,
            aws_secret_access_key=self.secret_access_key
        )


    def upload(self, file):
        client = self.get_spaces_client()

        is_public = False # = kwargs.get("is_public", False)
        # content_type = kwargs.get("content_type")
        # meta = kwargs.get("meta")

        content_type = ''
        if not content_type:
            file_type_guess = mimetypes.guess_type(file)

            if not file_type_guess[0]:
                raise Exception("We can't identify content type. Please specify directly via content_type arg.")

            content_type = file_type_guess[0]

        extra_args = {
            'ACL': "public-read" if is_public else "private",
            'ContentType': content_type
        }

        # if isinstance(meta, dict):
        #     extra_args["Metadata"] = meta

        save_as = file

        return client.upload_file(
            file,
            self.bucket_name,
            save_as,
            ExtraArgs=extra_args
        )