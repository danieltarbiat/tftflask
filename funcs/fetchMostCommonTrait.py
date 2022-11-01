from fetchMatchInfo import *


def fetch_most_common_trait(region, summoner_name):
    match_info_dictionary = fetch_match_info(region, summoner_name)
    i = 1
    matches_trait_info = {}
    for match in match_info_dictionary:
        if i == 21:
            break
        for element in match_info_dictionary['match' + str(i)]:
            if element == 'traits':
                placement = match_info_dictionary['match' + str(i)]['placement']
                match_traits = match_info_dictionary['match' + str(i)][element]
                matches_trait_info['match' + str(i)] = [placement, match_traits]
                i += 1
    trait_info_data = {}
    for match in matches_trait_info:
        for trait_properties in matches_trait_info[match]:
            if type(trait_properties) == int:
                placement = trait_properties
            else:
                for trait_properties_elements in trait_properties:
                    trait_name = trait_properties_elements['name']
                    num_units = trait_properties_elements['num_units']
                    active_trait_style = trait_properties_elements['style']
                    if trait_name not in trait_info_data:
                        trait_info_data[trait_name] = [
                            {placement: {'num_units': num_units, 'active_trait_style': active_trait_style}}]
                    else:
                        trait_info_data[trait_name] += [
                            {placement: {'num_units': num_units, 'active_trait_style': active_trait_style}}]
    filtered_trait_info = {}
    for element in trait_info_data:
        trait_name = element
        average_trait_placement_counter = 0
        average_trait_placement = 0
        for properties in trait_info_data[element]:
            for number in properties:
                average_trait_placement_counter += 1
                average_trait_placement += number
        average_trait_placement = average_trait_placement / average_trait_placement_counter
        filtered_trait_info[trait_name] = [(average_trait_placement, average_trait_placement_counter)]
    count_of_trait_style = {}
    for element in trait_info_data:
        trait_name = element
        count_of_trait_style[trait_name] = [{0: 0, 1: 0, 2: 0, 3: 0}]
        for properties in trait_info_data[element]:
            for nested in properties.values():
                for values in nested:
                    if values == 'active_trait_style':
                        if nested[values] == 0:
                            count_of_trait_style[trait_name][0][0] += 1
                        elif nested[values] == 1:
                            count_of_trait_style[trait_name][0][1] += 1
                        elif nested[values] == 2:
                            count_of_trait_style[trait_name][0][2] += 1
                        elif nested[values] == 3:
                            count_of_trait_style[trait_name][0][3] += 1
    return count_of_trait_style, filtered_trait_info


print(fetch_most_common_trait(region,summoner_name))
