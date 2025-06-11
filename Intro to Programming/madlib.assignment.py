'''
Week 2 Prove Assignment: Time to attempt an madlib
Author: MJ Quizon
Last Updated: 3/24/24
*Use this multiline line comment tip so you don't have to use # comments all the time
Use this story prompt:
   The other day, I was really in trouble. It all started when I saw a very
   [adjective] [animal] [verb] down the hallway. "[exclamation]!" I yelled. But all
   I could think to do was to [verb] over and over. Miraculously,
   that caused it to stop, but not before it tried to [verb]
   right in front of my family.
'''
#I decided to continue my appoach from a previous assignment and make the code feel like it's talking to the user
import time
#This is used to setup later code

print('Hello I am Baymax, your personal healthcare companion')
for i in range(2):
    print('.')
    time.sleep(1)
print("I noticed that your stress levels are high, let's create an madlib to help calm you down")
for i in range(2):
    print('.')
    time.sleep(1)
#Using this code to make the code feel alive and responsive by using dots and time to "delay" the next message
adjective = input('Give me an adjective: ')
animal = input("Now give me an animal, real or fictional: ")
verb = input("Now I'm going to need a verb: ")
exclamation = input("Now I need a word that you use when you're excited, also known as an exclamation: ")
verb2 = input("This time, I'm going to need a different verb: ")
verb3 = input("I'm now going to need one last verb: ")
print('Excellent, I am now compiling the data together')
for i in range(3):
    print('.')
    time.sleep(1)
print('Here is your adlib: ')
print(f'''\nThe other day, I was really in trouble. It all started when I saw a very
{adjective} {animal} {verb} down the hallway. {exclamation}! I yelled. But all
I could think to do was to {verb2} over and over. Miraculously
that caused it to stop, but not before it tried to {verb3}
right in front of my family
''')