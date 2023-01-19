from funcs.generateAugmentData import generate_augment_data


def generate_augment_list_data(augment_list, data):
    augment_list_data = {}
    for augment in augment_list:
        new_augment = generate_augment_data(augment, data)
        augment_list_data[augment] = {"augmentName": new_augment[0],
                                      "timesPlayed": new_augment[1],
                                      "playrate": new_augment[2],
                                      "averagePlacement": new_augment[3],
                                      "augmentImage": new_augment[4]}
    return augment_list_data
