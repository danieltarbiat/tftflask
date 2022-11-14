from urllib.request import Request, urlopen
import json


def fetch_trait_images(dictionary, json_url, path_url):
    trait_image_links = {}
    request = Request(json_url, headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(request).read()
    data_json = json.loads(response)
    for trait in dictionary:
        for element in data_json:
            if element == "setData":
                for items in data_json[element]:
                    for properties in items:
                        if properties == "traits":
                            for values in items[properties]:
                                if values["apiName"] == trait:
                                    path = values["icon"].lower()
                                    end = path.find(".tex")
                                    path = path[:end] + ".png"
                                    trait_image_links[trait] = path_url + path
    return trait_image_links
