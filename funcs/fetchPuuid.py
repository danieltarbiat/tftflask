from riotwatcher import TftWatcher


def fetch_puuid(region, summoner_name,API):
    summoner = TftWatcher(API).summoner.by_name(region, summoner_name)
    summoner_puuid = summoner['puuid']
    return summoner_puuid
