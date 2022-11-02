# Imports
from riotwatcher import TftWatcher

# Initialize
riotAPIKey = "RGAPI-1d816f99-6417-44d8-a6ce-35d9d0b533a2"
watcher = TftWatcher(riotAPIKey)
region = ["BR1", "EUN1", "EUW1", "JP1", "KR", "LA1", "LA2", "NA1", "OC1", "TR1", "RU"]
summoner_name = "sorry im l8"


def fetch_puuid(region, summoner_name):
    summoner = watcher.summoner.by_name(region, summoner_name)
    summoner_puuid = summoner['puuid']
    return summoner_puuid
