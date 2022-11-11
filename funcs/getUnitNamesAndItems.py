def get_unit_names_and_items(dictionary):
    unit_names = {}
    for unit in dictionary:
        if unit not in unit_names:
            unit_names[unit] = []
        for item in dictionary[unit]:
            unit_names[unit] += [item]
    return unit_names
