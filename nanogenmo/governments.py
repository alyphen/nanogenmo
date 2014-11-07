import json
import random

resource_directory = "./nanogenmo/resources/government"


def get_random_nsa_project():
    f = open(resource_directory + "/nsa_projects.json")
    nsa_projects = json.load(f)
    f.close()
    return random.choice(nsa_projects['codenames'])


def get_random_us_military_operation():
    f = open(resource_directory + "/us_mil_operations.json")
    us_mil_operations = json.load(f)
    f.close()
    return random.choice(us_mil_operations['operations'])
