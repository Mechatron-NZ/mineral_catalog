import json
import os
from collections import OrderedDict
from minerals.models import Mineral


def most_common():
    """counts the number of times each field appears in the json file"""
    with open('minerals.json', encoding="utf8") as datafile:
        data = json.load(datafile)
        name = 0
        image_filename = 0
        image_caption = 0
        category = 0
        formula = 0
        strunz_classification = 0
        crystal_system = 0
        unit_cell = 0
        color = 0
        crystal_symmetry = 0
        cleavage = 0
        mohs_scale_hardness = 0
        luster = 0
        streak = 0
        diaphaneity = 0
        optical_properties = 0
        refractive_index = 0
        crystal_habit = 0
        specific_gravity = 0

        for item in data:

            keys = item.keys()

            name += (1 if "name" in keys else 0)
            image_filename += (1 if "image filename" in keys else 0)
            image_caption += (1 if "image caption" in keys else 0)
            category += (1 if "category" in keys else 0)
            formula += (1 if "formula" in keys else 0)
            strunz_classification += (1 if "strunz classification" in keys else 0)
            crystal_system += (1 if "crystal system" in keys else 0)
            unit_cell += (1 if "unit cell" in keys else 0)
            color += (1 if "color" in keys else 0)
            crystal_symmetry += (1 if "crystal symmetry" in keys else 0)
            cleavage += (1 if "cleavage" in keys else 0)
            mohs_scale_hardness += (1 if "mohs scale hardness" in keys else 0)
            luster += (1 if "luster" in keys else 0)
            streak += (1 if "streak" in keys else 0)
            diaphaneity += (1 if "diaphaneity" in keys else 0)
            optical_properties += (1 if "optical properties" in keys else 0)
            refractive_index += (1 if "refractive index" in keys else 0)
            crystal_habit += (1 if "crystal habit" in keys else 0)
            specific_gravity += (1 if "specific gravity" in keys else 0)

        properties = {
            "name": name,
            "image_filename": image_filename,
            "image_caption": image_caption,
            "category": category,
            "formula": formula,
            "strunz_classification": strunz_classification,
            "crystal_system": crystal_system,
            "unit_cell": unit_cell,
            "color": color,
            "crystal_symmetry": crystal_symmetry,
            "cleavage": cleavage,
            "mohs_scale_hardness": mohs_scale_hardness,
            "luster": luster,
            "streak": streak,
            "diaphaneity": diaphaneity,
            "optical_properties": optical_properties,
            "refractive_index": refractive_index,
            "crystal_habit": crystal_habit,
            "specific_gravity": specific_gravity
        }

        properties = OrderedDict(sorted(properties.items(), key=lambda t: t[1]))
        print(properties)
        properties = list(properties)

        for foo in properties:
            print(foo)


def find_duplicates():
    """checks if more than one mineral is referencing the same image file
    Prints the name of duplicates and the number of minerals in the database vs the number of images"""
    with open('minerals.json', encoding="utf8") as datafile:
        data = json.load(datafile)
        mineral_file_names = []
        for item in data:
            mineral_file_names.append(item["image filename"])
        else:
            pass

        mineral_file_names = list(set(mineral_file_names))

        for name in mineral_file_names:
            entries = list(filter(lambda mineral: mineral["image filename"] == name, data))
            if len(entries) > 1:
                for entry in entries:
                    print(entry['name'])

            entries.append(entries[0])

        print(len(mineral_file_names))
        print(len(entries))


def simple_image_name():
    """modifies the name of the image file to be the mineral name + .jpg"""
    with open('minerals.json', encoding="utf8") as datafile:
        data = json.load(datafile)
        for item in data:
            old = os.path.join('minerals/static', 'images', item["image filename"])
            new = os.path.join('minerals/static', 'images', (item['name'] + ".jpg"))
            os.rename(old, new)
        print("done")


def populate_database():
    """creates Mineral objects for every entry in the json file also populates empty fields"""
    with open('minerals.json', encoding="utf8") as datafile:
        data = json.load(datafile)
        fixtures = []

        for item in data:

            keys = item.keys()

            fixture = {
                "name": item["name"],
                "image_filename": (item["name"] + ".jpg"),
                "image_caption": item["image caption"] if "image caption" in keys else "",
                "category": item["category"] if "category" in keys else "",
                "formula": item["formula"] if "formula" in keys else "",
                "strunz_classification": item["strunz classification"] if "strunz classification" in keys else "",
                "crystal_system": item["crystal system"] if "crystal system" in keys else "",
                "unit_cell": item["unit cell"] if "unit cell" in keys else "",
                "color": item["color"] if "color" in keys else "",
                "crystal_symmetry": item["crystal symmetry"] if "crystal symmetry" in keys else "",
                "cleavage": item["cleavage"] if "cleavage" in keys else "",
                "mohs_scale_hardness": item["mohs scale hardness"] if "mohs scale hardness" in keys else "",
                "luster": item["luster"] if "luster" in keys else "",
                "streak": item["streak"] if "streak" in keys else "",
                "diaphaneity": item["diaphaneity"] if "diaphaneity" in keys else "",
                "optical_properties": item["optical properties"] if "optical properties" in keys else "",
                "refractive_index": item["refractive index"] if "refractive index" in keys else "",
                "crystal_habit": item["crystal habit"] if "crystal habit" in keys else "",
                "specific_gravity": item["specific gravity"] if "specific gravity" in keys else ""
            }
            fixtures.append(fixture)

        for mineral in fixtures:
            Mineral.objects.create(**mineral)

        print('done')
