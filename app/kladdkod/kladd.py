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
riotAPIKey = "RGAPI-5f115e39-8307-4cd1-8dba-fcd92f1586de"
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


def generate_unit_info(unit, data):
    unit_name = unit
    unit_played = 0
    unit_playrate = ""
    unit_avg_placement = ""
    unit_image = ""
    unit_items = {}
    for element in data:
        if element == "unit_images":
            dictionary = data[element]
            for properties in dictionary:
                if properties == unit:
                    unit_image += dictionary[properties]
        if element == "item_images":
            dictionary = data[element]
            for properties in dictionary:
                if properties == unit:
                    for items in dictionary[properties]:
                        for item in items:
                            if item in unit_items:
                                value = list(unit_items[item].values())
                                unit_items[item] = {items[item]: value[0]}
        if element == "units_info_0":
            dictionary = data[element]
            for properties in dictionary:
                if properties == unit:
                    for value in dictionary[properties]:
                        if type(value) == int:
                            unit_played += value
                        else:
                            unit_playrate += value
        if element == "most_common_items":
            dictionary = data[element]
            for properties in dictionary:
                if properties == unit:
                    if bool(unit_items):
                        print("Bug at line 98")
                    else:
                        for items in dictionary[properties]:
                            dictionary2 = dictionary[properties]
                            value = dictionary2[items]
                            unit_items[items] = {"": value}
        if element == "units_info_1":
            dictionary = data[element]
            for properties in dictionary:
                if properties == unit:
                    unit_avg_placement += dictionary[properties]
    return unit_name, unit_played, unit_playrate, unit_avg_placement, unit_image, unit_items


@dataclass
class Unit:
    unit_name: str
    unit_played: int
    unit_playrate: str
    unit_avg_placement: str
    unit_image: str
    unit_items: dict[str:(dict[str:int])] = field(default_factory=dict)


def generate_unit(unit_name, unit_played, unit_playrate, unit_avg_placement, unit_image, unit_items):
    new_unit = Unit(unit_name, unit_played, unit_playrate, unit_avg_placement, unit_image, unit_items)
    return new_unit


dict1 = []
for unit in list_of_units:
    stored_unit = generate(unit, data)
    new_unit = generate_unit(stored_unit[0], stored_unit[1], stored_unit[2], stored_unit[3], stored_unit[4], stored_unit[5])
    dict1.append(new_unit)


print(*dict1, end='\n')
