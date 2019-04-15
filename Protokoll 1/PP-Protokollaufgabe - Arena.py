#!/usr/bin/env python
__author__ = "Dominique Lahl"
__copyright__ = "Copyright 2017, Dominique Lahl"
__version__ = "1.0.0"
__maintainer__ = "Dominique Lahl"
__email__ = "domee.lahl@gmail.com"
__status__ = "Production"

# Needed randint-modul will be imported here
from random import randint

# Classes will be put into a list here.
classes = ["Warrior", "Archer", "Mage", "Patron of Chaos"]

# This function exists for every random value that is used in fight and doesn't depend on a class.
def rnd_int(min, max):
    return randint(min, max)

# Dummy will be defined here.
dummy_name = "Dummy"
dummy_stats = 10
dummy_life = 30

# Creation of a randomly generated character.
# List of random, self-written names and a variable to set a certrain name out of the list.
random_nameslist = ["Gregory the Great", "Malzahar the Mysterium", "Moira the Moist", "Elysia the Prodigy",
                    "Mahagoni the Standing Tree", "Aaron the Adventurer", "Heinrich", "Seraph the Seraph",
                    "Norbert", "Udo the Unyielding", "Oskar the Omen"]
random_name = random_nameslist[randint(0, len(random_nameslist)-1)]

# Randomly choosen class that is assigned to a variable.
random_class = classes[randint(0, len(classes)-1)]

# the skillpoints will be allocated randomly here.
random_skillpoints = 48
while random_skillpoints != 0:
    random_intelligence = randint(8, 15)
    random_skillpoints -= random_intelligence
    random_strength = randint(8,15)
    random_skillpoints -= random_strength
    random_sleight_of_hand = randint(8,15)
    random_skillpoints -= random_sleight_of_hand
    if random_skillpoints > 15:
        random_skillpoints = 48
    elif random_skillpoints < 8:
        random_skillpoints = 48
    else:
        random_constitution = randint(8, 15)
        random_skillpoints -= random_constitution

# Life of the randomly generated character is generated here. Depends on the given class.
if random_class == classes[0]:
    rnd_class_life = 30
elif random_class == classes[1]:
    rnd_class_life = 30
elif random_class == classes[2]:
    rnd_class_life = 15
elif random_class == classes[3]:
    if random_strength == 8 or random_intelligence == 8 or random_sleight_of_hand == 8 or random_constitution == 8:
        rnd_class_life = 100
    else:
        rnd_class_life = randint(15,50)

# The damage for the randomly generated character defined here. Depends on the damage of the given class.
if random_class == classes[0]:
    if random_strength >= 12:
        bonus_dmg = random_strength // 2 - 1
        def rnd_class_dmg(min, max):
            return randint(1, 6) + bonus_dmg
    else:
        def rnd_class_dmg(min, max):
            return randint(1, 6) + 4
elif random_class == classes[1]:
    if random_sleight_of_hand >= 12:
        bonus_dmg = random_sleight_of_hand // 2
        def rnd_class_dmg(min, max):
            return randint(1, 6) + bonus_dmg
    else:
        def rnd_class_dmg(min, max):
            return randint(1, 6) + 5
elif random_class == classes[2]:
    if random_intelligence >= 12:
        bonus_dmg = random_intelligence // 2 + 2
        def rnd_class_dmg(min, max):
            return randint(1, 6) + bonus_dmg
    else:
        def rnd_class_dmg(min, max):
            return randint(1, 6) + 7
# Damage of the Patron of Chaos. Has multiple options
elif random_class == classes[3]:
    if random_strength == 8 or random_intelligence == 8 or random_sleight_of_hand == 8 or random_constitution == 8:
        def rnd_class_dmg(min, max):
            return randint(-5,10)
    else:
        def rnd_class_dmg(min, max):
            return randint(-15, 30)

# Startmenu.
gamename = "Arena - Fight For Honor"
option_a = "1. Start Game"
option_b = "2. End Game"
gn_len = len(gamename)
seperator_gamemenu = "-" * (gn_len + 15)
print("\n", gamename.center(gn_len + 15), "\n\n", seperator_gamemenu)
print("\n", option_a, "\n", option_b, "\n")
# This exists to make sure no answer out of the given is choosen. Wrong answers will just repeat the question.
gm_error_control = False
while not gm_error_control:
    gm_choose = input(" What do you choose to do?: ")
    if gm_choose == "1" or gm_choose == "2":
        gm_error_control = True

# Here beginns or ends the game
if gm_choose == "2":
    print("\n Thanks for playing. Or not playing, whatever.")
elif gm_choose == "1":
    # Start of the game and you can choose your name. If you change your mind about your name, you get the chance to redo it.
    decisionpath_name = False
    while not decisionpath_name:
        menuname = "Character-Editor"
        print("\n\n\n", menuname.center(gn_len+15), "\n\n", seperator_gamemenu, "\n")
        print(" Here you can choose your destiny!\n Well, actually your character but destiny sounds better.")
        name_character = str(input("\n Choose a name fitting your, uhh, glory!: "))

        print("\n " + seperator_gamemenu + "\n")
        name_choose = input(" Uhh, your name's {}? Did I get it right?\n Write [Yes] if I got it right.\n ".format(name_character))
        if name_choose == "Yes":
            decisionpath_name = True

    # You choose a class and get the chance to change your decision. Wrong answers will lead to keeping you inside the loop.
    decisionpath_class = False
    while not decisionpath_class:
        print("\n", seperator_gamemenu, "\n")
        print(" Whatever you were in your past is not of importance here, decide who you are now.\n")
        for i in classes:
            print("",i)
        chr_class = str(input("\n Choose a class: "))
        if chr_class in classes:
            print("\n", seperator_gamemenu, "\n")
            decision_classes = input(" So... you're a {}, huh?\n"
                                     " Write [Yes] if you want to continue: ".format(chr_class))
            if decision_classes == "Yes":
                decisionpath_class = True

    # At this point the allocation of skillpoints beginns. I used while-loops in a variety of ways to realize certain features. More in other commentaries.
    skill_points = 48
    decisionpath_skills = False
    allocate_breaker = False
    # allocater_breaker and decisionpath_skills are set to easily get out of the loops.
    while not allocate_breaker:
        # If the "Patron of Chaos" is choosen, his skill points will be randomly defined.
        if chr_class == classes[3]:
            while skill_points != 0:
                chr_intelligence = randint(8, 15)
                skill_points -= chr_intelligence
                chr_strength = randint(8, 15)
                skill_points -= chr_strength
                chr_sleight_of_hand = randint(8, 15)
                skill_points -= chr_sleight_of_hand
                if skill_points > 15:
                    skill_points = 48
                elif skill_points < 8:
                    skill_points = 48
                else:
                    chr_constitution = randint(8, 15)
                    skill_points -= chr_constitution
            decisionpath_skills = True

        # The actual allocation begins here
        while decisionpath_skills == False:
            print("\n", seperator_gamemenu, "\n")
            print(" Now, in an arena your abilites are everything. Fighting, running, scratching, even singing if you're "
                  "bad enough. So choose wisely.\n You can't have less than 8 or more than 15 points.\n")
            print(" You have {} points left!".format(skill_points))

            # Intelligence will be allocated here. A while-loop is used to make sure neither too much or not enough points are invested. Left skillpoints will be printed after allocation.
            chr_intelligence = int(input("\n How many funfacts do you know? (Intelligence): "))
            while chr_intelligence < 8 or chr_intelligence > 15:
                if chr_intelligence < 8:
                    print(" You're not smart enough to persist in the arena. You probably can't read this either but as "
                          "nice as I am, I let you reallocate your points.")
                else:
                    print(" Wooow.. smart boy, look at you. So smart that you choose too much intelligence smh..")
                chr_intelligence = int(input("\n How many funfacts do you REALLY know? (Intelligence): "))
            skill_points -= chr_intelligence
            print("\n You have {} points left!".format(skill_points))

            # Strength will be allocated here. A while-loop is used to make sure neither too much or not enough points are invested. Left skillpoints will be printed after allocation.
            chr_strength = int(input("\n How many nerds can you beat up? (Strength): "))
            while chr_strength < 8 or chr_strength > 15:
                if chr_strength < 8:
                    print(" You probably wouldn't be able to carry a stick, let alone a sword or bow.")
                elif chr_strength > 9000:
                    print(" OVER 9... wait, wrong genre.")
                else:
                    print(" Your planet-like biceps pulverized the arena before you even entered it.")
                chr_strength = int(input("\n You don't even need to beat up nerds but please be realistic: "))
            skill_points -= chr_strength
            print("\n You have {} points left!".format(skill_points))

            # Sleight of Hand will be allocated here. A while-loop is used to make sure neither too much or not enough points are invested. Left skillpoints will be printed after allocation.
            chr_sleight_of_hand = int(input("\n How many knives can you juggle with, without killing yourself? "
                                        "(Sleight Of Hand): "))
            while chr_sleight_of_hand < 8 or chr_sleight_of_hand > 15:
                if chr_sleight_of_hand < 8:
                    print(" I took away your knives, so you don't hurt yourself...")
                else:
                    print(" You would juggle with the skulls of your enemies!\n But since that would bring us into legal "
                          "problems, please don't.")
                chr_sleight_of_hand = int(input("\n You won't get knives again, what's your real ability-value?: "))
            skill_points -= chr_sleight_of_hand
            print("\n You have {} points left!".format(skill_points))

            # If it's not possible to spent enough points to get Constitution over 7, the Skillpoints allocation will restart
            if skill_points < 8:
                chr_constitution = 0
            else:
                # Constitution will be allocated here. A while-loop is used to make sure neither too much or not enough points are invested. Left skillpoints will be printed after allocation.
                chr_constitution = int(input("\n How often do you can walk 500 miles? (Constitution): "))
                while chr_constitution < 8 or chr_constitution > 15:
                    if chr_constitution < 8:
                        print(" For the arena you need to walk more than 500 miles and 500 miles more.")
                    else:
                        print(" You circled the world, no one seems to be able to stop your running, not even you. "
                              "Children are crying, the world is burning but you, you are still running.")
                    chr_constitution = int(input("\n At least 4000 miles and max 7500, "
                                                 "everything else would be unrealistic: "))
                skill_points -= chr_constitution
                print("\n You have {} points left!".format(skill_points))

            # Multiple possibilites exist here. If you've spent too much points, the loop will restart. If you haven't spent enough you can choose to continue or restart. Otherwise the game will continue.
            if skill_points == 0:
                decisionpath_skills = True
                print("\n You have allocated all points! Congrats to this... uhh... amazing achievement!")
            elif skill_points < 0 or chr_constitution == 0:
                print("\n You have allocated too much points, start over again.")
                skill_points = 48
            elif skill_points < 48 or skill_points > 0:
                decision_skills = input("\n You have not allocated all points, wanna continue?\n "
                                        "Write [Yes] if ya want to: ")
                if decision_skills == "Yes":
                    decisionpath_skills = True
                else:
                    skill_points = 48

        # Life points of the own class will be set to a single variable for better use
        if chr_class == classes[0]:
            chr_life = 30
        elif chr_class == classes[1]:
            chr_life = 30
        elif chr_class == classes[2]:
            chr_life = 15
        elif chr_class == classes[3]:
            if chr_strength == 8 or chr_intelligence == 8 or chr_sleight_of_hand == 8 or chr_constitution == 8:
                chr_life = 100
            else:
                chr_life = randint(15, 50)

        # Damage of the own class will be set to a single function for better use
        if chr_class == classes[0]:
            if chr_strength >= 12:
                chr_bonus_dmg = chr_strength // 2 - 1
                def rnd_chr_dmg(min, max):
                    return randint(1, 6) + chr_bonus_dmg
            else:
                def rnd_chr_dmg(min, max):
                    return randint(1, 6) + 4
        elif chr_class == classes[1]:
            if chr_sleight_of_hand >= 12:
                chr_bonus_dmg = chr_sleight_of_hand // 2
                def rnd_chr_dmg(min, max):
                    return randint(1, 6) + chr_bonus_dmg
            else:
                def rnd_chr_dmg(min, max):
                    return randint(1, 6) + 5
        elif chr_class == classes[2]:
            if chr_intelligence >= 12:
                chr_bonus_dmg = chr_intelligence // 2 + 2
                def rnd_chr_dmg(min, max):
                    return randint(1, 6) + chr_bonus_dmg
            else:
                def rnd_chr_dmg(min, max):
                    return randint(1, 6) + 7
        # Damage of the Patron of Chaos. Has multiple options
        elif chr_class == classes[3]:
            if chr_strength == 8 or chr_intelligence == 8 or chr_sleight_of_hand == 8 or chr_constitution == 8:
                def rnd_chr_dmg(min, max):
                    return randint(-5, 10)
            else:
                def rnd_chr_dmg(min, max):
                    return randint(-15, 30)

        # Character will be printed and you will be give the chance to reallocate your skillpoints
        print("\n\n Your Character is finished! Wow!\n " + seperator_gamemenu)
        print(" Name: {}\n Class: {}\n Intelligence: {}\n Strength: {}\n Sleight of Hand: {}\n Constitution: {}\n "
              "Lifepoints: {}\n".format(name_character, chr_class, chr_intelligence, chr_strength, chr_sleight_of_hand,
                                                          chr_constitution, chr_life) + " " + seperator_gamemenu)
        arena_error_control = False
        while not arena_error_control:
            decision_arena = input("\n Wanna go at it in the arena, boi?! Or rather not? Now's your last chance!\n "
                                       "Write [Yes] if you're absolutely sure that you want to continue.\n Like, "
                                       "honestly, think about it, you don't look like much, this could be hard...\n "
                                       "Ya can still change if ya want too, just sayin.\n "
                                       "(PS: You can write [I'm a scaredy cat] if ya just want to leave)\n ")
            if decision_arena == "Yes":
                allocate_breaker = True
                arena_error_control += 1
            elif decision_arena == "I'm a scaredy cat":
                print("\n Welp... understandable. Good luck, with.. whatever someone like you can do.")
                quit()
            else:
                arena_error_control = True
                decisionpath_skills = False
                skill_points = 48

    # You choose the enemy of your choice
    enemy_choose = input("\n\n " + seperator_gamemenu +
                         "\n\n You've waited for this moment. All your life was built up to this.\n You hear "
                         "the gleeming glory in the mouths of thousand of ecstatic spectators.\n "
                         "You hear screams of agony from the poor souls that dared to enter before you.\n "
                         "A bright light blinds you as you step into the arena, the adrenaline building\n "
                         "up inside of you makes thinking difficult.\n "
                         "But still, you think you see someone standing before you... who is it?\n\n "
                         "[1] A simple dummy. Where did the screams of agony come from...\n "
                         "[2] A battle-worn Gladiator. Uhh, how scary!\n\n ")

    # Menu for the fight against the dummy. His stats will be printed and the fight will start.
    if enemy_choose == "1":
        print("\n " + seperator_gamemenu + "\n\n A dummy, wise decision!\n")
        print(" Your enemy has the following stats\n Name: {0}\n Class: {0}\n Intelligence: {1}\n Strength: {1}\n "
              "Sleight of Hand: {1}\n Constitution: {1}\n Lifepoints: {2}\n\n"
              .format(dummy_name, dummy_stats, dummy_life)
              + " " + seperator_gamemenu)
        print("\n A battle ensures! One for the future to remember! You blood beginns to boil and\n "
              "with piercing eyes you look at the fiend standing before you!\n "
              "Meanwhile, said enemy just stands there, because... well... he's a dummy.\n\n " + seperator_gamemenu + "\n")
        # A while-loop is used to make sure the fight ends when one has no lifepoints left.
        while dummy_life > 0 and chr_life > 0:
            battlemenu = input(" What do you choose to do?\n\n "
                               "[A] Attack\n "
                               "[B] Block\n "
                               "[X] Give up (Coward!)\n\n ")

            # What happens when "Attack" is choosen. Two possibile conditions exist, both work with their own randomly generated damage and block values
            if battlemenu == "A":
                enemy_decision = rnd_int(1,2)
                # The enemy attacks back. Both characters deal damage to each other.
                if enemy_decision == 1:
                    print("\n The enemy attacks back!")
                    dummy_life -= rnd_chr_dmg(min, max)
                    chr_life -= rnd_int(1,6)
                    print(" You've hit! Surprisingly...\n The enemy has {} life left.\n "
                          "The dummy hit too (What's even more suprising).\n "
                          "You have {} life left.".format(dummy_life, chr_life))
                # The enemy blocks. Damage will be subtracted from a random amount blocked. Any amount of damage under the value blocked will be ignored.
                elif enemy_decision == 2:
                    damage_done = rnd_chr_dmg(min, max) - rnd_int(1,6)
                    if damage_done > 0:
                        dummy_life -= damage_done
                        print("\n His blocking's not that good, since well, he's a dummy. You hit.\n T"
                              "he enemy has {} life left".format(dummy_life))
                    else:
                        print(" He blocked your attack... a... dummy... blocked your attack...")
            # What happens when "Block" is choosen. Two possibile conditions exist, both work with their own randomly generated damage and block values
            elif battlemenu == "B":
                enemy_decision = rnd_int(1, 2)
                # The enemy attacks. Their amount of damage done is subtracted from a random amount blocked. Any amount of damage under the value blocked will be ignored.
                if enemy_decision == 1:
                    print("\n The enemy attacks!")
                    damage_done = rnd_int(1, 6) - rnd_int(1, 6)
                    if damage_done > 0:
                        chr_life -= damage_done
                        print(" You blocked! Wow!\n You've {} life left.".format(chr_life))
                    else:
                        print(" You fully blocked the attack of the dummy! Congrats! Such an... achievement. ")
                # The enemy blocks. Nothing special happens here.
                elif enemy_decision == 2:
                    print("\n You both blocked, so... nothing happened. ")
            # What happens when "Give Up" is choosen. The possibilty to change the decision, otherwise a message will be printed and the programm will end.
            elif battlemenu == "X":
                decision_giveup = input(" Honestly? Like, completely sure?\n "
                                        "Write [Yes] if so.\n ")
                if decision_giveup == "Yes":
                    print(" Disappointment is written with the letters of your name...\n Not really prolly but if it is, it will sound so cool!")
                    quit()

    # Menu for the fight against the randomly generated enemy. His stats will be printed and the fight will start.
    elif enemy_choose == "2":
        print("\n " + seperator_gamemenu + "\n\n A real gladiator. Bold but stupid.")
        print(" Your enemy has the following stats\n\n Name: {}\n Class: {}\n Intelligence: {}\n Strength: {}\n "
              "Sleight of Hand: {}\n Constitution: {}\n Lifepoints: {}\n\n"
              .format(random_name, random_class, random_intelligence, random_strength, random_sleight_of_hand,
                      random_constitution, rnd_class_life)+" "+seperator_gamemenu)
        # A while-loop is used to make sure the fight ends when one has no lifepoints left.
        while rnd_class_life > 0 and chr_life > 0:
            battlemenu = input("\n What do you choose to do?\n\n "
                               "[A] Attack\n "
                               "[B] Block\n "
                               "[X] Give up (Coward!)\n\n ")
            # What happens when "Attack" is choosen. Two possibile conditions exist, both work with their own randomly generated damage and block values
            if battlemenu == "A":
                enemy_decision = rnd_int(1, 2)
                # The enemy attacks back. Both characters deal damage to each other. Damage depends on class.
                if enemy_decision == 1:
                    print("\n The enemy attacks back!")
                    rnd_class_life -= rnd_chr_dmg(min, max)
                    chr_life -= rnd_class_dmg(min, max)
                    print(" You've hit! Surprisingly...\n The enemy has {} life left.\n "
                          "{} hit too.\n "
                          "You have {} life left.".format(rnd_class_life, random_name, chr_life))
                # The enemy blocks. Damage will be subtracted from a random amount blocked. Any amount of damage under the value blocked will be ignored.
                elif enemy_decision == 2:
                    damage_done = rnd_chr_dmg(min, max) - rnd_int(1, 6)
                    if damage_done > 0:
                        rnd_class_life -= damage_done
                        print("\n Your enemy's quite good at blocking, \n but not good enough,"
                              " you still hit.\n "
                              "The enemy has {} life left".format(rnd_class_life))
                    else:
                        print(" {} blocked your attack fully, not all too surprising.".format(random_name))
            # What happens when "Block" is choosen. Two possibile conditions exist, both work with their own randomly generated damage and block values
            elif battlemenu == "B":
                enemy_decision = rnd_int(1, 2)
                # The enemy attacks. Their amount of damage done is subtracted from a random amount blocked. Any amount of damage under the value blocked will be ignored.
                if enemy_decision == 1:
                    print("\n The enemy attacks!")
                    damage_done = rnd_int(1, 6) - rnd_class_dmg(min, max)
                    if damage_done > 0:
                        chr_life -= damage_done
                        print(" You blocked! Wow!\n You've {} life left.".format(chr_life))
                    else:
                        print(" Hot damn, you blocked your enemies attack fully!")
                # The enemy blocks. Nothing special happens here.
                elif enemy_decision == 2:
                    print("\n You both blocked, so... nothing happened. ")
            # What happens when "Give Up" is choosen. The possibilty to change the decision, otherwise a message will be printed and the programm will end.
            elif battlemenu == "X":
                decision_giveup = input(" Honestly? Like, completely sure?\n "
                                        "Write [Yes] if so.\n ")
                if decision_giveup == "Yes":
                    print(
                        " Disappointment is written with the letters of your name...\n Not really prolly but if it is, it will sound so cool!")
                    quit()

    # The end of the game. Either you won or you lost, a specific message will be printed and the program ends.
    print("\n " + seperator_gamemenu + "\n")
    if chr_life <= 0:
        print(" You've lost... Oh well. Glory doesnt' seem to be on your side..\b but a caskin's supposed to be comfy I heard.")
    elif rnd_class_life <= 0:
        print(" You've won! Against all the odds, you came victorious out of this battle!\n"
              " You celebrate with excessive amounts of alcohol and other drugs and with a\n"
              " myriad of willing fans. Your legendary party leads to the wrecking of multiple\n"
              " cities, poverty for the poor soul who said he'll finance this chaotic venture and\n"
              " to the deaths of multiple people, including yourself. Congrats!" )
    elif dummy_life <= 0:
        print(" Wow.")

