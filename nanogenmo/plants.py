import json
import random

resource_directory = "./nanogenmo/resources/plants"


def get_random_flower():
    f = open(resource_directory + "/flowers.json")
    flowers = json.load(f)
    f.close()
    return random.choice(flowers['flowers'])
