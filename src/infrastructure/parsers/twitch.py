import logging
from typing import Callable
from typing import Dict

from src.services import controller
from src.services.twitch import TwitchService


class TwitchParser:
    """class for parsing Twitch data using httpx"""

    __logger = logging.getLogger("Parser")

    async def _parse_object_list(
        self,
        base_url: str,
        access_object: Callable[[str], Dict],
        service: TwitchService,
        cursor: str = "",
    ) -> None:
        """abstract method for parsing objects list"""

        self.__logger.info("Starting parsing")
        url = base_url + cursor
        object_list = access_object(url)
        data, pagination = object_list["data"], object_list["pagination"]
        service.create_many_objects(data)
        if pagination:
            cursor = f"?after={pagination['cursor']}"
            await self._parse_object_list(base_url, access_object, service, cursor)
        else:
            return

    async def parse_game_list(self, url: str) -> None:
        await self._parse_object_list(
            base_url=url,
            access_object=controller.twitch_dao.get_games,
            service=controller.games,
        )

    async def parse_stream_list(self, url: str) -> None:
        await self._parse_object_list(
            base_url=url,
            access_object=controller.twitch_dao.get_streams,
            service=controller.streams,
        )
