import json
import random

resource_directory = "./nanogenmo/resources/technology"


def get_random_computer_science():
    f = open(resource_directory + "/computer_sciences.json")
    computer_sciences = json.load(f)
    f.close()
    return random.choice(computer_sciences['computer_sciences'])


def get_random_firework():
    f = open(resource_directory + "/fireworks.json")
    fireworks = json.load(f)
    f.close()
    return random.choice(fireworks['effects'])


def get_random_gun():
    f = open(resource_directory + "/guns_n_rifles.json")
    guns = json.load(f)
    f.close()
    return random.choice(guns['weapons'])
