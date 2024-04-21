from abc import abstractmethod


class BaseAPIClient:
    @abstractmethod
    def fetch_players(self, count) -> list[dict]:
        pass
