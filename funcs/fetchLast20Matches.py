from riotwatcher import TftWatcher


def fetch_last_20_matches(region,puuid,API):
    matches = TftWatcher(API).match.by_puuid(region, puuid)
    return matches
