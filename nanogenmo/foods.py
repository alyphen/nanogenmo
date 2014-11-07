import json
import random

resource_directory = "./nanogenmo/resources/foods"


def get_random_beer_category():
    f = open(resource_directory + "/beer_categories.json")
    beer_categories = json.load(f)
    f.close()
    return random.choice(beer_categories['beer_categories'])


def get_random_beer_style():
    f = open(resource_directory + "/beer_styles.json")
    beer_styles = json.load(f)
    f.close()
    return random.choice(beer_styles['beer_styles'])


def get_random_fruit():
    f = open(resource_directory + "/fruits.json")
    fruits = json.load(f)
    f.close()
    return random.choice(fruits['fruits'])


def get_random_pizza_topping():
    f = open(resource_directory + "/pizzaToppings.json")
    pizza_toppings = json.load(f)
    f.close()
    return random.choice(pizza_toppings['pizzaToppings'])


def get_random_sandwich():
    f = open(resource_directory + "/sandwiches.json")
    sandwiches = json.load(f)
    f.close()
    return random.choice(sandwiches['sandwiches'])


def get_random_vegetable():
    f = open(resource_directory + "/vegetables.json")
    vegetables = json.load(f)
    f.close()
    return random.choice(vegetables['vegetables'])

