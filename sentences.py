'''
Sentences Prove Assignemnt
Last updated: 05/20/25
Author: Michael Jacob (MJ) Quizon
'''
import random

def main():
    quantity = random.randint(1, 10)
    tense = ["past", "present", "future"]
    r_tense = tense_randomizer(tense)
    cap_determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    tense = tense_randomizer(tense)
    verb = get_verb(quantity, tense)
    preposition = get_preposition()
    prepositional_phrase = get_prepositional_phrase(quantity)
    make_sentence(cap_determiner, noun, verb, prepositional_phrase)

def get_determiner(quantity):
    if quantity == 1:
        determiner = ["a", "one", "the"]
    else:
        determiner = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    determiner = random.choice(determiner)
    cap_determiner = determiner.capitalize()
    return cap_determiner

def get_noun(quantity):
    if quantity == 1:
        noun = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        noun = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    
    # Randomly choose and return a noun.
    noun = random.choice(noun)
    return noun

def tense_randomizer(tense):
    # Ranomly choose a tense
    if not tense:
        return None
    return random.choice(tense)

def get_verb(quantity, tense):
    if tense == "past":
        verb = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            verb = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        else:
            verb = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verb = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    # Randomly choose and return a noun.
    verb = random.choice(verb)
    return verb

def get_preposition():
    preposition = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    preposition = random.choice(preposition)
    return preposition

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity).lower()
    noun = get_noun(quantity)
    prepositional_phrase = []
    prepositional_phrase.append(preposition)
    prepositional_phrase.append(determiner)
    prepositional_phrase.append(noun)
    return prepositional_phrase


def make_sentence(cap_determiner, noun, verb, prepositional_phrase):
    # Create a sentence with all the required variables
    print(f'''{cap_determiner} {noun} {verb} {' '.join(prepositional_phrase)}''')

loop = int(input('How many sentences would you like? '))
for i in range(loop):
    main()
