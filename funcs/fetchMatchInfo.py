from fetchLast20Matches import *


def fetch_match_info(region, summoner_name):
    list_of_matches = fetch_last_20_matches(region, summoner_name)
    puuid = fetch_puuid(region, summoner_name)
    i = 1
    match_info_dictionary = {}
    for match in list_of_matches:
        matchinfo = watcher.match.by_id(region, match)
        for match_data in matchinfo['info']['participants']:
            if match_data['puuid'] == puuid:
                match_info_dictionary['match' + str(i)] = match_data
                i += 1
    return match_info_dictionary

