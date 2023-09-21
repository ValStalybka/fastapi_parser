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

    get_token_url: str = (
        "https://id.twitch.tv/oauth2/token?client_id={app_id}&"
        "client_secret={app_secret}&grant_type=client_credentials"
    )
    validate_token_url: str = "https://id.twitch.tv/oauth2/validate"
    get_games_url: str = "https://api.twitch.tv/helix/games/top"
    get_streams_url: str = "https://api.twitch.tv/helix/streams"

    class Config:
        env_prefix = "TWITCH_"
        env_file = ".env"


class Redis(BaseSettings):
    host: str
    port: int
    db: int

    class Config:
        env_prefix = "REDIS_"
        env_file = ".env"


class Settings:
    fastapi: FastAPI = FastAPI()
    mongo: MongoDB = MongoDB()
    lamoda: LamodaUrls = LamodaUrls()
    twitch: Twitch = Twitch()
    redis: Redis = Redis()
