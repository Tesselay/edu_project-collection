#!/usr/bin/env python3
"""
Generator for cinema-creation and seat-finding.
"""

# Needed modules will be imported here
from random import randint

__author__ = "Dominique Lahl"
__copyright__ = "Copyright 2018, Dominique Lahl"
__version__ = "1.0.0"
__maintainer__ = "Dominique Lahl"
__email__ = "domee.lahl@gmail.com"
__status__ = "Development"


def cinema_creation():
    rows = 7
    columns = 30
    count = 0
    cinema_list = []
    for items in range(0, rows):
        cinema_list.append([])
        for items in range(0, columns):
            cinema_list[count].append("O ")
        count += 1
    return cinema_list


def cinema_print(list):
    for items_a in list:
        for items_b in items_a:
            print(items_b, end="")
        print()


def cinema_randomization(list):
    rows_rand = randint(0,7)
    columns_rand = randint(0,30)
    count = 0
    for items_a in range(0, rows_rand):
        for items_b in range(0, columns_rand):
            list[count][randint(0,29)] = "X "
        count += 1
    return list


def empty_seat(list):
    count = 0
    seats = []
    for items in list:
        try:
            column = list[count].index("O ")
            if column > 9:
                seat = str(count+1)+str(column+1)
            else:
                seat = str(count+1)+"0"+str(column+1)
            seats.append(seat)
            count += 1
        except ValueError:
            count += 1
    print("\nFirst free seats of the rows:")
    for items in seats:
        print(items)


def seat_group(list):
    loop = True
    while loop:
        try:
            print("Which Cinema?")
            index = 1
            for items in list:
                print("[" + str(index) + "] Cinema 1")
                index += 1
            cinema = int(input(">"))
            loop = False
        except ValueError:
            print("Please give an Integer.")

    group_loop = True
    while group_loop:
        try:
            group = int(input("\nHow many people are you?\n> "))
            group_loop = False
        except ValueError:
            print("You need to give a number. A full one.")

    noR = len(list[cinema-1])
    noC = len(list[cinema-1][0])
    found = False
    for i in range(0, noR):
        for j in range(0, noC + 1 - group):
            if found == False:
                if (list[cinema-1][i][j] == "O "):
                    emptySeats = 0
                    for k in range(j, j + group):
                        if list[cinema-1][i][k] == "O ":
                            emptySeats += 1
                    if emptySeats == group:
                        row = i
                        col = j
                        found = True
    if found:
        print("The first free seat:")
        empty = str(row + 1)
        if col < 9:
            empty = empty + "0" + str(col + 1)
        else:
            empty = empty + str(col + 1)
        print(empty)
        confirmation = input("Do you want to book? Press Enter to confirm.\n> ")
        if confirmation == "":
            name = input("Please enter your Name.\n> ")
            file = open("cinema_booking.txt", "w")
            file.write("Kundenname: " + name)
            for items in range(0, group):
                list[cinema-1][row][col] = "X "
                empty = str(row + 1)
                if col < 9:
                    file.write("\nSeat {}:".format(items + 1) + empty + "0" + str(col + 1))
                    col += 1
                else:
                    file.write("\nSeat {}:".format(items + 1) + empty + str(col + 1))
                    col += 1
            file.close()
    else:
        print("Keine Sitzreihe hat genug Platz!")


def booked(list):
    index_a = 0
    index_b = 0
    file = open("cinema_booked.txt", "w")
    for items_a in list:
        for items_b in list[index_a]:
            if list[index_a][index_b] == "X ":
                if index_b < 9:
                    file.write("Seat: " + str(index_a+1) + "0" + str(index_b+1) + " / ")
                else:
                    file.write("Seat: " + str(index_a+1) + str(index_b+1) + " / ")
            index_b += 1
        file.write("\n")
        index_b = 0
        index_a += 1


def cinema_import():
    loop = True
    while loop:
        try:
            file_name = input("What is the name of the file?\n\n[x] Leave\n\n> ")
            if file_name == "x":
                loop = False
            else:
                index_a = 1
                count = 0
                cinema_list = []
                for items in range(0, 7):
                    cinema_list.append([])
                    index_b = 1
                    for items in range(0, 30):
                        if index_b < 10:
                            if (str(index_a) + "0" + str(index_b)) in open(file_name, "r").read():
                                cinema_list[count].append("X ")
                            else:
                                cinema_list[count].append("O ")
                        if index_b >= 10:
                            if (str(index_a) + str(index_b)) in open(file_name, "r").read():
                                cinema_list[count].append("X ")
                            else:
                                cinema_list[count].append("O ")
                        index_b += 1
                    count += 1
                    index_a += 1
                loop = False
        except:
            print("A file with this name doesn't exist.")

    return cinema_list


def cinema_menu():
    separator = "-" * 50
    cinema_list = []

    print("\n\n" + str.center("Cinexpress", len(separator)) + "\n\n" + separator)
    loop = True
    while loop:
        try:
            menu = int(input("\nWhat do you want to do?\n\n[1] Booking\n[2] Create a cinema hall\n[3] Delete a/Look at cinema hall(s)\n[4] Import a cinema hall\n[5] End Programm\n\n> "))
            if menu == 1:

                seat_group(cinema_list)
            elif menu == 2:
                created_cinema = cinema_creation()
                created_cinema = cinema_randomization(created_cinema)
                cinema_list.append(created_cinema)
            elif menu == 3:
                index = 0
                for items in cinema_list:
                    print("Cinema "+str(index+1))
                    cinema_print(cinema_list[index])
                    print()
                    index += 1
                index = 1
                try:
                    print("\nWhich hall do you want to delete?\n\n[anything] Leave\n")
                    for items in cinema_list:
                        print("["+str(index)+"] Cinema 1")
                        index += 1
                    delete_input = input("\n> ")
                    if int(delete_input) in range(1, len(cinema_list) + 1):
                        cinema_list.remove(cinema_list[int(delete_input)-1])
                    else:
                        print("This cinema doesn't exist.")
                except ValueError:
                    print("You can only give an Integer.")
            elif menu == 4:
                imp_cinema = cinema_import()
                cinema_list.append(imp_cinema)
            elif menu == 5:
                print("Bye!")
                loop = False
        except ValueError:
            print("You can only give an Integer.")
        except NameError:
            print("There is no hall to book for.")


if __name__ == '__main__':
    cinema_menu()

