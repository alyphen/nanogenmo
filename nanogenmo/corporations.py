import json
import random

resource_directory = "./nanogenmo/resources/corporations"


def get_random_car():
    f = open(resource_directory + "/cars.json")
    cars = json.load(f)
    f.close()
    return random.choice(cars['cars'])


def get_random_djia():
    f = open(resource_directory + "/dija.json")
    corporations = json.load(f)
    f.close()
    return random.choice(corporations['corporations'])


def get_random_nasdaq():
    f = open(resource_directory + "/nasdaq.json")
    corporations = json.load(f)
    f.close()
    return random.choice(corporations['corporations'])


def get_random_newspaper():
    f = open(resource_directory + "/newspapers.json")
    newspapers = json.load(f)
    f.close()
    return random.choice(newspapers['newspapers'])
