from flask import Blueprint, render_template, request
from riotwatcher import TftWatcher

# Import functions
from funcs.fetchPuuid import fetch_puuid
from funcs.fetchLast20Matches import fetch_last_20_matches
from funcs.fetchMatchInfo import fetch_match_info
from funcs.fetchAugmentInfo import fetch_augment_info
from funcs.fetchUnitsInfo import fetch_units_info
from funcs.fetchMostCommonItems import fetch_most_common_items
from funcs.fetchMostCommonTrait import fetch_most_common_trait

# Initialize
riotAPIKey = "RGAPI-3f3873df-8fe2-4354-8f7f-29e70e9d0249"
watcher = TftWatcher(riotAPIKey)
views = Blueprint('views', __name__)


@views.route('', methods=["GET"])
def load_page():
    return render_template("index.html")


@views.route('', methods=["POST"])
def search():
    if request.method == 'POST':
        try:
            summoner_name = request.form.get("summonerName")
            region = request.form.get("region")
            puuid = fetch_puuid(region, summoner_name, riotAPIKey)
            last_20_matches = fetch_last_20_matches(region, puuid, riotAPIKey)
            matches_info = fetch_match_info(last_20_matches, region, puuid, riotAPIKey)
            augment_info = fetch_augment_info(matches_info)
            most_common_trait_info = fetch_most_common_trait(matches_info)
            units_info = fetch_units_info(matches_info)
            most_common_items = fetch_most_common_items(units_info[1])
            return render_template("index.html")
        except:
            print("error")
    return render_template("index.html")
