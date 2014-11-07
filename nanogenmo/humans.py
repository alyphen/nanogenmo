import json
import random

resource_directory = "./nanogenmo/resources/humans"


def get_random_author():
    f = open(resource_directory + "/authors.json")
    authors = json.load(f)
    f.close()
    return random.choice(authors['authors'])


def get_random_british_actor():
    f = open(resource_directory + "/britishActors.json")
    actors = json.load(f)
    f.close()
    return random.choice(actors['britishActors'])


def get_random_first_name():
    f = open(resource_directory + "/firstNames.json")
    first_names = json.load(f)
    f.close()
    return random.choice(first_names['firstNames'])


def get_random_occupation():
    f = open(resource_directory + "/occupations.json")
    occupations = json.load(f)
    f.close()
    return random.choice(occupations['occupations'])


def get_random_prefix():
    f = open(resource_directory + "/prefixes.json")
    prefixes = json.load(f)
    f.close()
    return random.choice(prefixes['prefixes'])


def get_random_rich_person():
    f = open(resource_directory + "/richpeople.json")
    rich_people = json.load(f)
    f.close()
    return random.choice(rich_people['richPeople'])


def get_random_spinal_tap_drummer():
    f = open(resource_directory + "/spinalTapDrummers.json")
    spinal_tap_drummers = json.load(f)
    f.close()
    return random.choice(spinal_tap_drummers['deceasedDrummers'])


def get_random_suffix():
    f = open(resource_directory + "/suffixes.json")
    suffixes = json.load(f)
    f.close()
    return random.choice(suffixes['suffixes'])


def get_random_wrestler():
    f = open(resource_directory + "/wrestlers.json")
    wrestlers = json.load(f)
    f.close()
    return random.choice(wrestlers['wrestlers'])
