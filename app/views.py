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
from funcs.getUnitNamesAndItems import get_unit_names_and_items
from funcs.getItemNames import get_item_names
from funcs.fetchUnitImages import fetch_unit_images
from funcs.fetchTraitImages import fetch_trait_images
from funcs.fetchItemImages import fetch_item_images
from funcs.fetchAugmentImages import fetch_augment_images
from funcs.generateUnitList import generate_unit_list
from funcs.generateUnitDataList import generate_unit_data_list
from funcs.generateAugmentList import generate_augment_list
from funcs.generateAugmentListData import generate_augment_list_data
from funcs.generateTraitList import generate_trait_list
from funcs.generateTraitListData import generate_trait_list_data

# Initialize
riotAPIKey = ""
watcher = TftWatcher(riotAPIKey)
views = Blueprint('views', __name__)

# Paths
json_url = "https://raw.communitydragon.org/latest/cdragon/tft/en_gb.json"
path_url = "https://raw.communitydragon.org/latest/game/"


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
            unit_list = generate_unit_list(units_info[2])
            most_common_items = fetch_most_common_items(units_info[1])
            unit_names_and_items = get_unit_names_and_items(most_common_items)
            item_names = get_item_names(unit_names_and_items)
            unit_images = fetch_unit_images(unit_names_and_items, json_url, path_url)
            item_images = fetch_item_images(item_names, json_url, path_url)
            trait_images = fetch_trait_images(most_common_trait_info[0], json_url, path_url)
            augment_images = fetch_augment_images(augment_info[1], json_url, path_url)
            augment_list = generate_augment_list(augment_info[1])
            trait_list = generate_trait_list(most_common_trait_info[0])
            data = {"augment_info_0": augment_info[0],
                    "augment_info_1": augment_info[1],
                    "units_info_0": units_info[0],
                    "units_info_1": units_info[2],
                    "most_common_trait_info_0": most_common_trait_info[0],
                    "most_common_trait_info_1": most_common_trait_info[1],
                    "most_common_items": most_common_items,
                    "unit_images": unit_images,
                    "item_images": item_images,
                    "trait_images": trait_images,
                    "augment_images": augment_images}
            units_data_list = generate_unit_data_list(unit_list, data)
            augment_data_list = generate_augment_list_data(augment_list, data)
            trait_list_data = generate_trait_list_data(trait_list, data)
            data3 = {"units_data_list": units_data_list,
                     "augment_data_list": augment_data_list,
                     "trait_list_data": trait_list_data}
            return jsonify(data3)
        except Exception as error:
            status = "error"
            print(error)
            return render_template("index.html", status=status)
