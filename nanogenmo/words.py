import json
import random

resource_directory = "./nanogenmo/resources/words"


def get_adjectives():
    f = open(resource_directory + "/adjs.json")
    adjectives = json.load(f)
    f.close()
    return adjectives['adjs']


def get_random_adjective():
    return random.choice(get_adjectives())


def get_common_words():
    f = open(resource_directory + "/common.json")
    commons = json.load(f)
    f.close()
    return commons['commonWords']


def get_random_common_word():
    return random.choice(get_common_words())


def get_nouns():
    f = open(resource_directory + "/nouns.json")
    nouns = json.load(f)
    f.close()
    return nouns['nouns']


def get_random_noun():
    return random.choice(get_nouns())


def get_prefixes():
    f = open(resource_directory + "/prefix_root_suffix.json")
    prefixes_roots_suffixes = json.load(f)
    f.close()
    return prefixes_roots_suffixes['prefixes']


def get_random_prefix():
    return random.choice(get_prefixes())


def get_roots():
    f = open(resource_directory + "/prefix_root_suffix.json")
    prefixes_roots_suffixes = json.load(f)
    f.close()
    return prefixes_roots_suffixes['roots']


def get_random_root():
    return random.choice(get_roots())


def get_suffixes():
    f = open(resource_directory + "/prefix_root_suffix.json")
    prefixes_roots_suffixes = json.load(f)
    f.close()
    return prefixes_roots_suffixes['suffixes']


def get_random_suffix():
    return random.choice(get_suffixes())


def get_proverbs():
    f = open(resource_directory + "/proverbs.json")
    proverbs = json.load(f)
    f.close()
    return proverbs['proverbs']


def get_random_proverb():
    return random.choice(get_proverbs())


def get_shakespeare_sonnets():
    f = open(resource_directory + "/shakespeare_sonnets.json")
    shakespeare_sonnets = json.load(f)
    f.close()
    return shakespeare_sonnets['sonnets']


def get_random_shakespeare_sonnet():
    return random.choice(get_shakespeare_sonnets())


def get_verbs():
    f = open(resource_directory + "/verbs.json")
    verbs = json.load(f)
    f.close()
    return verbs['verbs']


def get_random_verb():
    return random.choice(get_verbs())


def get_adverbs():
    f = open(resource_directory + "/adverbs.json")
    adverbs = json.load(f)
    f.close()
    return adverbs['adverbs']


def get_random_adverb():
    return random.choice(get_adverbs())
