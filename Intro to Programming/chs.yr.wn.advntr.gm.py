'''
Grade Calculator Team Activity Assignment
Last Updated: 10/29/24
Author: Michael Jacob (MJ) Quizon

1. You need to have at least three levels of scenarios with possible choices.
2. At least one of your scenarios must have more than two possible choices.
3. In each prompt, write the choices in ALL CAPS, so that the user knows which words are possible responses to choose.
4. When checking the users responses, you should match on the keyword, 
regardless of the uppercase/lowercase used in the response (e.g., "match", "MATCH", "Match" should all work).
5. Making different choices should take you to different scenarios. (You shouldn't have the same result for different choices.)
6. Choices should only work for the correct question.
7. In other words, if one scenario resulted in choices of Run/Hide, 
but another resulted in choices Follow/Look, 
you should not be able to respond with "Follow" to the question that asked for Run/Hide.
8. A good way to accomplish this is to have a series of nested if statements. 
(That is, the print and then the next if statement will be within the body/block of the first if statement.)
9. For each question, you should provide an "else" clause to handle the case that the user tries to type something
other than the possible choices. It is up to you how to handle this case.

Milestone Requirements:

1. The program is working for the first question and possible choices, and displays a follow-up response to each choice (including an else condition).
For the milestone, you do not need to implement any additional scenarios/questions, you only need the first one.

2. Create a design for your complete game.
Prepare for the rest of your game by deciding on all the possible prompts, choices, and responses that the user might see.
You should design the complete game, including else conditions.
Then, to finish up the assignment for the next lesson, you'll just need to code up all of these options.
Feel free to write this design out on paper or in a document (Word, Google Docs, Powerpoint, etc.), whatever is most convenient for you.
You should write each possible scenario along with its choices.
Then, for each choice, write the resulting scenario with its choices, etc.
You are not required to submit this design to I-Learn, 
but you should complete it as part of your Milestone to make sure you are prepared to finish the program.

'''
print('-' * 40)

frst_chc = input('''You are reborn into the world of Star Wars. 
You get to choose between joining the LIGHT Side as a Jedi or the DARK side as a Sith.
What side do you choose? ''').lower()

if frst_chc == 'light':
    scnd_chc = input('''\nYou have chosen the Light Side and have been born as a Jedi Padawan in the middle of their training.
On a training expedition to the planet of Lothal, you enounter a hurt Loth-cat. 
    Do you choose to try and SAVE it or do you KILL it and put it out of its misery? ''').lower()
    if scnd_chc == 'save':
        thrd_chc = input('''\nDue to your efforts to save the Loth-cat, it makes a full recovery and now decides to stay with you as a pet.
After a couple of days, you end up in a lightsaber duel with your master. While fighting, you feel a dark presence empowering you. 
    Do you EMBRACE this dark power or do you RESIST it, relying on your power? ''').lower()
        if thrd_chc == 'embrace':
            print('''\nAfter deciding to embrace this dark power, your attacks become so strong that you end up killing your master in the duel.
You suddenly feel your desires consume you and in this dark state you end up killing your pet Loth-cat,
ending this quick journey as you embace the dark side of the force''')
        elif thrd_chc == 'resist':
            print('''\nYou shake your head and resist the power, instead relying on your own and your pet Loth-cat's power. With your combined efforts,
your skills improve and you're able to fight your master to a stalemate,
ending this quick journey as you begin to grow in the light side of the force.''')       
    elif scnd_chc == 'kill':
        thrd_chc = input('''\nWith a heavy heart, you pull out your lightsaber and ignite it against the Loth-cat's head, killing it instantly.
When you return to camp, you notice your master asleep and you get a thought of igniting your lightsaber again but instead
at your master's head. 
    Do you let this dark desire INFLUENCE you or do you IGNORE it and start mediating instead? ''').lower()
        if thrd_chc == 'influence':
            print('''\nWhen you decide to let this desire influence you, you sneak up on your master while sleeping and ignite the lightsaber against his head,
killing him as instantly as the Loth-cat. By doing this, you claim your master's lightsaber and the dark side begins to consume you.
This quick journey ends as you begin to turn into a ruthless, dual lightsaber wielding killer,
slaying any organics you see on Lothal's plains with the power of the dark side''')
        elif thrd_chc == 'ignore':
            print('''\nBy choosing to ignore it, you instead find a quiet place in camp and begin to start meditating.
This quick journey ends by with you contemplating your recent choices and feeling good that in the end, you made the right choices
as you begin to slowly grow stronger in the light side of the force''')
        else:
            print('\nYou spontaneously collpase from lack of brain cells... Have a nice day')
    else:
        print('''\nBy picking a "3rd" option, you take too long to decide and with what little strength remaining,
the Loth-cat jumps and ends your life... Have a nice day''')
elif frst_chc == 'dark':
    scnd_chc = input('''\nYou have chosen the Dark Side and been born as a secret Sith Apprentice to a powerful Sith Lord.
While you are out buying supplies for your master, you find a blaster and a wallet full of credits and identification.
Do you steal the WALLET and keep the money for yourself, 
steal the BLASTER, or do you try to find the owner and 
RETURN the items you've found? ''').lower()
    if scnd_chc == 'wallet':
        thrd_chc = input('''\nYou decide to steal the wallet and quickly escape the area. As you head back with the supplies,
you find a trio of thugs trying to swindle your master of his money. 
Do you use the MONEY from the stolen wallet or 
do you ignite your LIGHTSABER, cutting the thugs down where they stand? ''').lower()
        if thrd_chc == 'money':
            print('''\nYou walk up to the thugs and use the money you've stolen to leave you and your master alone.
As they leave, you turn to your master and he looks at you at disappointment, before turning around and heading inside.
This quick journey ends as you enter in with him, wondering why he reacted like that, 
unaware that the light side of the force begins to glow within you''')
        elif thrd_chc == 'lightsaber':
            print('''\nWithout hesitation, you drop the supplies you were holding and rush towards the thugs,
lightsaber in hand, you ignite it and instantly cut the thugs' head off.
This quick journey ends as their bodies collapse and you turn to your master, 
a smile on his face as he sees the power of the dark side growing insdie you''')
        else:
            print('''\nBy choosing a "3rd" option, you take too long in deciding and the thugs see and turn their attention to you, 
beating you to a pulp and leaving you on the street, 
your master going back insde unwilling to help you... Have a nice day''')
    elif scnd_chc == 'blaster':
        thrd_chc = input('''\nYou decide to steal the blaster, hiding it in the supplies you've bought.
As you head back to your master's place, you get stopped by a officer who thinks they saw you steal something.
Do you LIE to the officer, in the hopes that he believes you,
or do you KILL him with the blaster you just stole? ''').lower()
        if thrd_chc == 'lie':
            print('''You try to lie and say that the blaster was your master's that he gave you in self-defence.
The officer looks you up and down, then decides to leave you alone and let you go on your day. Your journey ends
as you head back to your master, the dark side slowly growing inside of you.''')
        elif thrd_chc == 'kill':
            print('''You try to play coy and tell the officer to look into your bag of supplies for the gun. As he
looks through the supplies, you pull out the blaster and try to shoot him. The blaster jams and blows up in your face.
Your journey ends as you end up in the ground, dying from the explosion.''')
        else:
            print('''By choosing a "3rd" option, 
you take too long to decide and the officer takes in you into custody for being suspicious... Have a nice day''')
    elif scnd_chc == 'return':
        thrd_chc = input('''\nBy choosing to return the items, you are able to find the original owner, who turns out is a Jedi Master.
He senses that you are strong in the force but notices the dark side clouds around you. He asks if you want to JOIN him or LEAVE and go
back to your master? ''').lower()
        if thrd_chc == 'join':
            print('''\nBy choosing to join the Jedi Master, you end up becoming his padawan and you feel the presence of the dark side leave you
as your journey ends here.''')
        elif thrd_chc == 'leave':
            print('''\nBy choosing to leave him and go back to your master, you end up leading the Jedi back to your master,
where he kills you and your master, ending your journey as you're cut up by his lightsaber.''')
        else:
            print('''\nBy choosing a different option, you take too long in deciding and your head magically implodes, ending your journey quickly.''')
    else:
        print('''\nBy choosing a "4th" option, you take too long in deciding
            and instead the owner of the items finds you and thinks you are stealing his items.
            He grabs you by the clothes as he brings you to an officer and you are put in jail... Have a nice day''')
else:
    print('You have squandered this new oppourtunity that was given to you... Have a nice day')

print('-' * 40)