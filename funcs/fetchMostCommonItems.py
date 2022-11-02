def fetch_most_common_items(units_data):
    unit_items = {}
    for unit in units_data:
        i = 0
        unit_name = unit[i]
        for elements in unit:
            if type(elements) is list:
                for dictionary in elements:
                    if type(dictionary) is dict:
                        item_list = dictionary['itemNames']
                        unit_items[unit_name] = [item for item in item_list]
        i += 1
    new_unit_items = {}
    for key in set(unit_items.keys()):
        new_unit_items[key] = {}
    for unit in new_unit_items:
        for units_data in unit_items:
            if unit == units_data:
                for element in unit_items[units_data]:
                    if element not in new_unit_items[unit]:
                        new_unit_items[unit][element] = 1
                    else:
                        new_unit_items[unit][element] += 1
    for key in new_unit_items:
        new_unit_items[key] = dict(sorted(new_unit_items[key].items(), key=lambda x: x[1], reverse=True))
    return new_unit_items