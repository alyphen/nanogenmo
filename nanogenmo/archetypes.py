import json
import random

resource_directory = "./nanogenmo/resources/archetypes"


def get_artifacts():
    f = open(resource_directory + "/artifact.json")
    artifacts = json.load(f)
    f.close()
    return artifacts['artifacts']


def get_random_artifact():
    return random.choice(get_artifacts())


def get_characters():
    f = open(resource_directory + "/character.json")
    characters = json.load(f)
    f.close()
    return characters['characters']


def get_random_character():
    return random.choice(get_characters())


def get_events():
    f = open(resource_directory + "/event.json")
    events = json.load(f)
    f.close()
    return events['events']


def get_random_event():
    return random.choice(get_events())


def get_settings():
    f = open(resource_directory + "/setting.json")
    settings = json.load(f)
    f.close()
    return settings['settings']


def get_random_setting():
    return random.choice(get_settings())
