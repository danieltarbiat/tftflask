from funcs.generateTraitData import generate_trait_data


def generate_trait_list_data(augment_list, data):
    augment_list_info = {}
    for augment in augment_list:
        new_augment = generate_trait_data(augment, data)
        augment_list_info[augment] = {"traitName": new_augment[0],
                                      "timesPlayed": new_augment[1],
                                      "traitStyles": new_augment[2],
                                      "averagePlacement": new_augment[3],
                                      "traitImage": new_augment[4]}
    return augment_list_info
