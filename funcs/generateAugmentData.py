def generate_augment_data(augment_name, data):
    augment_name = augment_name
    augment_played = 0
    augment_playrate = ""
    augment_avg_place = ""
    augment_image = ""
    for element in data:
        if element == "augment_info_0":
            for properties in data[element]:
                if properties == augment_name:
                    dictionary = data[element]
                    values = dictionary[properties]
                    augment_played = values[0]
                    augment_playrate = values[1]
        if element == "augment_info_1":
            for properties in data[element]:
                if properties == augment_name:
                    dictionary = data[element]
                    for item in dictionary:
                        augment_avg_place = dictionary[item]
        if element == "augment_images":
            for properties in data[element]:
                if properties == augment_name:
                    dictionary = data[element]
                    for item in dictionary:
                        augment_image = dictionary[item]
    return augment_name, augment_played, augment_playrate, augment_avg_place, augment_image
