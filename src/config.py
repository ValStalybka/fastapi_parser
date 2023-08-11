from pydantic_settings import BaseSettings
from decouple import config


class FastAPI(BaseSettings):
    host: str = config("FASTAPI_HOST")
    port: int = config("FASTAPI_PORT")
    reload: bool = True


class MongoDB(BaseSettings):
    host: str = config("MONGO_HOST")
    port: int = config("MONGO_PORT")
    db_name: str = config("MONGO_DB_NAME")


class Settings:
    fastapi: FastAPI = FastAPI()
    mongo: MongoDB = MongoDB()
