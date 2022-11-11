from flask import Blueprint, render_template, request, jsonify
from urllib.request import Request, urlopen
from riotwatcher import TftWatcher

# Import functions
from funcs.fetchPuuid import fetch_puuid
from funcs.fetchLast20Matches import fetch_last_20_matches
from funcs.fetchMatchInfo import fetch_match_info
from funcs.fetchAugmentInfo import fetch_augment_info
from funcs.fetchUnitsInfo import fetch_units_info
from funcs.fetchMostCommonItems import fetch_most_common_items
from funcs.fetchMostCommonTrait import fetch_most_common_trait
from funcs.fetchUnitImages import fetch_unit_images
from funcs.getUnitNamesAndItems import get_unit_names_and_items

# Initialize
riotAPIKey = ""
watcher = TftWatcher(riotAPIKey)
views = Blueprint('views', __name__)


@views.route('', methods=["GET", "POST"])
def load_page():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
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
            unit_names_and_items = get_unit_names_and_items(most_common_items)
            unit_images = fetch_unit_images(unit_names_and_items)
            data = {"augment_info_0": augment_info[0],
                    "augment_info_1": augment_info[1],
                    "units_info_0": units_info[0],
                    "units_info_1": units_info[2],
                    "most_common_trait_info_0": most_common_trait_info[0],
                    "most_common_trait_info_1": most_common_trait_info[1],
                    "most_common_items": most_common_items,
                    "unit_images": unit_images}
            data = jsonify(data)
            return data
        except Exception as error:
            status = "error"
            print(error)
            return render_template("index.html", status=status)
