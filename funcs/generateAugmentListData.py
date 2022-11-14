from funcs.generateAugmentData import generate_augment_data


def generate_augment_list_data(augment_list, data):
    augment_list_data = {}
    for augment in augment_list:
        new_augment = generate_augment_data(augment, data)
        augment_list_data[augment] = {"Augment Name":new_augment[0],
                                      "Times Played":new_augment[1],
                                      "Playrate":new_augment[2],
                                      "Average Placement":new_augment[3],
                                      "Augment Image":new_augment[4]}
    return augment_list_data
