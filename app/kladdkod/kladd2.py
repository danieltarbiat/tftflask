import json
from dataclasses import dataclass, field

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

# Initialize
riotAPIKey = "RGAPI-1ebf407e-f797-46ff-9289-6fe3da6fc5d5"
watcher = TftWatcher(riotAPIKey)
platformRoutingValue = "EUW1"
summonerName = "sorry im l8"
# Paths
json_url = "https://raw.communitydragon.org/latest/cdragon/tft/en_gb.json"
path_url = "https://raw.communitydragon.org/latest/game/"


def generate_unit_list(dictionary):
    list_of_units = {}
    for unit in dictionary:
        list_of_units[unit] = None
    return list_of_units


puuid = fetch_puuid(platformRoutingValue, summonerName, riotAPIKey)
last_20_matches = fetch_last_20_matches(platformRoutingValue, puuid, riotAPIKey)
matches_info = fetch_match_info(last_20_matches, platformRoutingValue, puuid, riotAPIKey)
augment_info = fetch_augment_info(matches_info)
most_common_trait_info = fetch_most_common_trait(matches_info)
units_info = fetch_units_info(matches_info)
list_of_units = generate_unit_list(units_info[2])
most_common_items = fetch_most_common_items(units_info[1])
unit_names_and_items = get_unit_names_and_items(most_common_items)
item_names = get_item_names(unit_names_and_items)
unit_images = fetch_unit_images(unit_names_and_items, json_url, path_url)
item_images = fetch_item_images(item_names, json_url, path_url)
trait_images = fetch_trait_images(most_common_trait_info[0], json_url, path_url)
augment_images = fetch_augment_images(augment_info[1], json_url, path_url)
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

test = most_common_trait_info[0]


def generate_trait_list(dictionary):
    augment_names = {}
    for augment in dictionary:
        augment_names[augment] = None
    return augment_names


lista = generate_trait_list(test)


def generate_trait_data(trait_name, data):
    trait_name = trait_name
    trait_played = 0
    trait_styles = {"Bronze":0,
                    "Silver":0,
                    "Gold":0,
                    "Platinum":0}
    trait_avg_place = ""
    trait_image = ""
    for element in data:
        if element == "most_common_trait_info_0":
            for properties in data[element]:
                if properties == trait_name:
                    dictionary = data[element]
                    for key in dictionary[properties]:
                        for style in key:
                            if style == 0:
                                trait_styles["Bronze"] = key[style]
                            elif style == 1:
                                trait_styles["Silver"] = key[style]
                            elif style == 2:
                                trait_styles["Gold"] = key[style]
                            elif style == 3:
                                trait_styles["Platinum"] = key[style]
        if element == "most_common_trait_info_1":
            for properties in data[element]:
                if properties == trait_name:
                    dictionary = data[element]
                    for item in dictionary[properties]:
                        trait_avg_place = item[0]
                        trait_played = item[1]
        if element == "trait_images":
            for properties in data[element]:
                if properties == trait_name:
                    dictionary = data[element]
                    for item in dictionary:
                        trait_image = dictionary[item]
    return trait_name, trait_played, trait_styles, trait_avg_place, trait_image


def generate_trait_list_data(augment_list, data):
    augment_list_info = {}
    for augment in augment_list:
        new_augment = generate_trait_data(augment, data)
        augment_list_info[augment] = {"Trait Name":new_augment[0],
                                      "Times Played":new_augment[1],
                                      "Trait Styles":new_augment[2],
                                      "Average Placement":new_augment[3],
                                      "Trait Image":new_augment[4]}
    return augment_list_info


jason = generate_trait_list_data(lista, data)
print(json.dumps(jason))