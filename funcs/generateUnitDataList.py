import collections
from funcs.generateUnitData import generate_unit_info


def generate_unit_data_list(list_of_units, data):
    units_info_list = {}
    for unit in list_of_units:
        new_unit = generate_unit_info(unit, data)
        units_info_list[unit] = {"Unit Name": new_unit[0],
                                 "Times Played": new_unit[1],
                                 "Playrate": new_unit[2],
                                 "Average Placement": new_unit[3],
                                 "Unit Image": new_unit[4],
                                 "Unit Items": new_unit[5]
                                 }

    return units_info_list
