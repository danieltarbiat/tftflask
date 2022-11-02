def fetch_augment_info(match_info_dictionary):
    i = 1
    augments = {}
    for match in list(match_info_dictionary):
        if i == 21:
            break
        for augment in match_info_dictionary['match' + str(i)]['augments']:
            if augment not in augments:
                augments[augment] = 1
            else:
                augments[augment] += 1
        i += 1
    a = 1
    average_placement_augment = {}
    for match in list(match_info_dictionary):
        if a == 21:
            break
        placement = match_info_dictionary['match' + str(a)]['placement']
        for augment in match_info_dictionary['match' + str(a)]['augments']:
            if augment not in average_placement_augment:
                average_placement_augment[augment] = [placement]
            else:
                average_placement_augment[augment] += [placement]
        a += 1
    sorted_augments = dict(sorted(augments.items(), key=lambda x: (x[1], x[0]), reverse=True))
    total = sum(augments.values())
    for key, val in sorted_augments.items():
        sorted_augments[key] = [val, str(round(val / total * 100, 1)) + '%']
    average_placement_augment = dict(
        sorted(average_placement_augment.items(), key=lambda x: (len(x[1]), x[0]), reverse=True))
    for key in average_placement_augment:
        val = average_placement_augment[key]
        val = round(sum(val) / len(val), 1)
        average_placement_augment[key] = '#' + str(val)
    return sorted_augments, average_placement_augment