import sys
from environs import Env

from factories.provider import  ProviderFactory

env = Env()
env.read_env()

AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
PROVIDER = env("PROVIDER")
ENDPOINT_URL = env("ENDPOINT_URL")
REGION = env("REGION")


def execute_upload(file_to_upload):
    f = ProviderFactory()
    f = f.get_provider(PROVIDER)
    factory = f()

    factory.secret_access_key = AWS_SECRET_ACCESS_KEY
    factory.access_key_id = AWS_ACCESS_KEY_ID
    factory.bucket_name = AWS_STORAGE_BUCKET_NAME
    factory.region = REGION
    factory.endpoint_url = ENDPOINT_URL
    factory.upload(file_to_upload)


if __name__ == "__main__":
    file = str(sys.argv[1])
    print(f" Arquivo recebido no Python: {file}")
    execute_upload(file)
