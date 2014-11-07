import json
import random

resource_directory = "./nanogenmo/resources/animals"


def get_animals():
    f = open(resource_directory + "/common.json")
    animals = json.load(f)
    f.close()
    return animals['animals']


def get_random_animal():
    return random.choice(get_animals())


def get_dinosaurs():
    f = open(resource_directory + "/dinosaurs.json")
    dinosaurs = json.load(f)
    f.close()
    return dinosaurs['dinosaurs']


def get_random_dinosaur():
    return random.choice(get_dinosaurs())


def get_dogs():
    f = open(resource_directory + "/dogs.json")
    dogs = json.load(f)
    f.close()
    return dogs['dogs']


def get_random_dog():
    return random.choice(get_dogs())
