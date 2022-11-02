from riotwatcher import TftWatcher
riotAPIKey = "RGAPI-1d816f99-6417-44d8-a6ce-35d9d0b533a2"
watcher = TftWatcher(riotAPIKey)


def fetch_last_20_matches(region,puuid):
    matches = watcher.match.by_puuid(region, puuid)
    return matches
