import json
import random

resource_directory = "./nanogenmo/resources/colors"


def get_random_crayola():
    f = open(resource_directory + "/crayola.json")
    colors = json.load(f)
    f.close()
    return random.choice(colors['colors'])


def get_random_web_color():
    f = open(resource_directory + "/web_colors.json")
    colors = json.load(f)
    f.close()
    return random.choice(colors['colors'])

