from typing import Dict

import httpx

from src.config import Settings


class TwitchDAO:
    _settings = Settings()
    __app_id: str = Settings().twitch.app_id
    __app_secret: str = Settings().twitch.app_secret
    _access_token = None

    def _get_access_token(self) -> None:
        """fetches OAuth token for user"""
        url = self._settings.twitch.get_token_url.format(
            app_id=self.__app_id, app_secret=self.__app_secret
        )
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        access_token = httpx.post(url, headers=headers).json()["access_token"]
        self._access_token = access_token

    def _is_valid_token(self) -> bool:
        """checks if access token is valid"""
        if not self._access_token:
            self._get_access_token()

        headers = {"Authorization": f"OAuth {self._access_token}"}
        url = self._settings.twitch.validate_token_url

        validation_status_code = httpx.get(url, headers=headers).status_code
        if validation_status_code != 200:
            self._get_access_token()

        return True

    def _get_headers(self) -> Dict[str, str]:
        """compiles headers with credentials info"""
        if self._is_valid_token():
            headers = {
                "Authorization": f"Bearer {self._access_token}",
                "Client-Id": f"{self.__app_id}",
            }
            return headers

    def get_games(self, url: str) -> Dict:
        headers = self._get_headers()
        games = httpx.get(url, headers=headers).json()
        return games

    def get_streams(self, url: str) -> Dict:
        headers = self._get_headers()
        streams = httpx.get(url, headers=headers).json()
        return streams
