import sys
import asyncio
from fpl import FPL
import pandas as pd
import aiohttp

async def main():
    session = aiohttp.ClientSession()
    fpl = FPL(session)

    ## Get player
    player = await fpl.get_player(302)
    print(player)

    print(player.points_per_game)
    print(player.total_points)

    player = await fpl.get_player(302, return_json=True)
    player_available_info = player.keys()


    players = await fpl.get_players(return_json=True, include_summary=True)



    players_table = pd.DataFrame.from_dict(players)
    players_table_history = []
    for id, name, player in zip(players_table.id, players_table.first_name, players_table.history):
        print(len(player))
        for i in range(len(player)):
            player[i]['id'] = id
            player[i]['name'] = name
        players_table_history.extend(player)
   
    players_history_df = pd.DataFrame(players_table_history)
    print(players_history_df.head())
    players_table.sort_values(by='goals_scored', inplace=True)

    print(players_table.head())
    #print(players_table.columns)
    print(players_table.describe())

    



""" 
players info
['chance_of_playing_next_round', 'chance_of_playing_this_round', 'code', 'cost_change_event', 'cost_change_event_fall', 
'cost_change_start', 'cost_change_start_fall', 'dreamteam_count', 'element_type', 'ep_next', 'ep_this', 'event_points', 
'first_name', 'form', 'id', 'in_dreamteam', 'news', 'news_added', 'now_cost', 'photo', 'points_per_game', 'second_name', 
'selected_by_percent', 'special', 'squad_number', 'status', 'team', 'team_code', 'total_points', 'transfers_in', 
'transfers_in_event', 'transfers_out', 'transfers_out_event', 'value_form', 'value_season', 'web_name', 'minutes', 
'goals_scored', 'assists', 'clean_sheets', 'goals_conceded', 'own_goals', 'penalties_saved', 'penalties_missed', 
'yellow_cards', 'red_cards', 'saves', 'bonus', 'bps', 'influence', 'creativity', 'threat', 'ict_index', 'influence_rank', 
'influence_rank_type', 'creativity_rank', 'creativity_rank_type', 'threat_rank', 'threat_rank_type', 'ict_index_rank', 
'ict_index_rank_type', 'corners_and_indirect_freekicks_order', 'corners_and_indirect_freekicks_text', 'direct_freekicks_order', 
'direct_freekicks_text', 'penalties_order', 'penalties_text']

"""

## pip install asyncio

if __name__ == '__main__':
    asyncio.run(main())