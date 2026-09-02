import json


def load_cache():

    with open("data/cache.json", "r") as file:
        return json.load(file)

def save_cache(cache):

    with open("data/cache.json", "w") as file:
        json.dump(cache, file, indent=4)