from riotwatcher import TftWatcher


def fetch_match_info(matches, region, puuid, API):
    list_of_matches = matches
    i = 1
    match_info_dictionary = {}
    for match in list_of_matches:
        matchinfo = TftWatcher(API).match.by_id(region, match)
        for match_data in matchinfo['info']['participants']:
            if match_data['puuid'] == puuid:
                match_info_dictionary['match' + str(i)] = match_data
                i += 1
    return match_info_dictionary

