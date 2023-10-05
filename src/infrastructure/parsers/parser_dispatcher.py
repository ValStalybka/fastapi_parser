import logging.config
from typing import Callable

from src.infrastructure.parsers.lamoda import LamodaParser
from src.infrastructure.parsers.twitch import TwitchParser


logging.config.fileConfig("src/log.conf", disable_existing_loggers=False)


class ParserDispatcher:
    _dispatcher = {
        "games": TwitchParser().parse_game_list,
        "streams": TwitchParser().parse_stream_list,
        "lamoda": LamodaParser().parse_product_list,
    }
    __logger = logging.getLogger("Parser")

    def get_parser(self, url: str) -> Callable:

        for keyword, parser in self._dispatcher.items():
            if keyword in url:
                return parser
        self.__logger.warning("Unable to find parser for a given url")
