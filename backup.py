import tinys3
import sys
from environs import Env

env = Env()
env.read_env()

AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")


def executa_upload(file):
    try:
        conn = tinys3.Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
        f = open(file, 'rb')
        conn.upload(file, f, AWS_STORAGE_BUCKET_NAME)

    except Exception as ex:
        print("[BACKUP ERROR] " + file + "  -   " + str(ex))


if __name__ == "__main__":
    arquivo = str(sys.argv[1])
    print(" Arquivo recebido no Python: " + arquivo)
    executa_upload(arquivo)
