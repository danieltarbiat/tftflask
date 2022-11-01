from fetchPuuid import *


def fetch_last_20_matches(region, summoner_name):
    puuid = fetch_puuid(region, summoner_name)
    matches = watcher.match.by_puuid(region, puuid)
    return matches
