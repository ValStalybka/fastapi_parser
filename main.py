import uvicorn
from fastapi import FastAPI
from src.config import Settings

app = FastAPI()
settings = Settings()

# testing git config
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.fastapi.host,
        port=settings.fastapi.port,
        reload=settings.fastapi.reload,
    )
