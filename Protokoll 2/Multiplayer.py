#!/usr/bin/env python3
"""
py.-file with multiplayer-functions, that will be imported to mainfile.
"""

# Needed modules will be imported here
from random import randint

__author__ = "Dominique Lahl"
__copyright__ = "Copyright 2018, Dominique Lahl"
__version__ = "1.0.0"
__maintainer__ = "Dominique Lahl"
__email__ = "domee.lahl@gmail.com"
__status__ = "Development"

SEPARATOR = "-" * (len("Character-Editor") + 30)                                                                        # universal separator(-length) is set here

def playfield_size():
    """
    The player can decide on a set gamefield (5x5) or create his own, with separately set rows and columns, meaning he
    can create fields like 5x10 or 27x114.
    :return row, column:
    """
    creator_loop = True
    while creator_loop:
        print(SEPARATOR+"\n\n"+"Multiplayer".center(len(SEPARATOR))+"\n\n"+SEPARATOR)
        creation_question = input("\nDo you want to use the set gamefield or create your own?\n\n"
                                  "[1] Set Gamefield\n[2] Custom Gamefield\n\n")
        if creation_question == "1":
            print("\n"+SEPARATOR+"\n")
            row = 5
            column = 5
            creator_loop = False
        elif creation_question == "2":
            error_saver = True                                                                                          # Another while-loop to not restart the whole menu if a ValueError occurs.
            while error_saver:                                                                                          #
                try:
                    row = None                                                                                          # Set so that the upcoming if-function works
                    column = None                                                                                       #
                    row = int(input("How many rows?: "))
                    column = int(input("How many columns?: "))
                except ValueError:
                    print("Only Integer!")
                if row > 0 and column > 0:
                    print(SEPARATOR)
                    error_saver = False
                    creator_loop = False
    return row, column


def playfield_creation(row, column):
    """
    The playfield is created here.
    :param row:
    :param column:
    :return playfield:
    """
    playfield = []
    counter = 0
    for i in range(0, column):
        playfield.append([])
        for j in range(0, row):
            playfield[counter].append("[  ]")
        counter += 1
    return playfield


def playfield_print(playfield):
    """
    function to print the playfield.
    :param playfield:
    :return:
    """
    for h in playfield:
        for g in h:
            print(g, end="")
        print()


def turn_decider(player_move):
    """
    decides whose turn it is.
    :param player_move:
    :return:
    """
    if player_move == 0:
        other_player = 1
        print("\nIt's Player 1s turn!")
    elif player_move == 1:
        other_player = 0
        print("\nIt's Player 2s turn!")
    return other_player


def movement():
    """
    Whole movement occurs here. Another function checks the position of the players. Error-interception, in case a player
    moves out of the boundaries or into another player. Before the movement-menu, it is checked whether the player at
    turn can attack the other player.
    :return:
    """
    global player_move
    movement_loop = True
    player_move = player_move_dec()
    other_player = turn_decider(player_move)
    used = attack(player_move)
    while used:
        if character_dic[0][2] <= 0 or character_dic[1][2] <= 0:
            movement_loop = False
            break
        print()
        playfield_print(playfield)
        other_player = turn_decider(player_move)
        used = attack(player_move)
    while movement_loop:
        try:
            direction_input = str(input("[w] Up / [s] Down / [a] Left / [d] Right\n> "))
            if direction_input == "w":
                position_x, position_y, other_player_pos_x, other_player_pos_y = pos_check(player_move, other_player)
                position_y -= 1
                if position_y < 0:
                    position_y += 1
                    print("\nChoose another way.")
                elif position_y == other_player_pos_y and position_x == other_player_pos_x:
                    position_y += 1
                    print("\nChoose another way.")
                else:
                    playfield[position_y + 1][position_x] = "[  ]"
                    playfield[position_y][position_x] = player_fieldfigure[player_move]
                    movement_loop = False
            elif direction_input == "s":
                position_x, position_y, other_player_pos_x, other_player_pos_y = pos_check(player_move, other_player)
                position_y += 1
                if position_y > column - 1:
                    position_y -= 1
                    print("\nChoose another way.")
                elif position_y == other_player_pos_y and position_x == other_player_pos_x:
                    position_y -= 1
                    print("\nChoose another way.")
                else:
                    playfield[position_y - 1][position_x] = "[  ]"
                    playfield[position_y][position_x] = player_fieldfigure[player_move]
                    movement_loop = False
            elif direction_input == "a":
                position_x, position_y, other_player_pos_x, other_player_pos_y = pos_check(player_move, other_player)
                position_x -= 1
                if position_x < 0:
                    position_x += 1
                    print("\nChoose another way.")
                elif position_y == other_player_pos_y and position_x == other_player_pos_x:
                    position_x += 1
                    print("\nChoose another way.")
                else:
                    playfield[position_y][position_x + 1] = "[  ]"
                    playfield[position_y][position_x] = player_fieldfigure[player_move]
                    movement_loop = False
            elif direction_input == "d":
                position_x, position_y, other_player_pos_x, other_player_pos_y = pos_check(player_move, other_player)
                position_x += 1
                if position_x > row - 1:
                    position_x -= 1
                    print("\nChoose another way.")
                elif position_y == other_player_pos_y and position_x == other_player_pos_x:
                    position_x -= 1
                    print("\nChoose another way.")
                else:
                    playfield[position_y][position_x - 1] = "[  ]"
                    playfield[position_y][position_x] = player_fieldfigure[player_move]
                    movement_loop = False
        except ValueError:
            print("String.")


def player_move_dec():
    """
    decides which player is at move. Takes the global move_decider variable and after that, alternates between
    the players.
    :return 1:
    :return 0:
    """
    global move_decider
    if move_decider == 0:
        move_decider = 1
        return 0
    elif move_decider == 1:
        move_decider = 0
        return 1


def player_character(characters):
    """
    The first player can decide, with which character he wants to play with.
    :param characters:
    :return character_dic:
    """
    character_description = ["Name:", "Class:", "Lifepoints:"]
    character_loop = True
    while character_loop:
        try:
            index_a = 0
            for items_a in characters:
                index_b = 0
                for items_b in items_a:
                    if index_b == 3:
                        break
                    print(character_description[index_b], items_b)
                    index_b += 1
                print()
                index_a += 1
            character_dec = int(input("\nWith which hero do you want to play?\n\n[1] Ludwig\n[2] Regalian\n> "))
            if character_dec == 1:
                player1 = 0
                player2 = 1
                character_loop = False
            elif character_dec == 2:
                player1 = 1
                player2 = 0
                character_loop = False
        except ValueError:
            print("Integer!")
    character_dic = {0:characters[player1],1:characters[player2]}                                                       # The Keys are 0 and 1 respectively, since I will work with player_move (0 = 1st player, 1 = 2nd Player) as an index
    return character_dic


def attack(player_move):
    """
    Checks if the player at turn is a mage or a warrior and, with another function, checks if the player is in the
    near enough the enemy player to hit him. If so, the attack_menu-function follows.
    :param player_move:
    :return used:
    """
    global character_dic
    if "Mage" in character_dic[player_move]:
        attack = range_check_mage()
        if attack == True:
            used = attack_menu(character_dic)
            return used
    elif "Warrior" in character_dic[player_move]:
        attack = range_check_warrior()
        if attack == True:
            used = attack_menu(character_dic)
            return used


def range_check_mage():
    """
    The mage can only strike in the cardinal directions, but can reach 3 fields far.
    :return True:
    """
    p1_position_x, p1_position_y, p2_position_x, p2_position_y = range_pos_check()
    if p1_position_y == p2_position_y:
        if abs(p1_position_x - p2_position_x) <= 3:
            return True
    if p1_position_x == p2_position_x:
        if abs(p1_position_y - p2_position_y) <= 3:
            return True


def range_check_warrior():
    """
    The warrior can strike in any direction around him, but only 1 field far.
    :return True:
    """
    p1_position_x, p1_position_y, p2_position_x, p2_position_y = range_pos_check()
    if abs(p1_position_y - p2_position_y) <= 1 and abs(p1_position_x - p2_position_x) <= 1:
        return True


def attack_menu(character_dic):
    """
    The player is asked if he wants to attack. If he does, he can't move. If he doesn't, he can move.
    :param character_dic:
    :return:
    """
    global player_move
    att_menu_loop = True
    while att_menu_loop:
        try:
            att_dec = int(input("Do you want to attack?\n\n[1] F*CK YES!\n[2] Nah... rather not tbh.\n\n> "))
            if att_dec == 1:
                if player_move == 1:
                    character_dic[0][2] -= character_dic[player_move][3]
                    print("Player 1 has {} Lifepoints left!".format(character_dic[0][2]))
                    player_move = player_move_dec()
                    return True
                elif player_move == 0:
                    character_dic[1][2] -= character_dic[player_move][3]
                    print("Player 2 has {} Lifepoints left!".format(character_dic[1][2]))
                    player_move = player_move_dec()
                    return True
            if att_dec == 2:
                return False
        except ValueError:
            print("Integer!")


def pos_check(player_move, other_player):
    """
    the position for the movement-function is checked here. Is different from the range_pos_check-function in that it
    checks for the position of the player at turn (and the one not at turn) instead of checking for P1 and P2.
    :param player_mover:
    :param other_player:
    :return position_x, position_y, other_player_pos_x, other_player_pos_y:
    """
    count = 0
    for j in playfield:
        try:
            position_x = playfield[count].index(player_fieldfigure[player_move])
            position_y = count
        except ValueError:
            count += 1
    count = 0
    for i in playfield:
        try:
            other_player_pos_x = playfield[count].index(player_fieldfigure[other_player])
            other_player_pos_y = count
        except ValueError:
            count += 1
    return position_x, position_y, other_player_pos_x, other_player_pos_y


def range_pos_check():
    """
    Checks the position of player1 and player2.
    :return p1_position_x, p1_position_y, p2_position_x, p2_position_y:
    """
    count = 0
    for j in playfield:
        try:
            p1_position_x = playfield[count].index("[P1]")
            p1_position_y = count
        except ValueError:
            count += 1
    count = 0
    for j in playfield:
        try:
            p2_position_x = playfield[count].index("[P2]")
            p2_position_y = count
        except ValueError:
            count += 1
    return p1_position_x, p1_position_y, p2_position_x, p2_position_y


if __name__ == '__main__':
    characters = [["Ludwig", "Warrior", 30, randint(2, 6)], ["Regalian", "Mage", 20, randint(4, 7)]]
    row, column = playfield_size()
    playfield = playfield_creation(row, column)
    player_fieldfigure = ["[P1]","[P2]"]
    playfield[0][randint(0,row-1)] = player_fieldfigure[0]
    playfield[column-1][randint(0,row-1)] = player_fieldfigure[1]
    move_decider = 0                                                                                                    # set for the player_move_dec function to have an variable to start with
    character_dic = player_character(characters)                                                                        # saved as dictionary for working/easier reference
    while character_dic[0][2] > 0 and character_dic[1][2] > 0:
        print("\n"+SEPARATOR+"\n")
        playfield_print(playfield)
        movement()
    if character_dic[0][2] <= 0:
        print("\nHey, Player 2 won, congrats for showing Player 1 who's the real second!")
    if character_dic[1][2] <= 0:
        print("\nHey, Player 1 won! Wow, such an... achievement!")