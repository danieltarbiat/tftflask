def get_item_names(dictionary):
    dictionary = dict(sorted(dictionary.items()))
    units = {}
    for unit, values in dictionary.items():
        if "b_" in unit:
            unit = unit.replace("b_", "_")
            if unit in units:
                units[unit] += values
            else:
                units[unit] = values
        else:
            if unit in units:
                units[unit] += values
            else:
                units[unit] = values
    return units