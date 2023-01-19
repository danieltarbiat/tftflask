import collections
from funcs.generateUnitData import generate_unit_info


def generate_unit_data_list(list_of_units, data):
    units_info_list = {}
    for unit in list_of_units:
        new_unit = generate_unit_info(unit, data)
        units_info_list[unit] = {"unitName": new_unit[0],
                                 "timesPlayed": new_unit[1],
                                 "playrate": new_unit[2],
                                 "averagePlacement": new_unit[3],
                                 "unitImage": new_unit[4],
                                 "unitItems": new_unit[5]
                                 }

    return units_info_list
