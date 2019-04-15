#!/usr/bin/env python3
"""
A text-based RPG with several features like leveling, bosses, difficulties etc.. Gives the possibility to replay with
the same character and gives through that a certain replay value.
"""

# Needed modules/py.-files will be imported here
from random import randint
from time import sleep
import Singleplayer

__author__ = "Dominique Lahl"
__copyright__ = "Copyright 2017, Dominique Lahl"
__version__ = "1.0.0"
__maintainer__ = "Dominique Lahl"
__email__ = "domee.lahl@gmail.com"
__status__ = "Development"                                                                                              # Second py.-file is imported here. Actually only contains enemies and bosses

# Classes will be put into a list here.
CLASSES = ["Warrior", "Archer", "Mage", "Patron of Chaos"]  # classes are set into a list
SEPARATOR = "-" * (len("Character-Editor") + 30)  # universal separator(-length) is set here


def character_editor():
    """
    self explanatory, the main part of the character-editor is in this function. References some other functions in itself
    :return player_name, player_class, player_life, player_intelligence, player_strength, player_sleight_of_hand,
            player_constitution, player_exp, player_level
    """
    character_editor_breaker = True
    while character_editor_breaker:
        print(SEPARATOR + "\n\n" + "Character-Editor".center(len("Character-Editor") + 30) + "\n\n" + SEPARATOR)  # Header is designed
        print("Name".center(len("Character-Editor") + 30))  # This part is for the name of the player. Uses while-loop for decision changes
        decisionpath_name = True
        while decisionpath_name:
            player_name = str(input(SEPARATOR + "\n\nChoose a name fitting your, uhh, glory!: "))
            print("\n" + SEPARATOR + "\n")
            name_choose = input("Your name's {}? Did I get it right?\nWrite [1] if so: ".format(player_name))
            print()
            if name_choose == "1":
                decisionpath_name = False
        decisionpath_class = True  # Class is choosen here.
        print("\n" + SEPARATOR + "\n" + "Class".center(len("Character-Editor") + 30))
        while decisionpath_class:
            print(SEPARATOR + "\n\nWell, well, what you were is not of importance.\nWhat will your profession be?\n")
            counter = 1
            for i in CLASSES:  # prints classes with a for-loop and a bit of formatting
                print("[" + str(counter) + "] " + i)
                counter += 1
            user_input_class = input("\nChoose a class: ")
            input_list = ["1", "2", "3", "4"]  # put the corresponding number for the classes in a list, to bypass the error for int(input
            if user_input_class in input_list:
                player_class = CLASSES[int(user_input_class) - 1]  # changed the type to int here
                print("\n" + SEPARATOR + "\n")
                decision_classes = input("So... you're a {}, huh?\nWrite [1] if you want to continue: "
                                         .format(player_class))
                print()
                if decision_classes == "1":
                    decisionpath_class = False

        # Class of player is asked and either the allocation of skillpoints start or they're assigned randomly
        if player_class == CLASSES[0] or player_class == CLASSES[1] or player_class == CLASSES[2]:
            player_intelligence, player_strength, player_constitution, player_sleight_of_hand = skillpoints_allocation()
        elif player_class == CLASSES[3]:
            player_intelligence, player_strength, player_constitution, player_sleight_of_hand = rnd_skillpoints_allocation()

        # lifepoints of the player are defined
        if player_class == CLASSES[0]:
            player_life = 30
        elif player_class == CLASSES[1]:
            player_life = 30
        elif player_class == CLASSES[2]:
            player_life = 15
        elif player_class == CLASSES[3]:
            if player_strength == 8 or player_intelligence == 8 or player_sleight_of_hand == 8 or player_constitution == 8:
                player_life = 100
            else:
                player_life = randint(15, 50)
        for i in range(0,player_constitution):  # for every point in constitution, the player gets 2 extra lifepoints
            player_life += 2

        player_exp = 0  # player experience and level are set for later use
        player_level = 1
        print("\n\nYour Character is finished! Wow!\n" + SEPARATOR)  # pretty self-explanatory, the character is printed and a final decision is asked.
        print("Name: {}\nClass: {}\nIntelligence: {}\nStrength: {}\nSleight of Hand: {}\nConstitution: {}\n"
              "Lifepoints: {}\nLevel: {}\n".format(player_name, player_class, player_intelligence, player_strength, player_sleight_of_hand,
                                        player_constitution, player_life, player_level) + SEPARATOR)

        character_editor_decision = input("\nYou're finished! Content with your decision?\nIf not, the Character-Editor"    
                                          " will start over again.\nSo be sure of your decision.\nWrite [1] if so: ")
        if character_editor_decision == "1":  # elif is not needed. Any other input will lead to an restart of the creation.
            character_editor_breaker = False
    return player_name, player_class, player_life, player_intelligence, player_strength, \
           player_sleight_of_hand, player_constitution, player_exp, player_level


def skillpoints_allocation():
    """
    Allocation of skillpoints
    :return player_intelligence, player_strength, player_constitution, player_sleight_of_hand:
    """
    player_intelligence = None                                                                                          # Will be set to none, so they can be put into a list
    player_strength = None
    player_sleight_of_hand = None
    player_constitution = None
    skills = [player_intelligence, player_strength, player_sleight_of_hand, player_constitution]
    skill_first_input = ["How many funfacts do you know? (Intelligence): ", "How many nerds can you beat up? "
                         "(Strength): ", "How many knives can you juggle with? (Sleight Of Hand): ", "How long"
                         " can you walk? (Constitution): "]
    skill_less_messages = ["You're not smart enough to persist anywhere. You probably can't read this either but\nas "
                          "nice as I am, I let you reallocate your points.", "You probably wouldn't be able to"
                          " carry a stick, let alone a sword or bow.", "I took away your knives, so you don't "
                          "hurt yourself...","Oh well... you need to be able to walk further than from the kitchen"
                          " to your bed."]
    skill_more_messages = ["Wooow.. smart boy, look at you. So smart that you choose too much intelligence, smh..",
                           "Your planet-like biceps pulverized the arena before you even entered it.","You would juggle"
                           " with the skulls of your enemies!But since that would bring us into legal problems, please"
                           " don't.","You circled the world, no one seems to be able to stop your running, not even you."
                           " Children are crying, the world is burning. But you, you are still running."]
    skill_second_input = ["How many funfacts do you REALLY know? (Intelligence): ", "You don't even need to beat up"
                          " nerds but please be realistic. (Strength): ", "You won't get knives again, what's your "
                          "real ability-value? (Sleight of Hand): ", "Don't lie. Your ability HAS to be between "
                          "laziness and world-destruction, everything else would be unrealistic (Constitution): "]
    skillpoints = 48
    index = 0
    skillpoints_menu = True
    print(SEPARATOR + "\n" + "Skillpoints".center(len("Character-Editor") + 30))
    print(SEPARATOR + "\n\nNow, your abilites are everything. Fighting, running, scratching,\neven singing if you're "
                      "bad enough. So choose wisely.\nYou can't have less than 8 or more than 15 points.")
    print("You have {} points left!\n\n".format(skillpoints) + SEPARATOR)
    while skillpoints_menu:
        if skillpoints == 0:
            skillpoints_menu = False
            print(SEPARATOR)
            print("\nYou have allocated all points! Congrats to this... uhh... amazing achievement!")
        elif skillpoints < 0 or player_constitution == 0:
            print("\n" + SEPARATOR)
            print("\nYou have allocated too much points, start over again.\n" + SEPARATOR)
            skillpoints = 48
            player_constitution = None
            index = 0
        elif skillpoints < 48 and skillpoints > 0 and (None != skills[0] and None != skills[1]and None != skills[2]and None != skills[3]):
            print("\n" + SEPARATOR)
            decision_skills = input("\nYou have not allocated all points, wanna continue?\nWrite [1] if ya want to: ")
            print("\n" + SEPARATOR)
            if decision_skills == "1":
                skillpoints_menu = False
            else:
                skillpoints = 48
                index = 0
        else:
            for items in skills:
                if index == 3:
                    if skillpoints < 8:
                        player_constitution = 0
                        break
                try:
                    skills[index] = int(input("\n{}".format(skill_first_input[index])))
                    while skills[index] < 8 or skills[index] > 15:
                        if skills[index] < 8:
                            print("{}".format(skill_less_messages[index]))
                        else:
                            print("{}".format(skill_more_messages[index]))
                        skills[index] = int(input("\n{}".format(skill_second_input[index])))
                    skillpoints -= skills[index]
                    print("You have {} points left!".format(skillpoints))
                    if index != 3:
                        index += 1
                    else:
                        break
                except ValueError:
                    print("No Integer!")
                    break
    player_intelligence = skills[0]
    player_strength = skills[1]
    player_sleight_of_hand = skills[2]
    player_constitution = skills[3]
    return player_intelligence, player_strength, player_constitution, player_sleight_of_hand


def rnd_player_damage():
    """
    damage for the four classes is set here. Used in fights, not much more. class and abilities are declared local for easier use
    :return randint(1, 6) + bonus_dmg, randint(-5, 10), randint(-15, 30):
    """
    player_class = character[1]
    player_strength = character[3]
    player_intelligence = character[2]
    player_sleight_of_hand = character[4]
    player_constitution = character[5]
    if player_class == CLASSES[0]:
        if player_strength >= 12:
            bonus_dmg = player_strength // 2 - 1
            return randint(1, 6) + bonus_dmg
        else:
             return randint(1, 6) + 4
    elif player_class == CLASSES[1]:
        if player_sleight_of_hand >= 12:
            bonus_dmg = player_sleight_of_hand // 2
            return randint(1, 6) + bonus_dmg
        else:
            return randint(1, 6) + 5
    elif player_class == CLASSES[2]:
        if player_intelligence >= 12:
            bonus_dmg = player_intelligence // 2 + 2
            return randint(1, 6) + bonus_dmg
        else:
            return randint(1, 6) + 7
    elif player_class == CLASSES[3]:
        if player_strength == 8 or player_intelligence == 8 or player_sleight_of_hand == 8 or player_constitution == 8:
            return randint(-5, 10)
        else:
            return randint(-10, 30)


def player_character():
    """
    the character the player wants to use is 'choosen' here
    :return int(player_character_input) - 1, :
    """
    counter = 0
    for items in character_list:
        print("[" + str((counter + 1)) + "] " + character_list[counter][0])
        counter += 1
    player_character_menu = True
    while player_character_menu:
        try:  # Try to check if the input is an integer
            player_character_input = int(input("\nWhich character do you want to play with?: "))
            if player_character_input in range(1, len(character_list) + 1):
                return int(player_character_input) - 1  # gives back the index of the choosen character
        except ValueError:
            print("Please give a number as an input. smh.")


def random_character():
    """
    random character is mainly created here
    :return random_name, random_class, rnd_class_life, random_intelligence, random_strength,
            random_sleight_of_hand, random_constitution:
    """
    random_nameslist = ["Gregory the Great", "Malzahar the Mysterium", "Moira the Moist", "Elysia the Prodigy",
                        "Mahagoni the Standing Tree", "Aaron the Adventurer", "Heinrich", "Seraph the Seraph",
                        "Norbert", "Udo the Unyielding", "Oskar the Omen", "Felicita the Fanatic", "Doskan the Desperado"
                        ,"Lennard the Lender", "Asbest the Bad Building Component", "Doran the Blade", "Aaa the Vowel",
                        "Heras the Heretic", "Ogush the Oven", "Rammon the Es", "Edald the Emmentaler", "Ur the Uncreative"]
    random_name = random_nameslist[randint(0, len(random_nameslist) - 1)]
    random_class = CLASSES[randint(0, len(CLASSES) - 1)]
    random_skillpoints = 48
    while random_skillpoints != 0:
        random_intelligence = randint(8, 15)
        random_skillpoints -= random_intelligence
        random_strength = randint(8, 15)
        random_skillpoints -= random_strength
        random_sleight_of_hand = randint(8, 15)
        random_skillpoints -= random_sleight_of_hand
        if random_skillpoints > 15:
            random_skillpoints = 48
        elif random_skillpoints < 8:
            random_skillpoints = 48
        else:
            random_constitution = randint(8, 15)
            random_skillpoints -= random_constitution

    if random_class == CLASSES[0]:
        rnd_class_life = 30
    elif random_class == CLASSES[1]:
        rnd_class_life = 30
    elif random_class == CLASSES[2]:
        rnd_class_life = 15
    elif random_class == CLASSES[3]:
        if random_strength == 8 or random_intelligence == 8 or random_sleight_of_hand == 8 or random_constitution == 8:
            rnd_class_life = 100
        else:
            rnd_class_life = randint(15, 50)
    for i in range(0, random_constitution):
        rnd_class_life += 2

    return random_name, random_class, rnd_class_life, random_intelligence, random_strength,\
    random_sleight_of_hand, random_constitution


def rnd_skillpoints_allocation():
    """
    skillpoints for the patron of chaos are allocated here
    :return: player_intelligence, player_strength, player_constitution, player_sleight_of_hand
    """
    skillpoints = 48
    while skillpoints != 0:
        player_intelligence = randint(8, 15)
        skillpoints -= player_intelligence
        player_strength = randint(8, 15)
        skillpoints -= player_strength
        player_sleight_of_hand = randint(8, 15)
        skillpoints -= player_sleight_of_hand
        if skillpoints > 15:
            skillpoints = 48
        elif skillpoints < 8:
            skillpoints = 48
        else:
            player_constitution = randint(8, 15)
            skillpoints -= player_constitution
    return player_intelligence, player_strength, player_constitution, player_sleight_of_hand


def set_classes():
    """
    put the random character in a list for further use
    :return set character:
    """
    random_character()
    set_character = []
    random_name, random_class, rnd_class_life, random_intelligence, random_strength, random_sleight_of_hand, random_constitution = random_character()
    random_exp = 0
    random_level = 1
    set_character.append(random_name)
    set_character.append(random_class)
    set_character.append(rnd_class_life)
    set_character.append(random_intelligence)
    set_character.append(random_strength)
    set_character.append(random_sleight_of_hand)
    set_character.append(random_constitution)
    set_character.append(random_exp)
    set_character.append(random_level)
    return set_character


def level_system():
    """
    Level and the needed experience is set here.
    :return None:
    """
    global level_index
    global only_once
    level_exp = [25, 55, 90, 130, 175, 225, 280, 340, 405, 475, 550, 630, 715, 805, 900, 1000]
    for items in level_exp:  # always references the whole list (amount of levels)
        if character[7] > level_exp[level_index] and only_once == level_index:  # only if the players exp are over the needed amount for a level up, the function actually does something
            character[8] += 1  # level of player is set to one higher
            print("\n" + SEPARATOR + "\n\nYou've leveled up! You're level {} now.".format(character[8]))
            print("Only {} exp left 'till the next level!".format(level_exp[level_index+1] - character[7]))
            only_once += 1
            level_index += 1
            level_up()  # references the function for the achievements of a level up, the player will actually notice
        else:  # if no level up happened, the loop will just break and nothing happes
            break


def level_up():
    """
    stat changes and potential sp_allocation of a level up happen here
    :return None:
    """
    global max_life
    character[2] += 5
    max_life += 5
    level_up_menu = True
    if character[8] % 3 == 0:                                                                                           # only every third level the player can allocate another point
        while level_up_menu:
            print("\nYay, you get a bonus skillpoint! invest it wisely.")
            bonus_sp_input = input("\n[1] Intelligence (Current: {})\n[2] Strength (Current: {})\n"
                                   "[3] Sleight of Hand (Current: {})\n[4] Constitution (Current: {})\n\n"
                                   "Which ability should be strengthened?: "
                                   .format(character[3],character[4],character[5],character[6]))
            if bonus_sp_input == "1":
                character[3] += 1
                print("\nYour {} is now {}.".format("Intelligence", character[3]))
                level_up_menu = False
            if bonus_sp_input == "2":
                character[4] += 1
                print("\nYour {} is now {}.".format("Strength", character[4]))
                level_up_menu = False
            if bonus_sp_input == "3":
                character[5] += 1
                print("\nYour {} is now {}.".format("Sleight of Hand", character[5]))
                level_up_menu = False
            if bonus_sp_input == "4":
                character[6] += 1
                print("\nYour {} is now {}.".format("Constitution", character[6]))
                level_up_menu = False


def enemy_field():
    """
    what happens on an enemy field
    :return None:
    """
    enemy = Singleplayer.monsters()  # returned list of function from Singleplayer.py is put into local list
    if difficulty == 1:  # decides which kinda enemies occur, depending on difficulty
        choosen_monster = enemy[randint(0,2)]
    if difficulty == 2:
        choosen_monster = enemy[randint(3,5)]
    if difficulty == 3:
        choosen_monster = enemy[randint(6,8)]

    enemy_dmg = choosen_monster[2]
    enemy_lp = choosen_monster[1]
    print(choosen_monster[0])  # welcoming text of the choosen monster is printed
    while character[2] > 0 and enemy_lp > 0:  # as long as both, player and enemy, are alive, the loop will continue
        try:  # Again Try/ValueError to bypass the int(input error
            print("\nYour survival is at stake, so think carefully what you do!\n")
            fight_input = int(input("1. Attack\n2. Block\n\nWhat do you choose to do?: "))
            if fight_input == 1:
                enemy_decision = randint(1, 2)
                if enemy_decision == 1:
                    print("\nThe enemy attacks back!")
                    enemy_lp -= rnd_player_damage()
                    character[2] -= enemy_dmg
                    print("You've hit! Congrats!\nBut you didn't go out of this unscathed, the enemy hit too.\n"
                          "The enemy has {} life left.\n"
                          "You have {} life left.".format(enemy_lp, character[2]))
                elif enemy_decision == 2:
                    damage_done = rnd_player_damage() - randint(1, 6)
                    if damage_done > 0:
                        enemy_lp -= damage_done
                        print("\nYou hit through his defenses.\nThe enemy has {} life left".format(enemy_lp))
                    else:
                        print("The enemy blocked fully.")
            if fight_input == 2:
                enemy_decision = randint(1, 2)
                if enemy_decision == 1:
                    print("The enemy attacks!")
                    damage_done = enemy_dmg - randint(1, 6)
                    if damage_done > 0:
                        character[2] -= damage_done
                        print("The enemy hit. Welp.\nYou've {} life left".format(character[2]))
                    else:
                        print("You blocked fully. Yay.")
                elif enemy_decision == 2:
                    print("You... both blocked. Dunno what you both were thinking but congrats I suppose.")
        except ValueError:
            print("Same shit, give an integer. smh.")
    if character[2] <= 0:
        print("\nYou life ends here. You try to draw a breath after another\nbut fastly realize that it's futile.")
    elif enemy_lp <= 0:  # enemy dies. You get experience and the level_system-function will be used.
        print("\nYou're exhausted but the enemy lies dead before you. You won.")  # only works when an actual level-up happens, otherwise the game will continue normally
        character[7] += choosen_monster[3]
        level_system()
    print("\n" + SEPARATOR + "\n")
    sleep(5)  # the game waits 5 seconds after end of the stage. for atmosphere


def free_field():
    """
    free field is created with an function on every encounter
    :return None:
    """
    messages = ["The wind plays a soothing melody, light falls through tiny cracks and lights up the darkness around "  # a random message is choosen and printed. nothing more happens, really
                "you. You feel content.", "Funny looking jellyfishes crawl around the walls and emit light blue light, "
                "which falls onto the pelts of apparent mold on the walls. You don't dare to touch it but the calmness "
                "here feels nice.", "A wooden ground, crackling of burning fire and seats and books. Those mushroom-"
                "induced hallucinations just feel as nice as they look, but you better be fast."]
    message = messages[randint(0,len(messages)-1)]
    print(message + "\n\n" + SEPARATOR + "\n")
    sleep(5)


def treasure_field():
    """
    treasure field is designed. Restores health if you're not full health, otherwise does nothing
    :return None:
    """
    print("You see a podest, light and an entranching aura around it.\nThere's something lying there, which makes you\n"
          "feel deeply satisfied. As you get nearer to it, a strong light\nemits in all directions, playing around you"
          "like the wind does on wide coasts.\nYou feel refreshed and almost stronger than before")
    heal_amount = randint(10, 25)
    for items in range(0, heal_amount+1):
        while character[2] < max_life and heal_amount > 0:
            character[2] += 1
            heal_amount -= 1
        break
    print("\n" + SEPARATOR + "\n")
    sleep(5)


def test_field():
    """
    stage for tests is created as a function
    :return None:
    """
    test = tests()
    test_text = test[0]
    print("A challenge awaits!\n" + test_text)
    test_a, test_b, test_c = randint(1, 20), randint(1,20), randint(1, 20)# three value_tests are calculated,
    sleep(5)
    if test_a <= test[1] and test_a <= test[2] and test_a <= test[3]:  # if the abilites of the player (as test[x], created in tests-function) are over the test-values, the player passes
        print("Congrats, you passed! You celebrate by dancing around the room and almost killing\nyourself by running"
              " a bit too fast into a wall. You stumble into the next room...")
    else:  # otherwise the player gets damage
        character[2] -= randint(1,8)
        if character[2] <= 0:  # if the player dies during a test, he gets a sweet little message
            print("You succeed! Nah, only jk, you died. Pretty painfully too.")
        else:
            print("You get by but failed the test. The wounds from your failing are pretty painful.\nA shame because"
                  " they wouldn't be there if you didn't fail but you did fail and failed pretty badly too.")
    print("\n" + SEPARATOR + "\n")
    sleep(5)


def boss_field():  # boss encounter is created here
    """
    boss encounter is created here
    :return None:
    """
    enemy = Singleplayer.bosses()                                                                                       # bosses are imported from Singleplayer.py as list
    if difficulty == 1:                                                                                                 # depending on the difficulty, one of the bosses is choosen
        choosen_boss = enemy[0]
    elif difficulty == 2:
        choosen_boss = enemy[1]
    elif difficulty == 3:
        choosen_boss = enemy[2]

    print(choosen_boss[0])                                                                                              # everything else is pretty much the same as with an normal enemy encounter
    while character[2] > 0 and choosen_boss[1] > 0:
        try:
            print("\nYour survival is at stake, so think carefully what you do!\n")
            fight_input = int(input("1. Attack\n2. Block\n\nWhat do you choose to do?: "))
            if fight_input == 1:
                enemy_decision = randint(1, 2)
                if enemy_decision == 1:
                    print("\nThe enemy attacks back!")
                    choosen_boss[1] -= rnd_player_damage()
                    character[2] -= choosen_boss[2]
                    print("You've hit! Congrats!\nBut you didn't go out of this unscathed, the enemy hit too.\n"
                          "The enemy has {} life left.\n"
                          "You have {} life left.".format(choosen_boss[1], character[2]))
                elif enemy_decision == 2:
                    damage_done = rnd_player_damage() - randint(1, 6)
                    if damage_done > 0:
                        choosen_boss[1] -= damage_done
                        print("\nYou hit through his defenses.\nThe enemy has {} life left".format(choosen_boss[1]))
                    else:
                        print("The enemy blocked fully.")
            if fight_input == 2:
                enemy_decision = randint(1, 2)
                if enemy_decision == 1:
                    print("The enemy attacks!")
                    damage_done = choosen_boss[2] - randint(1, 6)
                    if damage_done > 0:
                        character[2] -= damage_done
                        print("The enemy hit. Welp.\nYou've {} life left".format(character[2]))
                    else:
                        print("You blocked fully. Yay.")
                elif enemy_decision == 2:
                    print("You... both blocked. Dunno what you both were thinking but congrats I suppose.")
        except ValueError:
            print("Same shit, give an integer. smh.")
    if character[2] <= 0:
        print("\nYou life ends here. You try to draw a breath after another\nbut fastly realize that it's futile.")
    elif choosen_boss[1] <= 0:
        print("\nYou're exhausted but the enemy lies dead before you. You won.")
        character[7] += choosen_boss[3]
        level_system()
    print("\n" + SEPARATOR + "\n")
    sleep(5)


def end_boss_stage():
    """
    end boss stage is created here. as with boss and enemy encouter, almost the same
    :return None:
    """
    enemy = Singleplayer.end_boss()
    print(enemy[0])
    while character[2] > 0 and enemy[1] > 0:
        try:
            print("\nYour survival is at stake, so think carefully what you do!\n")
            fight_input = int(input("1. Attack\n2. Block\n\nWhat do you choose to do?: "))
            if fight_input == 1:
                enemy_decision = randint(1, 2)
                if enemy_decision == 1:
                    print("\nThe enemy attacks back!")
                    enemy[1] -= rnd_player_damage()
                    character[2] -= enemy[2]
                    print("You've hit! Congrats!\nBut you didn't go out of this unscathed, the enemy hit too.\n"
                          "The enemy has {} life left.\n"
                          "You have {} life left.".format(enemy[1], character[2]))
                elif enemy_decision == 2:
                    damage_done = rnd_player_damage() - randint(1, 6)
                    if damage_done > 0:
                        enemy[1] -= damage_done
                        print("\nYou hit through his defenses.\nThe enemy has {} life left".format(enemy[1]))
                    else:
                        print("The enemy blocked fully.")
            if fight_input == 2:
                enemy_decision = randint(1, 2)
                if enemy_decision == 1:
                    print("The enemy attacks!")
                    damage_done = enemy[2] - randint(1, 6)
                    if damage_done > 0:
                        character[2] -= damage_done
                        print("The enemy hit. Welp.\nYou've {} life left".format(character[2]))
                    else:
                        print("You blocked fully. Yay.")
                elif enemy_decision == 2:
                    print("You... both blocked. Dunno what you both were thinking but congrats I suppose.")
        except ValueError:
            print("Same shit, give an integer. smh.")
    if character[2] <= 0:                                                                                               # other death and win messages
        print("\nYou feel your soul being sucked out and the torment awaiting you. Nothing you imagined\n"
              "comes close to the agony you're feeling now.")
    elif enemy[1] <= 0:
        print("\nYou won but there's no feel of satisfication. This fight took far more than hard work and wit,\n"
              "an emptiness fills your being. You won this fight, but lost so much more.")
        character[7] += enemy[3]
        level_system()
    print("\n" + SEPARATOR + "\n")
    sleep(5)


def tests():
    """
    tests are defined here and put into a list, which will be returned
    :return test:
    """
    tests = []
    whip_test = ["You see a bunch of whips, lashing around in all directions. There's a door behind them.",
                 character[4], character[5], character[5]]                                                              #soh + soh + soh
    boulder_test = ["A giant boulder lies at the other end of the room, the door seems to be behind it.",
                    character[4], character[4], character[4]]                                                           #str + str + str
    test_of_constitution = ["A giant stone hangs on ropes at hip-level. A pressure plate just below it.\n"
                            "You see a hourglass at the end of the room, seemingly you're supposed to carry\n"
                            "that stone over the button for a certain amount of time."
                            , character[6], character[6], character[6]]                                                 #con + con # con
    test_of_cunning = ["There a three doors infront of you, only one seemingly leading to the right direction.\n"
                       "One is worn and old, one is as new as it can and one has blood and carcasses all over it.",
                       character[3], character[3], character[3]]                                                        #int + int + int
    box_test = ["In the middle of the room stands a box with a key extending from it. There's a maze cut into it\n"
                "and a note lying by it. You need to lead the key out of the box without touching the sides.",
                character[3], character[5], character[5]]                                                               #int + soh + soh
    gym_test = ["Leathern punching bags descend from the ceiling, a funny-looking mechanism connected to them.",
                character[4], character[6], character[6]]                                                               #str + con + con
    wrestling_test = ["A wooden statue stands in the middle of the room. At the ground there's an ever changing\n"
                      "maze of directions to push that statue.", character[3], character[3], character[6]]              #int + int + con
    arm_wrestling_test = ["There's a table in the middle, an arm of steel at the one side and a chair at the other.\n"
                          "The arm looks almost alive and eager to test itself against you. Don't disappoint it.",
                          character[4], character[4], character[5]]                                                     #str + str + soh

    tests.append(whip_test)                                                                                             # tests/traps are appended onto list
    tests.append(boulder_test)
    tests.append(test_of_constitution)
    tests.append(test_of_cunning)
    tests.append(box_test)
    tests.append(gym_test)
    tests.append(wrestling_test)
    tests.append(arm_wrestling_test)
    test = tests[randint(0, len(tests)-1)]                                                                              # random test is choosen and will be given back
    return test                                                                                                         #


def stage_creator():
    """
    stage list will be created here
    :return stages:
    """
    stages = []
    stage_counter = randint(8, 12)                                                                                      # amount of repeats for the while-loop. 8-12
    while stage_counter != 0:                                                                                           # stages are given as string for easier use in the function for the current stage
        stage_decider = randint(1, 1000)
        if 400 >= stage_decider >= 1:
            stages.append("FF")
            stage_counter -= 1
        elif 700 >= stage_decider >= 401:
            stages.append("TF")
            stage_counter -= 1
        elif 900 >= stage_decider >= 701:
            stages.append("EF")
            stage_counter -= 1
        elif 990 >= stage_decider >= 901:
            stages.append("BF")
            stage_counter -= 1
        else:
            stages.append("TRF")
            stage_counter -= 1
    return stages                                                                                                       # gives back list


def cur_stage():
    """
    current stage is choosen here
    :return None:
    """
    global cs_index                                                                                                     # cs_index is created in the main progamm, so it's not resetted every time the function occurs
    current_stage = stages[cs_index]
    if current_stage == "FF":                                                                                           # strings are connected to their according field/stage
        free_field()
    elif current_stage == "TF":
        test_field()
    elif current_stage == "EF":
        enemy_field()
    elif current_stage == "BF":
        boss_field()
    elif current_stage == "TRF":
        treasure_field()
    cs_index += 1


def difficulty_level():
    """
    difficulty is choosen as an int here. does not much more
    :return int(diff_input):
    """
    difficulty_menu = True
    while difficulty_menu:
        print("\n" + SEPARATOR)
        diff_input = input("\nWhat difficulty do you wanna play?\nReminder: The End-Boss is only available on Expert.\n"
                           "\n[1] Easy\n[2] Normal\n[3] Expert\n\n")
        if diff_input == "1" or diff_input == "2" or diff_input == "3":
            return int(diff_input)


if __name__ == '__main__':                                                                                              # main programm starts
    character_list = []                                                                                                 # characters are stored as lists in this list
    game_control = True                                                                                                 # While this is True, the game runs. Will change if "End Game" is choosen
    while game_control:
        print(SEPARATOR + "\n\n" + "The Deepest Dungeon".center(len("Character-Editor") + 30) + "\n\n" + SEPARATOR)     # Header for game start
        print("\n[1] Start Game\n[2] Character-Editor\n[3] Characters\n[4] End Game\n")
        startmenu_error_catcher = True
        while startmenu_error_catcher:
            startmenu_choose = input("What do you choose to do? ")                                                      # No int is used because that would lead to an error if the input is no an integer
            print("\n" + SEPARATOR + "\n")                                                                              # formatting
            if startmenu_choose == "1" or startmenu_choose == "2" or startmenu_choose == "3" or startmenu_choose == "4":#
                startmenu_error_catcher = False
        if startmenu_choose == "1":                                                                                     # you start the game.
            if len(character_list) == 0:                                                                                # if there's no character a message comes and the player is back in the main menu
                print("You don't have a character!\n")
            else:
                character = character_list[player_character()]                                                         # Index from function saved as a variable, so the character can be refenenced in character_list later                                                           #
                max_life = character[2]                                                                                 # This variable is set so that the treasure doesn't heal over the max lifepoints and so that the lifepoints can be restored after game
                difficulty = difficulty_level()                                                                        # Difficulty is set here
                print("\n" + SEPARATOR + "\n")
                stages = stage_creator()                                                                               # stages are set as variable for later use and repeating uss (if the player starts the game anew)
                if character[8] == 1:                                                                                   # only_once and index are only set to zero, if the player is level 1
                    only_once = 0                                                                                       # variable is set so that a level-up for a certain treshold only occurs once
                    level_index = 0                                                                                     # is done out of the function because that led to errors I couldn't identify
                cs_index = 0
                for items in stages:                                                                                    # for loop for the amount of stages in the list
                    if character[2] <= 0:                                                                               # checks after every stage if the player is still alive. if not, a message comes and the player gets back to the main menu with full life
                        break
                    cur_stage()
                if cs_index == len(stages) and character[2] > 0:                                                                             # if the last stage has ended and the difficulty is on expert, the possibility to fight the end boss is given
                    if difficulty == 3:                                                                                 #
                        endboss_decision = True
                        while endboss_decision:
                            try:
                                last_stage = int(input("There's a pitch-black, gigantic door right before you. Are you brave"
                                                       " enough to enter?\n\n[1] Fuck, yes, I can't wait to die!\n"
                                                       "[2] Better not, I'll take the portal back...\n\n"))
                                if last_stage == 1:
                                    end_boss_stage()                                                                           # references function for endboss-stage
                                    endboss_decision = False
                                elif last_stage == 2:
                                    character[2] = max_life                                                                     # life is set to original amount (+ how much you got through level-ups) and player gets back to main menu
                                    print("Cowardish, but wise decision. Better train more, right?")
                                    endboss_decision = False
                            except ValueError:
                                print("Only Integer!")
                if character[2] <= 0:
                    character[2] = max_life
                    print("You died! What?! I'll give you another chance but don't mess up.\n")
                else:
                    character[2] = max_life                                                                             # Happens when you succeed in Easy or Normal
                    print("You made it! Congrats! Now ya can start again or try the endboss.\nPS: He's dangerous!\n")
        elif startmenu_choose == "2":                                                                                   # Character-Editor starts here. Several functions and a list, that is appended to character_list at the end
            created_character = []
            player_name, player_class, player_life, player_intelligence, player_strength, player_sleight_of_hand, player_constitution, player_exp, player_level = character_editor()
            created_character.append(player_name)
            created_character.append(player_class)
            created_character.append(player_life)
            created_character.append(player_intelligence)
            created_character.append(player_strength)
            created_character.append(player_sleight_of_hand)
            created_character.append(player_constitution)
            created_character.append(player_exp)
            created_character.append(player_level)
            character_list.append(created_character[:9])
        elif startmenu_choose == "3":                                                                                   # Character list can be viewed and some stuff else
            character_control = True
            while character_control:
                print(SEPARATOR + "\n")
                for i in range(0, len(character_list)):
                    print(str(i+1) + ". " + character_list[i][0])
                print("\nn. Create random character\nx. Exit menu")
                character_choose = input("\nChoose a character to see his stats: ")
                if character_choose == "n":                                                                             # Creates a random character. Neat for testing
                    rnd_character = set_classes()
                    character_list.append(rnd_character)
                    print()
                elif character_choose == "x":                                                                           # exits menu and player gets back to main menu
                    character_control = False
                elif character_choose <= str(len(character_list)):                                                      # converted len into string, so that a wrong input, restarts the loop instead of giving out a error
                    print(SEPARATOR)                                                                                    # (because int(character_choose) lead to an error every time any wrong input besides a number was given)
                    print("Name: {}\nClass: {}\nIntelligence: {}\nStrength: {}\nSleight of Hand: {}\nConstitution: {}\n"# choosen character is printed. Input comes again immediately, so the player needs to scroll a bit
                          "Lifepoints: {}\nLevel: {}"
                          .format(character_list[int(character_choose)-1][0],character_list[int(character_choose)-1][1],
                                  character_list[int(character_choose)-1][3],character_list[int(character_choose)-1][4],
                                  character_list[int(character_choose)-1][5],character_list[int(character_choose)-1][6],
                                  character_list[int(character_choose)-1][2],character_list[int(character_choose)-1][8]))
        elif startmenu_choose == "4":                                                                                   # simple: Game ends
            game_control = False
