from fetchMatchInfo import *


def fetch_units_info(region, summoner_name):
    match_info_dictionary = fetch_match_info(region, summoner_name)
    a = 1
    average_unit_placement = {}
    for match in list(match_info_dictionary):
        if a == 21:
            break
        placement = match_info_dictionary['match' + str(a)]['placement']
        for unit in match_info_dictionary['match' + str(a)]['units']:
            for properties in unit:
                if properties == 'character_id':
                    char = unit[properties]
                    if char not in average_unit_placement:
                        average_unit_placement[char] = [placement]
                    else:
                        average_unit_placement[char] += [placement]
        a += 1
    average_unit_placement = dict(sorted(average_unit_placement.items(), key=lambda x: (len(x[1]), x[0]), reverse=True))
    for key in average_unit_placement:
        val = average_unit_placement[key]
        val = round(sum(val) / len(val), 1)
        average_unit_placement[key] = '#' + str(val)
    i = 1
    counter = 0
    units = {}
    for key in list(match_info_dictionary):
        if i == 21:
            break
        for unit in match_info_dictionary['match' + str(i)]['units']:
            for element in list(unit):
                if element == 'character_id':
                    if unit[element] in units:
                        counter += 1
                        char = unit[element]
                        units[char][0] += 1
                        match_items = unit['itemNames']
                        for properties in units[char]:
                            if type(properties) is dict:
                                for value in properties:
                                    if value == 'itemNames':
                                        for match_item in match_items:
                                            where_to_add_items = units[char][1]['itemNames']
                                            where_to_add_items.append(match_item)
                    else:
                        char = unit[element]
                        units[unit[element]] = [1]
                        unit.pop(element)
                        units[char].append(unit)
                        counter += 1
        i += 1
    sorted_units = [(k, units[k]) for k in sorted(units, key=lambda x: units[x][0], reverse=True)]
    used_units = {}
    for used in units:
        values = units[used]
        values = values[0]
        used_units[used] = [values, str(round(values / counter * 100, 1)) + '%']
    used_units = dict(sorted(used_units.items(), key=lambda item: item[1], reverse=True))
    return used_units, sorted_units, average_unit_placement