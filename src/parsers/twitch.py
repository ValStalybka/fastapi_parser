from typing import Callable
from typing import Dict

from src.config import Settings
from src.services import controller
from src.services.twitch import TwitchService


class TwitchParser:
    _settings = Settings()
    """class for parsing Twitch data using httpx"""

    def _parse_object_list(
        self,
        base_url: str,
        access_object: Callable[[str], Dict],
        service: TwitchService,
        cursor: str = "",
    ) -> None:
        """abstract method for parsing objects list"""

        url = base_url + cursor
        object_list = access_object(url)
        data, pagination = object_list["data"], object_list["pagination"]
        service.create_many_objects(data)
        if pagination:
            cursor = f"?after={pagination['cursor']}"
            self._parse_object_list(base_url, access_object, service, cursor)
        else:
            return

    def parse_game_list(self) -> None:
        self._parse_object_list(
            base_url=self._settings.twitch.get_games_url,
            access_object=controller.twitch_dao.get_games,
            service=controller.games,
        )

    def parse_stream_list(self) -> None:
        self._parse_object_list(
            base_url=self._settings.twitch.get_streams_url,
            access_object=controller.twitch_dao.get_streams,
            service=controller.streams,
        )
