import json
import random

resource_directory = "./nanogenmo/resources/science"


def get_random_element():
    f = open(resource_directory + "/elements.json")
    elements = json.load(f)
    f.close()
    return random.choice(elements['elements'])


def get_random_planet():
    f = open(resource_directory + "/planets.json")
    planets = json.load(f)
    f.close()
    return random.choice(planets['planets'])


def get_random_toxic_chemical():
    f = open(resource_directory + "/toxic_chemicals.json")
    toxic_chemicals = json.load(f)
    f.close()
    return random.choice(toxic_chemicals['chemicals'])
