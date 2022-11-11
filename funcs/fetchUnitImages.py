from urllib.request import Request, urlopen


def fetch_unit_images(dictionary):
    unit_urls = {}
    unit_square_png = {}
    unit_image_urls = {}
    for unit in dictionary:
        unit = unit.lower()
        unit_urls[unit] = "https://raw.communitydragon.org/latest/game/assets/characters/" + unit + "/hud/"
    for unit, url in unit_urls.items():
        try:
            request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
            content = urlopen(request).read()
            text = content.decode('utf-8')
            text = text.split()
            for element in text:
                if 'href' and 'square' in element:
                    if unit not in unit_square_png:
                        unit_square_png[unit] = [element]
        except Exception as e:
            print(unit + " Does not exist.")
    for unit, href in unit_square_png.items():
        start = href[0].find("tft")
        end = href[0].find(".png") + 4
        unit_square_png[unit] = href[0][start:end]
    for unit, url in unit_urls.items():
        for square_unit in unit_square_png:
            if unit == square_unit:
                link = unit_urls[unit]
                square = unit_square_png[unit]
                unit_image_urls[unit] = link + square
    for unit in list(unit_image_urls):
        if "b_" in unit:
            new_unit = unit.replace("b_", "_")
            if new_unit in unit_image_urls:
                unit_image_urls.pop(unit)
            else:
                unit_image_urls[new_unit] = unit_image_urls.pop(unit)
    return unit_image_urls

