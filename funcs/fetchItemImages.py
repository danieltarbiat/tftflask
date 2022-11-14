from urllib.request import Request, urlopen
import json


def fetch_item_images(dictionary, json_url, path_url):
    item_image_links = {}
    request = Request(json_url, headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(request).read()
    data_json = json.loads(response)
    for unit in dictionary:
        for value in dictionary[unit]:
            for element in data_json:
                for items in data_json[element]:
                    for properties in items:
                        if properties == "apiName" and items[properties] == value:
                            path = items["icon"].lower()
                            end = path.find(".dds")
                            path = path[:end] + ".png"
                            if unit not in item_image_links:
                                item_image_links[unit] = [{value: path_url + path}]
                            else:
                                item_image_links[unit] += [{value: path_url + path}]
    return item_image_links
