from funcs.generateTraitData import generate_trait_data


def generate_trait_list_data(augment_list, data):
    augment_list_info = {}
    for augment in augment_list:
        new_augment = generate_trait_data(augment, data)
        augment_list_info[augment] = {"Trait Name": new_augment[0],
                                      "Times Played": new_augment[1],
                                      "Trait Styles": new_augment[2],
                                      "Average Placement": new_augment[3],
                                      "Trait Image": new_augment[4]}
    return augment_list_info
