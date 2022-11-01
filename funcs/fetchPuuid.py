# Imports
from riotwatcher import TftWatcher

# Initialize
riotAPIKey = "RGAPI-b4615421-ab0c-4f1e-9dd3-a506453eb8c1"
watcher = TftWatcher(riotAPIKey)
region = str(input())
summoner_name = str(input())


def fetch_puuid(region, summoner_name):
    summoner = watcher.summoner.by_name(region, summoner_name)
    summoner_puuid = summoner['puuid']
    return summoner_puuid
