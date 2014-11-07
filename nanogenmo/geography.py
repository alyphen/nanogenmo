import json
import random

resource_directory = "./nanogenmo/resources/geography"


def get_random_country():
    f = open(resource_directory + "/countries.json")
    countries = json.load(f)
    f.close()
    return random.choice(countries['countries'])


def get_random_english_town():
    f = open(resource_directory + "/english_towns_cities.json")
    towns_cities = json.load(f)
    f.close()
    return random.choice(towns_cities['towns'])


def get_random_english_city():
    f = open(resource_directory + "/english_towns_cities.json")
    towns_cities = json.load(f)
    f.close()
    return random.choice(towns_cities['cities'])


def get_random_river():
    f = open(resource_directory + "/rivers.json")
    rivers = json.load(f)
    f.close()
    return random.choice(rivers['rivers'])


def get_random_us_city():
    f = open(resource_directory + "/us_cities.json")
    cities = json.load(f)
    f.close()
    return random.choice(cities['cities'])
