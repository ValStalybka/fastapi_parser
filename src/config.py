from pydantic_settings import BaseSettings
from decouple import config


class FastAPI(BaseSettings):
    host: str
    port: int
    reload: bool

    class Config:
        env_prefix = "FASTAPI_"
        env_file = ".env"


class MongoDB(BaseSettings):
    host: str
    port: int
    db_name: str

    class Config:
        env_prefix = "MONGO_"
        env_file = ".env"


class Settings:
    fastapi: FastAPI = FastAPI()
    mongo: MongoDB = MongoDB()
