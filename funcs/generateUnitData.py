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
