#!/usr/bin/env python3
"""
py.-file with monsters, bosses and endboss, that will be imported to mainfile.
"""

# Needed modules will be imported here
from random import randint

__author__ = "Dominique Lahl"
__copyright__ = "Copyright 2017, Dominique Lahl"
__version__ = "1.0.0"
__maintainer__ = "Dominique Lahl"
__email__ = "domee.lahl@gmail.com"
__status__ = "Development"                                                                                              # Second py.-file is imported here. Actually only contains enemies and bosses


# every function with dmg is the specific damage functions for single enemies.
def raging_spirit_dmg():
    return randint(1, 3) + randint(1, 3) + randint(1, 2) + randint(1, 2)


def wolf_dmg():
    return randint(1, 3)


def wisp_dmg():
    return randint(0,1)


def rabid_frogs_dmg():
    return randint(0, 1) + randint(0, 1) + randint(0, 1) + randint(0, 1) + randint(0, 1) + randint(0, 1) + randint(0, 1) + randint(0, 1) + randint(0, 1) + randint(0, 1) + randint(0, 1) + randint(0, 1) + randint(0, 1) + randint(0, 1) + randint(0, 1)


def clawed_doll_dmg():
    return randint(7,9)


def mimic_dmg():
    attack_decision = randint(1,7)
    if attack_decision in range(0,2):
        return randint(1,4)
    elif attack_decision in range(3,4):
        return randint(0,10)
    elif attack_decision in range(5,6):
        return randint(0,2) + randint(0,2) + randint(0,2) + randint(0,2)


def demonic_jester_dmg():
    return randint(1,8) + randint(6,8)


def snake_skeleton_dmg():
    return randint(6,12)


def distorted_warrior_dmg():
    return randint(9,15)


def monsters():
    """
    monsters are created here, put into a list and appended as a list into another list
    :return:
    """
    monster_list = []

    wolf_lp = randint(8, 12)                                                                                            # lifepoints for every monster are assigned as local variable
    raging_spirit_lp = 5
    snake_skeleton_lp = 20
    rabid_frogs_lp = 15
    distorted_warrior_lp = 17
    clawed_doll_lp = 12
    wisp_lp = 25
    demonic_jester_lp = 25
    mimic_lp = 17

    wolf = ["A plain wolf. Creative... Nothing to fear though.", wolf_lp, wolf_dmg(),6]                              # monster and stats as list
    raging_spirit = ["Wrath fills the air around you as you see a burning spirit,\njumping around in directions you "
                     "never thought were possible", raging_spirit_lp, raging_spirit_dmg(),8]
    snake_skeleton = ["A gigantic snake, completely out of bones, towers before you.",
                      snake_skeleton_lp, snake_skeleton_dmg(),17]
    rabid_frogs = ["A bunch of wild, maniacal frogs jumps around in the room.\nAs you enter, the sole focus lies on you."
                   ,rabid_frogs_lp, rabid_frogs_dmg(),10]
    distorted_warrior = ["A construct of flesh and metal, only faintly comparable to\na human, begins to move. It's "
                         "clumsy moves not really distract\nfrom the danger this poor soul emits.",
                         distorted_warrior_lp, distorted_warrior_dmg(),19]
    clawed_doll = ["A little doll stands before you. It's atrocious looks are only\naccompanied by the questionable "
                   "amount of claws and blades\non a child's toy.",clawed_doll_lp, clawed_doll_dmg(),11]
    wisp = ["A meager white light illuminates the room. To your suprise\nthat light moves with beautiful swiftness "
            "through the room. A wisp!", wisp_lp, wisp_dmg(),4]
    demonic_jester = ["Horrible laughing fills the room and you immediately know it's not something human.\nThe sinister"
                      " grin of a jester welcomes you as you step further into the dark of the room...",
                      demonic_jester_lp, demonic_jester_dmg(),20]
    mimic = ["You step into the next room but are greeted with nothing but walls and mold. But still...\nyou feel "
             "something in this room, something that is watching you. Just as you thought that,\nsomething jumps from"
             " the wall and changes into a perfect image of yourself, before fastly\nchanging into a chair. A mimic."
             ,mimic_lp, mimic_dmg(), 13]

    # Easy Difficulty
    monster_list.append(wolf)
    monster_list.append(raging_spirit)
    monster_list.append(wisp)

    # Normal Difficulty
    monster_list.append(rabid_frogs)
    monster_list.append(clawed_doll)
    monster_list.append(mimic)

    # Expert Difficulty
    monster_list.append(snake_skeleton)
    monster_list.append(distorted_warrior)
    monster_list.append(demonic_jester)

    return monster_list


#damage of boss monsters
def entity_dmg():
    return randint(15,40)


def witch_dmg():
    return randint(5,15) + randint(5,15)


def bosses():
    """
    pretty much the same as with monsters-function, only as bosses
    :return:
    """
    boss_list = []

    moloch_dmg = 10
    moloch_lp = 40
    entity_lp = 40
    witch_lp = 20

    moloch = ["You hear an almost deafening 'thumbing' as you enter the room.\nYou see a giant, probably the most "
              "hideous and gigantic beast you've ever seen,\nthough that's a bit far-fetched for you to say, since "
              "there's no mirror in here.\nAdrenalin begins to build up inside of you, you know that this fight could\n"
              "very well be your end.", moloch_lp, moloch_dmg,25]
    entity = ["A weird darkness fills the room. You feel disturbed, maniacal, enthusiastic, deeply saddened\n"
              "and a lot more all at once. There's standing something... something you can't quite catch\nbut"
              " you feel uneasy just by looking at it.", entity_lp, entity_dmg(),50]
    witch = ["You heard the bubbling and screams long before you entered the room.\nNow you have a dark-"
             "coated witch looking at you, her prominent skin-pores just screaming evil at you.",
             witch_lp, witch_dmg(),35]

    # Easy Difficulty
    boss_list.append(moloch)

    # Normal difficulty
    boss_list.append(witch)

    # Expert Difficulty
    boss_list.append(entity)

    return boss_list


def chaos_dragon_dmg():
    """
    damage of endboss is created as function
    :return:
    """
    amount_of_attacks = randint(2,10)
    for items in range(0, amount_of_attacks+1):
        attack_decision = randint(1,3)
        if attack_decision == 1:
            return randint(5,10)
        elif attack_decision == 2:
            return randint(1,5) + randint(1,5) + randint(1,5) + randint(1,5)
        else:
            return randint(-10,-5) + randint(0,15)


def end_boss():
    """
    almost the same as with mosnters and bosses, only for endboss and with only one possibility
    :return:
    """
    chaos_dragon_lp = 100

    end_boss = ["You dared to enter. You see nothing but dark energy raging around a small plattform in the middle.\n"
                "There's something unsettling about this place and as soon as you saw yourself, screaming in agony,\n"
                "in the typhoon of dark energy around you, you decided to not look into it anymore. You slowly descend\n"
                "the stairs down to the plattform, every step as hard as an everlasting adventure. As you take your\n"
                "last step, a deeply disturbing rumbling begins, playing like a symphony you forgot you ever heard.\n"
                "This place drips with danger, fear and darkness and as soon as you thought that, something steps\n"
                "out of the typhoon. First you only see the head of a dragon, deeply lilac like a sinistershroom,\n"
                "you saw plenty of in this dungeon. There are eyes everywhere on the dragon, the unsettling feeling from\n"
                "before changes to an deeply entranching fear. But you stand, even as the dragon entered from his\n"
                "unholy realm. A monster, multiple times towering everything you've ever seen before. This is it,\n"
                "the fight you were looking for. Giving up is no possibility and losing will end in something far\n"
                "more vile and horrendous than death. So give everything, everything that you have.",
                chaos_dragon_lp, chaos_dragon_dmg(),200]

    return end_boss