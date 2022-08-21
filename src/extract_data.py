import asyncio
from fpl import FPL
import pandas as pd
import aiohttp



async def get_player_info():
    session = aiohttp.ClientSession()
    fpl = FPL(session)

    players = await fpl.get_players(return_json=True)

    players_table = pd.DataFrame.from_dict(players)
    players_table.sort_values(by='goals_scored', inplace=True)
    return players_table


def get_history(df:pd.DataFrame):
    """
    Need to understand what each level refers to e.g. Current game, all games?
    """
    players_table_history = []
    for id, name, player in zip(df.id, df.first_name, df.history):
        for i in range(len(player)):
            player[i]['id'] = id
            player[i]['name'] = name
        players_table_history.extend(player)
   
    history_df = pd.DataFrame(players_table_history)
    return history_df



"""
https://fantasy.premierleague.com/help/rules

Expected point per game:

Time on Pitch: +1 if <60mins else +2
Goal scored = +4 if forward else (+5 if midfielder else (+6 if goalkeeper or defender else 0)
Assists = +3
Clean sheet = +4 if goalkeep or defender else +1 if midfielder else 0 (Must be on field)
3 shot saves = +3 if goalkeeper else 0
Penalty save = +5
Penalty miss = -2
Best player = 1-3 (Need another function for this)
Goals conceded = -2 * conceded/2
Yellow card = -1
Red card = -3
Own goal = -2

"""

def calculate_player_score():

    return True
