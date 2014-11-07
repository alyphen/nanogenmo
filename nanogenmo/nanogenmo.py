import archetypes
import humans
import random
import words
import time


class Character(object):
    def __init__(self, first_name, last_name, archetype):
        self.first_name = first_name
        self.last_name = last_name
        self.archetype = archetype

    def get_full_name(self):
        return self.first_name + " " + self.last_name


characters = list()


def generate_characters():
    for archetype in archetypes.get_characters():
        character = Character(humans.get_random_first_name(), humans.get_random_author(), archetype)
        characters.append(character)


def get_random_sentence(capitalise_first, max_recursions):
    choice = random.randrange(2)
    sentence = ""
    if choice == 0 or max_recursions == 0:
        sentence = get_random_noun_phrase() + " " + get_random_verb_phrase()
    elif choice == 1:
        sentence = get_random_sentence(False, max_recursions - 1) + get_random_connective() + get_random_sentence(False, max_recursions - 1)
    if capitalise_first:
        sentence = sentence[0].capitalize() + sentence[1:len(sentence)]
    return sentence


def get_random_connective():
    choice = random.randrange(15)
    if choice == 0:
        return ", and "
    elif choice == 1:
        return ", despite this, "
    elif choice == 2:
        return ", in addition to this, "
    elif choice == 3:
        return ", "
    elif choice == 4:
        return ", however "
    elif choice == 5:
        return ", but "
    elif choice == 6:
        return ", but perhaps "
    elif choice == 7:
        return ", meanwhile "
    elif choice == 8:
        return ", then "
    elif choice == 9:
        return ", finally "
    elif choice == 10:
        return " when "
    elif choice == 11:
        return " while "
    elif choice == 12:
        return " as "
    elif choice == 13:
        return " so "
    elif choice == 14:
        return " and so "


def get_random_noun_phrase():
    choice = random.randrange(5)
    if choice == 0:
        return words.get_random_adjective() + " " + get_random_noun_phrase()
    elif choice == 1:
        return "the " + words.get_random_noun()
    elif choice == 2:
        noun = words.get_random_noun()
        return "an " + noun if ['a', 'e', 'i', 'o', 'u', 'h'].count(noun[0]) > 0 else "a " + noun
    elif choice >= 3:
        return get_random_character().first_name


def get_random_verb_phrase():
    choice = random.randrange(3)
    if choice == 0:
        return words.get_random_verb()['past'] + " " + get_random_noun_phrase()
    elif choice == 1:
        return words.get_random_verb()['past']
    elif choice == 2:
        return words.get_random_adverb() + " " + get_random_verb_phrase()


def get_random_paragraph():
    paragraph = ""
    r = range(random.randrange(15, 20))
    for i in r:
        paragraph += get_random_sentence(True, 5) + ". "
        print " - - Paragraph progress: %d / %d sentences" % (i + 1, len(r))
    return paragraph


def get_random_chapter():
    chapter = ""
    r = range(random.randrange(10, 20))
    for i in r:
        chapter += get_random_paragraph() + "\n\n"
        print " - Chapter progress: %d / %d paragraphs" % (i + 1, len(r))
    return chapter


def get_random_novel():
    novel = ""
    generate_characters()
    for character in characters:
        novel += "%s %s is the %s in this story.\n\n" % (
            character.first_name,
            character.last_name,
            random.choice(
                [character.archetype['name'], random.choice(character.archetype['synonyms'])]
            ) if len(character.archetype['synonyms']) > 0 else character.archetype['name']
        )
    novel += "\n\n"
    r = range(random.randrange(10, 20))
    for i in r:
        novel += "Chapter " + str(i + 1) + ": " + \
                 random.choice([
                     words.get_random_noun(),
                     words.get_random_adjective(),
                     words.get_random_verb()['present'],
                     words.get_random_verb()['past'],
                     get_random_noun_phrase(),
                     get_random_verb_phrase()
                 ]) + \
                 "\n====================\n\n" + \
                 get_random_chapter()
        print "Novel progress: %d / %d chapters" % (i + 1, len(r))
    return novel


def get_random_character():
    return random.choice(characters)

print "File: "
novel_file = "./" + raw_input("> ")
if not novel_file.endswith(".md"):
    novel_file += ".md"
start_time = int(round(time.time() * 1000))
f = open(novel_file, 'w')
f.write(get_random_novel().encode("utf8"))
f.close()
print "Done. (" + str(int(round(time.time() * 1000)) - start_time) + "ms)"
