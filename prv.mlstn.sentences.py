'''
Sentences Prove Milestone Assignemnt
Last updated: 05/07/25
Author: Michael Jacob (MJ) Quizon

Write a Python program named sentences.py that generates simple English sentences. 
During this prove milestone, you will write functions that generate sentences with three parts:

    1. a determiner (sometimes known as an article)
    2. a noun
    3. a verb

In other words, your program will build and output sentences in this form:

    Sentence = [Determiner] + [noun] + [verb] + .

For example:

    A cat laughed.
    Some girls thought.
    One man eats.
    Many dogs run.
    The woman will think.
    Many men will write.

For this milestone, your program must include at least these five functions:

    1. main
    2. make_sentence
    3. get_determiner
    4. get_noun
    5. get_verb

You may add other functions if you want. 
The functions get_determiner, get_noun, and get_verb must randomly choose a word from a list of words and return the randomly chosen word. 
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
    make_sentence(cap_determiner, noun, verb)

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

def make_sentence(cap_determiner, noun, verb):
    # Create a sentence with all the required variables
    print(f'''{cap_determiner} {noun} {verb}''')

loop = int(input('How many sentences would you like? '))
for i in range(loop):
    main()
