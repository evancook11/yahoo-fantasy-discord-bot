from pathlib import Path
from yfpy import YahooFantasySportsQuery, Team


class YahooApi():
    __league_id: str
    __game_key: str
    __env_file_location: Path
    __query: YahooFantasySportsQuery

    def __init__(self, league_id: str, game_key: str, env_file_location: Path):
        self.__league_id = league_id
        self.__game_key = game_key
        self.__env_file_location = env_file_location
        self.__query = YahooFantasySportsQuery(
            self.__league_id,
            self.__game_key,
            env_file_location=self.__env_file_location,
            save_token_data_to_env_file=True
        )

    def getLeagueStandings(self) -> list[Team]:
        return self.__query.get_league_standings().teams
