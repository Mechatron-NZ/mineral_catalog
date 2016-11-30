import json
import datetime
import os


def find_duplicates():
    with open('minerals.json', encoding="utf8") as datafile:
        data = json.load(datafile)
        mineral_file_names = []
        for item in data:
            mineral_file_names.append(item["image filename"])

        mineral_file_names = list(set(mineral_file_names))
        clean_data = []

        for name in mineral_file_names:
            entries = list(filter(lambda mineral: mineral["image filename"] == name, data))
            if len(entries) > 1:
                for entry in entries:
                    print(entry['name'])

            clean_data.append(entries[0])

        print(len(mineral_file_names))
        print(len(clean_data))


def simple_image_name():
    with open('minerals.json', encoding="utf8") as datafile:
        data = json.load(datafile)
        for item in data:
            old = os.path.join('static', 'images', item["image filename"])
            new = os.path.join('static', 'images', (item['name'] + ".jpg"))
            os.rename(old, new)
        print("done")


def create_fixture_file():
    with open('minerals.json', encoding="utf8") as datafile:
        data = json.load(datafile)
        fixtures = []

        for pk, item in enumerate(data):

            keys = item.keys()

            fixture = {
                "model": "minerals.mineral",
                "pk": pk,
                "fields": {
                    "name":                  item["name"],
                    "image_filename":        (item["name"] + ".jpg"),
                    "image_caption":         item["image caption"] if "image caption" in keys else "",
                    "category":              item["category"] if "category" in keys else "",
                    "formula":               item["formula"] if "formula" in keys else "",
                    "strunz_classification": item["strunz classification"] if "strunz classification" in keys else "",
                    "crystal_system":        item["crystal system"] if "crystal system" in keys else "",
                    "unit_cell":             item["unit cell"] if "unit cell" in keys else "",
                    "color":                 item["color"] if "color" in keys else "",
                    "crystal_symmetry":      item["crystal symmetry"] if "crystal symmetry" in keys else "",
                    "cleavage":              item["cleavage"] if "cleavage" in keys else "",
                    "mohs_scale_hardness":   item["mohs scale hardness"] if "mohs scale hardness" in keys else "",
                    "luster":                item["luster"] if "luster" in keys else "",
                    "streak":                item["streak"] if "streak" in keys else "",
                    "diaphaneity":           item["diaphaneity"] if "diaphaneity" in keys else "",
                    "optical_properties":    item["optical properties"] if "optical properties" in keys else "",
                    "refractive_index":      item["refractive index"] if "refractive index" in keys else "",
                    "crystal_habit":         item["crystal habit"] if "crystal habit" in keys else "",
                    "specific_gravity":      item["specific gravity"] if "specific gravity" in keys else ""
                }
            }
            fixtures.append(fixture)

        with open('fixtures_minerals.json', 'w') as fixture_file:
            json.dump(fixtures, fixture_file)
        print('done')

if __name__ == "__main__":
    create_fixture_file()
