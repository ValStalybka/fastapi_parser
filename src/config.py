from pydantic_settings import BaseSettings


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


class LamodaUrls(BaseSettings):
    women_clothes: str = "https://www.lamoda.by/c/355/clothes-zhenskaya-odezhda/"
    women_accessories: str = "https://www.lamoda.by/c/557/accs-zhenskieaksessuary/"
    women_shoes: str = "https://www.lamoda.by/c/15/shoes-women/"

    men_clothes: str = "https://www.lamoda.by/c/477/clothes-muzhskaya-odezhda/"
    men_accessories: str = "https://www.lamoda.by/c/559/accs-muzhskieaksessuary/"
    men_shoes: str = "https://www.lamoda.by/c/17/shoes-men/"


class Twitch(BaseSettings):
    """credentials for connecting to TwitchAPI"""

    app_id: str
    app_secret: str

    class Config:
        env_prefix = "TWITCH_"
        env_file = ".env"


class Settings:
    fastapi: FastAPI = FastAPI()
    mongo: MongoDB = MongoDB()
    lamoda: LamodaUrls = LamodaUrls()
    twitch: Twitch = Twitch()
