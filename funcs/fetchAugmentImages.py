from urllib.request import Request, urlopen
import json


def fetch_augment_images(dictionary, json_url, path_url):
    augment_image_links = {}
    request = Request(json_url, headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(request).read()
    data_json = json.loads(response)
    for augment in dictionary:
        for element in data_json:
            for items in data_json[element]:
                for properties in items:
                    if properties == "apiName" and items[properties] == augment:
                        path = items["icon"].lower()
                        end = path.find(".dds")
                        path = path[:end] + ".png"
                        path = path.replace("hexcore", "choiceui")
                        augment_image_links[augment] = path_url + path
    return augment_image_links
