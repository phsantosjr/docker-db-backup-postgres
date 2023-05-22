from dataclasses import dataclass
import tinys3
import sys

from interfaces.provider import ProviderInterface


@dataclass(slots=True)
class Aws(ProviderInterface):
    secret_access_key: str = ""
    access_key_id: str = ""
    bucket_name: str = ""
    region: str = ""
    endpoint_url: str = ""

    def upload(self, file):
        try:
            conn = tinys3.Connection(self.access_key_id, self.secret_access_key)
            f = open(file, 'rb')
            conn.upload(file, f, self.bucket_name)

        except Exception as ex:
            print("[BACKUP ERROR] " + file + "  -   " + str(ex))