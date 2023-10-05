import logging.config

import uvicorn
from fastapi import FastAPI

from src.config import Settings
from src.routers import lamoda
from src.routers import twitch

app = FastAPI()
settings = Settings()

app.include_router(lamoda.router)
app.include_router(twitch.router)


if __name__ == "__main__":
    logging.config.fileConfig("src/log.conf", disable_existing_loggers=False)
    uvicorn.run(
        "main:app",
        host=settings.fastapi.host,
        port=settings.fastapi.port,
        reload=settings.fastapi.reload,
    )
