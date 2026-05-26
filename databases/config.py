import os
from dotenv import load_dotenv


load_dotenv('../envs/.env') # подгружаем env

class Settings:
    def __init__(self):
        self.user = os.getenv('DB_USER')
        self.db_host = os.getenv('DB_HOST')
        self.db_password = os.getenv('DB_PASSWORD')
        self.db_name = os.getenv('db_name')
        self.db_port = os.getenv('db_port')

settings = Settings()
print(settings.__dict__)
