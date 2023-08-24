import uvicorn
from fastapi import FastAPI

from src.config import Settings
from src.routers import lamoda

app = FastAPI()
settings = Settings()

app.include_router(lamoda.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.fastapi.host,
        port=settings.fastapi.port,
        reload=settings.fastapi.reload,
    )
