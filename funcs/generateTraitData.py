def generate_trait_data(trait_name, data):
    trait_name = trait_name
    trait_played = 0
    trait_styles = {"Bronze": 0,
                    "Silver": 0,
                    "Gold": 0,
                    "Platinum": 0}
    trait_avg_place = ""
    trait_image = ""
    for element in data:
        if element == "most_common_trait_info_0":
            for properties in data[element]:
                if properties == trait_name:
                    dictionary = data[element]
                    for key in dictionary[properties]:
                        for style in key:
                            if style == 0:
                                trait_styles["Bronze"] = key[style]
                            elif style == 1:
                                trait_styles["Silver"] = key[style]
                            elif style == 2:
                                trait_styles["Gold"] = key[style]
                            elif style == 3:
                                trait_styles["Platinum"] = key[style]
        if element == "most_common_trait_info_1":
            for properties in data[element]:
                if properties == trait_name:
                    dictionary = data[element]
                    for item in dictionary[properties]:
                        trait_avg_place = item[0]
                        trait_played = item[1]
        if element == "trait_images":
            for properties in data[element]:
                if properties == trait_name:
                    dictionary = data[element]
                    for item in dictionary:
                        trait_image = dictionary[item]
    return trait_name, trait_played, trait_styles, trait_avg_place, trait_image
