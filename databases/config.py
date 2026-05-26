import os
from dotenv import load_dotenv


load_dotenv() # подгружаем env

class Settings:
    def __init__(self):
        self.user = os.getenv('DB_USER')
        self.db_host = os.getenv('DB_HOST')
        self.db_password = os.getenv('DB_PASSWORD')
        self.db_name = os.getenv('db_name')
        self.db_port = os.getenv('db_port', 5432)

    @property # используем property (позволяет вызывать settings.asyncpg_url как переменную, без скобочек, синтаксический сахар)
    def asyncpg_url(self):
        return f'postgresql+asyncpg://{self.user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}'

settings = Settings()
