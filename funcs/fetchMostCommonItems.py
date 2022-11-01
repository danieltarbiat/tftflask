from fetchUnitsInfo import *


def fetch_most_common_items(region, summoner_name):
    champion_data = fetch_units_info(region, summoner_name)[1]
    champion_items = {}
    for champion in champion_data:
        i = 0
        champion_name = champion[i]
        for elements in champion:
            if type(elements) is list:
                for dictionary in elements:
                    if type(dictionary) is dict:
                        item_list = dictionary['itemNames']
                        champion_items[champion_name] = [item for item in item_list]
        i += 1
    new_champion_items = {}
    for key in set(champion_items.keys()):
        new_champion_items[key] = {}
    for champion in new_champion_items:
        for champion_data in champion_items:
            if champion == champion_data:
                for element in champion_items[champion_data]:
                    if element not in new_champion_items[champion]:
                        new_champion_items[champion][element] = 1
                    else:
                        new_champion_items[champion][element] += 1
    for key in new_champion_items:
        new_champion_items[key] = dict(sorted(new_champion_items[key].items(), key=lambda x: x[1], reverse=True))
    return new_champion_items