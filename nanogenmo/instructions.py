import json
import random

resource_directory = "./nanogenmo/resources/instructions"


def get_random_laundry_care_instruction():
    f = open(resource_directory + "/laundry_care.json")
    laundry_care_instructions = json.load(f)
    f.close()
    return random.choice(laundry_care_instructions['laundry_care_instructions'])
