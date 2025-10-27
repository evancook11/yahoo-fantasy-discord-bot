from table2ascii import table2ascii
from yfpy import Team
from models import Table


def formatStandings(standings_table: Table):
    formated_str = table2ascii(standings_table.header, standings_table.entries)
    return formated_str
