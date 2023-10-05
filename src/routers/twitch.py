from typing import Dict
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from src.dependencies import set_pagination
from src.schemas.twitch import Game
from src.schemas.twitch import Stream
from src.services import controller

router = APIRouter(tags=["Twitch"], prefix="/twitch")


@router.post("/parse")
async def create_parsing_task(parsing_url: str):
    message = await controller.kafka.send_message(topic="parse", data=parsing_url)
    return message


@router.get("/games", response_model=List[Game])
async def get_games_list(pagination=Depends(set_pagination)):
    skip, limit = pagination
    game_list = controller.games.get_object_list()
    return game_list[skip : (skip + limit)]


@router.get("/games/{game_id}", response_model=Game)
async def get_game(game_id: str):
    game = controller.games.get_object(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Item not found")
    return game


@router.post("/games")
async def create_game(data: Game):
    return controller.games.create_object(data)


@router.patch("/games", response_model=Game)
async def update_game(game_id: str, data: Dict):
    return controller.games.update_object(game_id, data)


@router.delete("/games")
async def delete_game(game_id: str):
    return controller.games.delete_object(game_id)


@router.get("/streams", response_model=List[Stream])
async def get_streams_list(pagination=Depends(set_pagination)):
    skip, limit = pagination
    stream_list = controller.games.get_object_list()
    return stream_list[skip : (skip + limit)]


@router.get("/streams/{stream_id}", response_model=Stream)
async def get_stream(stream_id: str):
    stream = controller.streams.get_object(stream_id)
    if not stream:
        raise HTTPException(status_code=404, detail="Item not found")
    return stream


@router.post("/streams")
async def create_stream(data: Stream):
    return controller.streams.create_object(data)


@router.patch("/streams", response_model=Stream)
async def update_stream(stream_id: str, data: Dict):
    return controller.streams.update_object(stream_id, data)


@router.delete("/streams")
async def delete_stream(stream_id: str):
    return controller.streams.delete_object(stream_id)
