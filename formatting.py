from table2ascii import table2ascii
from yfpy import Team


def formatStandings(teams: list[Team]):
    header = ["Name", "Pts", "W", "L", "T"]
    body = []
    for team in teams:
        team_data = [team.name.decode(), team.points, team.wins, team.losses, team.ties]
        body.append(team_data)
    formated_str = table2ascii(header, body)
    return formated_str
