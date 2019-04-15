#!/usr/bin/env python
# coding=utf-8
__author__ = "Dominique Lahl"
__copyright__ = "Copyright 2018, Dominique Lahl"
__version__ = "1.0.0"
__maintainer__ = "Dominique Lahl"
__email__ = "domee.lahl@gmail.com"
__status__ = "Development"

# Die benoetigten Module/.py-Dateien werden importiert.
import os
from random import randint
from time import sleep
from subfiles.Weapon import Weapon
from subfiles.Monster import Monster
from subfiles.CharacterGroup import CharacterGroup
from subfiles.Map import Map
from classes.Knight import Knight
from classes.Mage import Mage
from classes.Thief import Thief
from classes.Acrobat import Acrobat


# Wichtige Variablen werden global gesetzt.
SEPERATOR = "-" * 50                                                                                                                        # Trenner für versch. Menüpunkte, dient lediglich dem Design.


class Game:
    """
    Klasse die das Spiel samt seiner Funktionen enthält.
    """

    def __init__(self):
        """
        Der Konstruktor, welcher die Instanzen mit den gewünschten Werten erstellt.
        Kein Wert wird übergeben.
        __current_group enthält das Objekt der Heldengruppe, welche für das Spiel ausgewählt wird.
        __classes enthält die Namen der einzelnen Klassen als string. Wichtig für das zählen von Klassen und zum Namen ausgeben bei der
        Charaktererstellung.
        __weapons wird bei Spielbeginn mit Objekten der Klasse Waffe gefüllt. Wird alle existierenden Waffen (inkl. Empty Hand) im Spiel
        enthalten.
        __monsters wird bei Spielbeginn mit Objekten der Klasse Monster gefüllt. Wird alle existierenden Monster im Spiel enthalten.
        """
        self.__current_group = None
        self.__classes = ["Knight", "Mage", "Thief", "Acrobat"]
        self.__weapons = []
        self.__monsters = []

    def create_weapons(self):
        """
        Methode welche aus Listen mit passenden Werten Objekte der Klasse Waffe erstellt und in dem jeweiligen Klassenattribut speichert.
        """
        weapon_name = ["Axe", "Lance", "Wooden Sword", "Empty Hand"]                                                                        # Empty Hand befindet sich in dieser Liste, um dem in die Textdatei geschriebenen Namen Werte zuordnen zu können.
        weapon_dmg = [7, 11, 2, 1]
        weapon_dur = [90, 120, 50, 0]   # Der Haltbarkeitswert der Waffen.
        for items in range(0, len(weapon_name)):
            weapon = Weapon(weapon_name[items], weapon_dmg[items], weapon_dur[items])
            self.__weapons.append(weapon)

    def create_monsters(self):
        """
        Methode welche aus Listen mit passenden Werten Objekte der Klasse Monster erstellt und in dem jeweiligen Klassenattribut speichert.
        """
        monster_names = ["Dire Wolf", "Treant", "Wraith"]
        monster_health = [15, 30, 4]
        monster_attribute = [10, 7, 16]
        monster_experience = [8, 8, 19]
        for items in range(0, len(monster_names)):
            monster = Monster(monster_names[items], monster_health[items], monster_attribute[items], monster_experience[items])
            self.__monsters.append(monster)

    def create_character(self):
        """
        Diese Methode erstellt einen Charakter mit zufälligen Attributswerten und Empty Hand festgelegt als Waffe. Der Name sowie eine
        Klasse ist vom Spieler wählbar. Der Charakter wird dabei in eine Textdatei geschrieben.
        """
        print("\n"+SEPERATOR+"\n")
        class_loop = True
        while class_loop:
            try:
                class_input = input("\n[0] Knight\n[1] Mage\n[2] Thief\n[3] Acrobat\n\n[x] leave\n\nWith what class do "
                                    "you want to play?\n> ")
                if class_input == "x" or class_input == "X":
                    class_loop = False
                elif int(class_input) in range(0,4):
                    class_input = int(class_input)
                    class_loop = False
                else:
                    print("This class doesn't exist.")
            except ValueError:
                print("Only (full) numbers.")
        if type(class_input) == int:
            name = input("What should your characters name be?\n> ")
            with open(os.path.join("characterfiles","characters.txt"), "a") as character_file:                                              # characters.txt wird für hinzufuegen (append) geoeffnet oder erstellt, falls nicht vorhanden.
                character_file.write(name+"\n"+self.__classes[class_input]+"\n"+str(30)+"\n"+str(randint(8,16))+"\n"+
                                     str(randint(8,16))+"\n"+str(randint(8, 16))+"\n"+str(randint(8,16))+"\n"+
                                     str(randint(8, 16))+"\n"+str(randint(8,16))+"\n"+str(randint(8,16))+"\n"+
                                     "Empty Hand"+"\n")
            character_file.close()

    def create_group(self):
        """
        Diese Methode lässt den Spieler eine Gruppe aus den vorhandenen Charakteren erstellen und speichert die Gruppe
        in eine .txt-Datei mit dem Namen der Gruppe.
        """
        character_list = self.find_characters()                                                                                             # Ließt die vorhandenen Charaktere in eine liste ein.
        if len(character_list) < 4:
            print("You need more heroes!")
        else:
            cg_loop = True
            print("\n"+SEPERATOR)
            while True:
                group_name = str(input("\nWhat should your group be called?\n[x] leave\n> "))
                if len(group_name) == 0:                                                                                                    # Es sind einige Bedingungen bezüglich des Namen gestellt.
                    print("The name has to be at least one character long!")
                elif len(group_name) > 25:
                    print("This name is too long!")
                elif group_name == "x" or group_name == "X":
                    cg_loop = False
                    break
                elif group_name in self.find_group_name():
                    print("\nThis group already exists! Delete it in the group-menu or choose a different name.")
                else:
                    break
            while cg_loop:
                with open(os.path.join("characterfiles",group_name+".txt"), "w") as group_file:                                             # Eine Textdatei, welche die Helden enthält, wird mit dem Namen der Gruppe erstellt.
                    error_catch = 4                                                                                                         # Die Wiederholungen der folgenden For-Schleife. Dient dem sicher gehen eines korrekten Ablaufs in Falle eines Fehlers.
                    while error_catch > 0:                                                                                                  # Eine while-, statt eine for-Schleife wird genutzt, da die übergebenen Werte für die range-Funktion nicht dynamisch sind.
                        try:
                            print()
                            for items in range(0, len(character_list)):                                                                     # Zur besseren Übersicht, werden die Namen der Charaktere bei jeder Auswahl ausgegeben.
                                print("[{}] Name: {}".format(str(items), character_list[items][0]))
                            hero_input = int(input("\nWhich hero should be part of your endeavour?\n"
                                                   "(Write his/her ID)\n> "))
                            if hero_input > len(character_list)-1:
                                print("\nThis character doesn't exist!")
                            else:
                                group_file.write(character_list[hero_input][0]+"\n"+character_list[hero_input][1]+"\n"+                     # Ähnlich der .txt-Datei für Charaktere, werden die Werte der Charaktere in die Gruppendatei geschrieben.
                                                 character_list[hero_input][2]+"\n"+character_list[hero_input][3]+"\n"+
                                                 character_list[hero_input][4]+"\n"+character_list[hero_input][5]+"\n"+
                                                 character_list[hero_input][6]+"\n"+character_list[hero_input][7]+"\n"+
                                                 character_list[hero_input][8]+"\n"+character_list[hero_input][9]+"\n"+
                                                 character_list[hero_input][10]+"\n"
                                                 )
                                self.delete_character(hero_input, character_list)
                                error_catch -= 1
                        except ValueError:
                            print("\nOnly (full) numbers!")
                    group_file.write("0\n")                                                                                                 # Schreibt die Erfahrungspunkte der Gruppe in die Datei.
                    group_file.write("0")                                                                                                   # Schreibt das Level der Gruppe in die Datei.
                    group_file.close()
                    cg_loop = False

    def find_characters(self):
        """
        Ließt die Charaktere aus der .txt-Datei aus und speichert sie, samt Attributswerten und Waffenname, in einer
        Liste, welche dann zurückgegeben wird.
        :return: character_list
        """
        character_list = []
        try:
            with open(os.path.join("characterfiles","characters.txt"), "r") as character_file:                                              # Öffnet characters.txt zum lesen (read).
                for counter, value in enumerate(character_file):
                    pass
                counter += 1
                counter = counter / 11
                character_file.seek(0)                                                                                                      # Springt zu Zeile 0 bzw. dem Beginn der Datei, um von dort wieder anzufangen.
                for items_a in range(0, int(counter)):
                    list = []                                                                                                               # Erstellt eine temporäre Liste, die dem Speichern der Werte eines Charakters dient.
                    for items_b in range(0, 11):
                        list.append(character_file.readline().rstrip("\n"))                                                                 # Fügt der temporären Liste den Wert einer Zeile hinzu. Entfernt dabei \n, da dies sonst in ebenfalls mit dem Wert gespeichert wird.
                    character_list.append(list)                                                                                             # Fügt die temporäre Liste der Charakterliste hinzu.
        except FileNotFoundError and UnboundLocalError:                                                                                     # Gibt eine Fehlermeldung aus, sollte die Datei nicht existieren oder leer stehen.
            print("There's no character!")
        return character_list

    def find_group_name(self):
        """
        Speichert die Namen der Gruppen in eine Liste und gibt diese aus.
        :return: group_list
        """
        group_list = []
        for file in os.listdir("characterfiles"):                                                                                           # Für jede Datei in dem Verzeichnis der .py-Datei, wird die For-Schleife durchlaufen.
            if file.endswith(".txt"):
                group_list.append(os.path.splitext(file)[0])                                                                                # Die Dateiennamen werden ohne dem Datentyp-Indikator in die Liste hinzugefügt.
        group_list.remove("characters")                                                                                                     # Die characters(.txt)-Datei wird aus der Liste entfernt.
        return group_list

    def find_group_members(self, name):
        """
        Speichert die Charaktere einer Gruppe samt den zugehörigen Werten in eine Liste und gibt diese aus. Kann dies
        auch für Gruppen tun, die weniger als 4 Mitglieder enthält.
        :param name: übergibt den Namen der gewünschten Gruppe.
        :return: character_list
        """
        character_list = []
        with open(os.path.join("characterfiles",name+".txt"), "r") as group_file:
            for counter, value in enumerate(group_file):                                                                                    # Zählt die Zeilen innerhalb der geöffneten Datei. Jeder Charakter entspricht genau 7 Zeilen,
                pass                                                                                                                        # damit können die Charaktere innerhalb der Datei einfach gezählt werden.
            counter -= 1                                                                                                                    # Der Wert wird um 1 verringert, da die erste gezählte Zeile dem Wert 0 entspricht und am Ende der Datei zwei Zeilen für EP und Level stehen.
            counter = counter / 11                                                                                                          # Wird durch 7 gerechnet um auf die Charakteranzahl zu kommen.
            group_file.seek(0)
            for items_a in range(0, int(counter)):
                list = []
                for items_b in range(0, 11):
                    list.append(group_file.readline().rstrip("\n"))
                character_list.append(list)
            experience = group_file.readline().rstrip("\n")                                                                                 # Die vorletze Zeile (Erfahrungspunkte der Gruppe) wird in eine Variable eingelesen.
            level = group_file.readline()                                                                                                   # Die letzte Zeile (Level der Gruppe) wird in eine Variable eingelesen.
            group_file.close()
        return character_list, experience, level

    def delete_character(self, id, list):
        """
        Methode zum löschen eines Charakters.
        :param id: Die ID bzw. der Index, an welcher Stelle sich der Charakter innerhalb der Liste befindet.
        :param list: Die Liste, die den zu löschenden Charakter enthält.
        """
        character_list = list
        character_list.remove(character_list[id])                                                                                           # Entfernt den Charakter an der Stelle der ausgewählten ID.
        with open(os.path.join("characterfiles","characters.txt"), "w") as character_file:                                                  # Öffnet die characters.txt-Datei und überschreibt diese. Dabei werden alle Charaktere außer dem entfernten in die Datei geschrieben.
            for items in range(0, len(character_list)):
                character_file.write(character_list[items][0] + "\n" + character_list[items][1] + "\n" +
                                     character_list[items][2] + "\n" + character_list[items][3] + "\n" +
                                     character_list[items][4] + "\n" + character_list[items][5] + "\n" +
                                     character_list[items][6] + "\n" + character_list[items][7] + "\n" +
                                     character_list[items][8] + "\n" + character_list[items][9] + "\n" +
                                     character_list[items][10] + "\n"
                                     )
        character_file.close()

    def print_characters(self, chr_list, index):
        """
        Methode, welche die mit einer Liste übergebenen Charaktere samt ihrer Werte ausgibt.
        :param chr_list: Liste mit Charakteren.
        """
        character_list = chr_list
        print("\n[{}]\nName: {}\nClass: {}\nLifepoints: {}\nStrength: {}\nDexterity: {}\nIntelligence: {}"
              "\nSleight of hand: {}\nCharisma: {}\nStamina: {}\nIntuition: {}\nWeapon: {}"
              .format(str(index),
                      character_list[index][0], character_list[index][1], character_list[index][2],
                      character_list[index][3], character_list[index][4], character_list[index][5],
                      character_list[index][6], character_list[index][7], character_list[index][8],
                      character_list[index][9], character_list[index][10]))
        cont = input("Press anything to continue!")

    def characters_menu(self):
        """
        Das Charaktermenü. Gibt die Charaktere aus und ermöglicht, einen Charakter zu löschen.
        """
        character_list = self.find_characters()  # Ließt die Charakterliste aus der get_characters-Methode in eine lokale Liste ein.
        chr_menu_loop = True
        print("\n" + SEPERATOR)
        if len(character_list) > 0:
            while chr_menu_loop:
                print()
                menu_input = str(input("Do you want to look into or delete a character?\n[l] look into a character"                         # Der Spieler kann eine ID auswählen und somit einen Charakter löschen oder das Charaktermenü verlassen.
                                       "\n[d] delete a character\n[x] leave\n\n> "))
                possible_inputs = ["x", "X", "d", "D", "l", "L"]                                                                            # Liste mit den möglichen Inputs. Als Liste definiert um simpel Groß- und Kleinschreibung bei der Eingabe zu ermöglichen
                if menu_input in possible_inputs:
                    if menu_input == "x" or menu_input == "X":                                                                              # Als alleinstehende if-Abfrage gesetzt um danach einen input zu verlangen der für die beiden anderen Möglichkeiten wichtig ist.
                        break
                    else:
                        try:
                            for items in range(0, len(character_list)):
                                print("[{}] Name: {}".format(str(items), character_list[items][0]))
                            chr_input = int(input("\nWhat character? (Write the ID)\n(Write anything else to get back)\n> "))
                            if chr_input in range(0, len(character_list)):
                                if menu_input == "d" or menu_input == "D":
                                    self.delete_character(chr_input,character_list)                                                         # Methode zum löschen eines Charakters. Übergibt die ausgewählte ID und die Charakterliste, in welcher sich dieser befindet.
                                elif menu_input == "l" or menu_input == "L":
                                    self.print_characters(character_list, chr_input)
                            else:
                                print("This character doesn't exist!")
                        except ValueError:
                            print("Only (full) numbers.")
                else:
                    print("You can only choose the given options.")

    def groups_menu(self):
        """
        Stellt das Menü für das Gruppenmanagement da. Ermöglicht die einzelnen Charaktere auszugeben und Gruppen zu
        löschen.
        """
        group_list = self.find_group_name()                                                                                                 # Namen der Gruppen werden in eine Liste eingelesen.
        grp_menu_loop = True
        if len(group_list) > 0:
            while grp_menu_loop:
                print("\n"+SEPERATOR+"\n")
                menu_input = str(input("Do you want to look into or delete a group?\n[l] look into a group"
                                       "\n[d] delete a group\n[x] leave\n\n> "))
                possible_inputs = ["x", "X", "d", "D", "l", "L"]                                                                            # Liste mit den möglichen Inputs. Als Liste definiert um simpel Groß- und Kleinschreibung bei der Eingabe zu ermöglichen
                if menu_input in possible_inputs:
                    try:                                                                                                                    # Exception-Handling, da eine Eingabe in Integer umgewandelt wird.
                        if menu_input == "x" or menu_input == "X":                                                                          # Die Eingabe für das Verlassen der Menü wird separat als erstes abgefangen, um einfacher mit den anderen Eingaben zu arbeiten.
                            break
                        for items in range(0, len(group_list)):
                            print("[{}] Name: {}".format(str(items), group_list[items]))
                        grp_input = int(input("\nWhich group? (Write the ID)\n(Write anything else to get back)\n> "))                      # Die Eingabe für die ID,...
                        if grp_input < len(group_list):
                            chr_list, exp, level = self.find_group_members(group_list[grp_input])                                           # ... und das speichern der Charakterwerte etc werden vor den beiden anderen Auswahlmöglichkeiten ausgeführt, da beide Werte davon benötigen.
                            if menu_input == "l" or menu_input == "L":
                                for items in range(0, len(chr_list)):
                                    self.print_characters(chr_list, items)
                                print("\nExperience: {}".format(str(exp)))
                                print("Level: {}".format(str(level)))
                            elif menu_input == "d" or menu_input == "D":
                                with open(os.path.join("characterfiles","characters.txt"), "a") as character_file:                          # Wird die Gruppe gelöscht, werden alle noch lebenden Charaktere wieder zur Auswahl in die characters.txt-Datei geschrieben.
                                    for items in range(0, len(chr_list)):
                                        character_file.write(chr_list[items][0] + "\n" + chr_list[items][1] + "\n" +
                                                             chr_list[items][2] + "\n" + chr_list[items][3] + "\n" +
                                                             chr_list[items][4] + "\n" + chr_list[items][5] + "\n" +
                                                             chr_list[items][6] + "\n" + chr_list[items][7] + "\n" +
                                                             chr_list[items][8] + "\n" + chr_list[items][9] + "\n" +
                                                             chr_list[items][10] + "\n"
                                                             )
                                os.remove(os.path.join("characterfiles",str(group_list[grp_input])+".txt"))
                                group_list.remove(group_list[grp_input])
                        else:
                            print("\nThis group doesn't exist!")
                    except ValueError:
                        print("\nOnly (full) numbers!")
                else:
                    print("You can only choose the given options.")
        else:
            print("There are no groups!")

    def lifepoint_tester(self):
        """
        Testet die Lebenspunkte der Charaktere der Spielgruppe und entfernt einen Charakter, sollten seine unter 0
        fallen.
        :param chr_id: Die ID des zu testenden Charakters wird übergeben.
        """
        for items in range(0, len(self.__current_group.get_heroes())):
            if self.__current_group.get_heroes()[items].get_lifepoints() <= 0:
                print(self.__current_group.get_heroes()[items].get_name() + " died!")
                self.__current_group.get_heroes().remove(self.__current_group.get_heroes()[items])                                          # Mithilfe der .remove-Funktion wird der gestorbene Charakter direkt aus der Heldengruppe entfernt.
                break
            else:
                pass

    def test(self, chr_id, current_test):
        """
        Methode die die Proben sowie zugehöriger Werteveränderungen (der Gruppe) enthält, mit Ausnahme der Kampfprobe, die in eine andere
        Methode verweist. Welche Probe kommt wird durch einen Zufallswert entschieden, welcher in der Map-Klasse innerhalb der Map-Datei
        ausgewürfelt wird.
        :param chr_id: Der Index des Charakters, welcher getestet wird..
        """
        if current_test in range(0,5):                                                                                                      # Kampfprobe
            self.fight()
        elif current_test in range(5,10):                                                                                                   # Fingerfertigkeitsprobe
            print("\n" + self.__current_group.get_heroes()[chr_id].get_name(), "is at turn!")
            print("Your party finds an incautious traveller. {} gets carefully closer..."
                  .format(self.__current_group.get_heroes()[chr_id].get_name()))                                                            # Die Funktion für das erhalten des Namen des Heldenobjekt innerhalb der spielenden Gruppe (Gruppenobjekt) wird direkt angesprochen.
            sleep(1)
            if self.__current_group.get_heroes()[chr_id].pickpocket():
                self.__current_group.set_experience(self.__current_group.get_experience() + 10)
        elif current_test in range(10,15):                                                                                                  # Intelligenzprobe
            print("\n" + self.__current_group.get_heroes()[chr_id].get_name(), "is at turn!")
            print("Your party encounters an unknown event. {} wonders what it could be..."
                  .format(self.__current_group.get_heroes()[chr_id].get_name()))
            sleep(1)
            if self.__current_group.get_heroes()[chr_id].wonder():
                self.__current_group.set_experience(self.__current_group.get_experience()+
                                                    self.__current_group.get_heroes()[chr_id].get_intelligence() * 2)
        elif current_test in range(15,20):                                                                                                  # Geschicklichskeitsprobe
            print("\n" + self.__current_group.get_heroes()[chr_id].get_name(), "is at turn!")
            print("{} has to cross a dangerous river...".format(self.__current_group.get_heroes()[chr_id].get_name()))
            sleep(1)
            if self.__current_group.get_heroes()[chr_id].balance():
                self.__current_group.set_experience(self.__current_group.get_experience() + 2)
        elif current_test == 20:
            print("Your heroes find nothing interesting, though they use this chance to rest.")
            for items in range(0, len(self.__current_group.get_heroes())):
                self.__current_group.get_heroes()[items].rest()
        elif current_test is False:
            pass

    def fight(self):
        """
        Methode für den Kampf. Es wird eine Gruppe von gleichen oder unterschiedlichen Instanzen der Monsterklasse in eine lokale Liste
        gespeichert, die dann als Gegner dienen. Rundenbasierter Kampf in dem sich Helden und Monster abwechseln. Helden können zwischen
        zwei Angriffen auswählen.
        :param chr_id: Der Index des Charakters innerhalb der Charakterlist, welcher kämpft.
        """
        monsterlist = []
        monster_group = randint(1,2)
        print(SEPERATOR)
        if monster_group == 1:
            for items in range(0,randint(1,3)):
                monsterlist.append(self.__monsters[randint(0, 2)])
            print("\nA group of monsters crosses your way, you're forced to fight.\n")
        else:
            monster_type = randint(0, len(self.__monsters))
            for items in range(0, randint(1,3)):
                monsterlist.append(self.__monsters[monster_type])
            print("\nA group of {}s crosses your way, you're forced to fight.\n".format(self.__monsters[monster_type].get_name()))
        turn = randint(1,2)                                                                                                                 # Entscheidet per Zufall, welcher Charakter dran ist.
        sleep(1)
        player_turn = 0
        monster_turn = 0
        out_of_action = None                                                                                                                # Variable für den evtl. Fehlschlag des SA des Akrobaten. Ist gesetzt um keinen Error hervorzurufen, sollte sein SA nicht schief gehen/genutzt werden.
        while len(monsterlist) > 0 and len(self.__current_group.get_heroes()) > 0:                                                          # Der Kampf läuft solange, bis eine der beiden Gruppen keine Kämpfer mehr enthält.
            if turn == 1:
                try:
                    move, target = self.fight_user_menu(player_turn, monsterlist)                                                           # Angriffstyp und Ziel werden mit separater Methode ausgewählt und übergeben.
                    if move == 1:
                        damage = self.__current_group.get_heroes()[player_turn].attack()                                                    # Damage wird vor der Berechnung in eine lokale Variable gespeichert.
                        if type(damage) is not int:                                                                                         # Geht die Probe für den Angriff schief, erscheint diese Fehlermeldung (Bool statt int wird übergeben).
                            print( "{}'s attack failed!".format(self.__current_group.get_heroes()[player_turn].get_name()))
                    elif move == 2 and self.__current_group.get_heroes()[player_turn].get_special_attack() == 0:                            # Sofern der Spezialangriff nicht vorige Runde ausgeführt wurde, kann er nun ausgeführt werden.
                        if self.__current_group.get_heroes()[player_turn].get_class_name() == "Knight":                                     # Jede Klasse besitzt einen eigenen Programmteil.
                            damage = self.__current_group.get_heroes()[player_turn].swordart()
                            if type(damage) is not int:
                                print("{} missed and hurt himself!\nHe/She lost 5 lifepoints.".format(
                                    self.__current_group.get_heroes()[player_turn].get_name()))
                        elif self.__current_group.get_heroes()[player_turn].get_class_name() == "Mage":
                            damage = self.__current_group.get_heroes()[player_turn].fireball()
                            if type(damage) is not int:
                                print("{} missed and hurt himself!\nHe/She has {} lifepoints left.".format(
                                    self.__current_group.get_heroes()[player_turn].get_name(),
                                    self.__current_group.get_heroes()[player_turn].get_intelligence()))
                        elif self.__current_group.get_heroes()[player_turn].get_class_name() == "Thief":
                            damage = self.__current_group.get_heroes()[player_turn].sneak_attack()
                            if type(damage) is not int:
                                print("{} missed and hurt himself!\nHe/She lost 5 lifepoints.".format(
                                    self.__current_group.get_heroes()[player_turn].get_name()))
                        elif self.__current_group.get_heroes()[player_turn].get_class_name() == "Acrobat":
                            damage = self.__current_group.get_heroes()[player_turn].assault()
                            if not damage:
                                print("{} fell and hurt himself greatly. He can't fight anymore.".format(
                                    self.__current_group.get_heroes()[player_turn].get_name()))
                                out_of_action = self.__current_group.get_heroes().pop(player_turn)                                          # Geht der Angriff des Akrobaten daneben, wird er aus der Spielergruppe entfernt und in einer lokalen Liste gespeichert.
                            else:
                                hit = randint(0, len(monsterlist))
                                print("{} hit and you've hit hard. A {} is killed instantly!".format(
                                    self.__current_group.get_heroes()[player_turn].get_name(), hit.get_name()))
                                monsterlist.remove(monsterlist.index(hit))
                                self.__current_group.get_heroes()[player_turn].get_weapon().durability_damage()
                    else:                                                                                                                   # Falls der Charakter seinen SA bereits ausgeführt hat, wird eine Meldung ausgegeben...
                        print("{} is exhausted, he can't use his special move.".format(self.__current_group.get_heroes()[player_turn].get_name()))
                        damage = False
                        player_turn -= 1                                                                                                    # ...und der Spieler am Zug zurückgesetzt...
                        turn -= 1                                                                                                           # ...sowie der Zug zurückgesetzt.
                    if type(damage) is int:                                                                                                 # Sind alle Bedingungen erfüllt, wird die Schadensberechnung über einer separaten Methode durchgeführt.
                        self.dmg_calc(monsterlist, target, damage, player_turn)
                    self.lifepoint_tester()
                    cont = input("Press anything to continue!\n")
                    turn += 1                                                                                                               # Die Variable für den Zug wird auf den Wert für die Gegenergruppe gestellt.
                    player_turn += 1                                                                                                        # Der nächste Spieler am Zug wird damit definiert.
                except IndexError:
                    player_turn = 0                                                                                                         # Falls ein Charakter gestorben ist und sein Index nicht mehr vorhanden ist, wiederholt sich die Schleife mit dem ersten Spieler der Liste.
            elif turn == 2:
                try:
                    target = randint(0, len(self.__current_group.get_heroes()) - 1)
                    damage = monsterlist[monster_turn].attack()
                    if monsterlist[monster_turn].attack() > self.__current_group.get_heroes()[target].get_strength():
                        print("A {} strikes!".format(monsterlist[monster_turn].get_name()))
                        self.__current_group.get_heroes()[target].set_lifepoints(self.__current_group.get_heroes()[target].
                                                                                 get_lifepoints()-damage)                                   # Berechnet den Schaden anders als beim Helden ohne weiterer Methode.
                        if self.__current_group.get_heroes()[target].get_lifepoints() > 0:
                            print("{} has {} lifepoints left!".format(self.__current_group.get_heroes()[target].get_name(),
                                                                      self.__current_group.get_heroes()[target].get_lifepoints()))
                        else:
                            self.lifepoint_tester()
                    else:
                        print("The {}s attack fails!".format(monsterlist[monster_turn].get_name()))
                    cont = input("Press anything to continue!\n")
                    turn -= 1
                    monster_turn += 1
                except IndexError:
                    monster_turn = 0
        if len(monsterlist) > 0:
            print("The monsters have won!")
        else:
            print("Your group won!")
        if out_of_action is not None:                                                                                                       # Sofern die Variable einen Wert enthält, wird der Charakter am Ende des Kampfes wieder in die Gruppe hinzugefügt.
            self.__current_group.append(out_of_action)
        for items in range(0, len(self.__current_group.get_heroes())):
            self.__current_group.get_heroes()[items].set_special_attack(0)                                                                  # Setzt den SA am Ende des Kampfes zurück, damit im nächsten Kampf wieder von vorne begonnen wird.

    def dmg_calc(self, monsterlist, target, damage, player_turn):
        """
        Methode, die den angerichteten Schaden vom Leben des Gegners abzieht und eine Meldung ausgibt.
        :param monsterlist: Liste, die die Monster des Gegnerteams enhält.
        :param target: Der Index des Ziels.
        :param damage: Der angerichtete Schaden.
        :param player_turn: Der Spieler, welcher am Zug ist.
        """
        print("{} strikes succesfully for {} damage!".format(self.__current_group.get_heroes()[player_turn].get_name(), damage))
        monsterlist[target].set_health(monsterlist[target].get_health() - damage)
        self.__current_group.get_heroes()[player_turn].get_weapon().durability_damage()
        if monsterlist[target].get_health() > 0:  # Falls das Monster nicht tot ist, werden die LP ausgegeben.
            print("The {} has {} lifepoints left!".format(monsterlist[target].get_name(), monsterlist[target].get_health()))
        else:  # Falls doch, wird eine Nachricht für dessen Tod ausgegeben.
            print("The {} died!\nYour group earned {} experience.".format(monsterlist[target].get_name(), monsterlist[target].get_experience()))
            self.__current_group.set_experience(self.__current_group.get_experience()+monsterlist[target].get_experience())
            del monsterlist[target]

    def fight_user_menu(self, player_turn, monsterlist):
        """
        Das Menü der Spieler während des Kampfes. Der Spieler kann einen Angriff und ein Ziel auswählen.
        :param player_turn: Der Index des Spielers, welcher am Zug ist.
        :param monsterlist: Liste, die die gegnerischen Monster im Kampf enthält.
        """
        user_loop = True
        while user_loop:
            try:
                print("{} is at turn!\n".format(self.__current_group.get_heroes()[player_turn].get_name()))
                move = int(input("What do you want to do?\n\n[1] Normal attack\n[2] Special attack\n\n> "))
                if self.__current_group.get_heroes()[player_turn].get_class_name() == "Acrobat" and move == 2:
                    user_loop = False
                else:
                    if move in range(1, 3):
                        print("\nWhich enemy to you want to attack?\n")
                        for items in range(0, len(monsterlist)):
                            print("[{}] {}".format(items + 1, monsterlist[items].get_name()))
                        target = int(input("\n> "))
                        if target in range(1, len(monsterlist) + 1):
                            user_loop = False
                            return move, target-1
                        else:
                            print("This enemy doesn't exist!")
                    else:
                        print("This option is not available!")
            except ValueError:
                print("Only Integer!")

    def playing_group(self, name):
        """
        Erstellt aus den ausgewählten Gruppennamen die Charakter-Objekte sowie das Objekt für die Heldengruppe und
        speichert diese unter der Klassenvariable für die spielende Gruppe. Da es unterschiedliche Heldenklassen gibt, wird durch eine
        separate Methode ein Objekt der spezifischen Klasse übergeben.
        :param name: Der Name der ausgewählten Gruppe.
        """
        chr_list, exp, lvl = self.find_group_members(name)
        hero_group = []
        weapon_list = []
        for items in range(0, len(self.__weapons)):
            wpn_name = self.__weapons[items].get_name()
            weapon_list.append(wpn_name)
        for items_a in range(0, len(chr_list)):                                                                                             # Wird so oft wiederholt wie es Charaktere in der gewünschten Gruppe gibt. Ermöglicht das Spielen mit weniger als 4 Charakteren.
            for items_b in range(0, len(self.__weapons)):
                if chr_list[items_a][10] == weapon_list[items_b]:
                    weapon_index = items
            character = self.playing_class(chr_list, items_a, weapon_index)
            hero_group.append(character)
        self.__current_group = CharacterGroup(name, int(exp), int(lvl),hero_group)                                                          # Erfahrung und Level werden mit den in der Datei gespeicherten Werten übergeben.

    def playing_class(self, chr_list, items, weapon_index):
        """
        Methode, die mit übergebenen Werten Objekte einer ausgewählten Heldenklasse erstellt.
        :param chr_list: Liste mit Charakteren, sowie deren Werte.
        :param items: Index des Helden, der als Objekt erstellt werden soll.
        :param weapon_index: Index der Waffe, die der Held besitzt.
        :return: class object (Knight or Mage or Thief or Acrobat)
        """
        if chr_list[items][1] == self.__classes[0]:
            return Knight(chr_list[items][0], int(chr_list[items][2]), int(chr_list[items][3]), int(chr_list[items][4]),
                          int(chr_list[items][5]), int(chr_list[items][6]), int(chr_list[items][7]),
                          int(chr_list[items][8]),
                          int(chr_list[items][9]), self.__weapons[weapon_index])
        elif chr_list[items][1] == self.__classes[1]:
            return Mage(chr_list[items][0], int(chr_list[items][2]), int(chr_list[items][3]), int(chr_list[items][4]),
                        int(chr_list[items][5]), int(chr_list[items][6]), int(chr_list[items][7]),
                        int(chr_list[items][8]),
                        int(chr_list[items][9]), self.__weapons[weapon_index])
        elif chr_list[items][1] == self.__classes[2]:
            return Thief(chr_list[items][0], int(chr_list[items][2]), int(chr_list[items][3]), int(chr_list[items][4]),
                         int(chr_list[items][5]), int(chr_list[items][6]), int(chr_list[items][7]),
                         int(chr_list[items][8]),
                         int(chr_list[items][9]), self.__weapons[weapon_index])
        elif chr_list[items][1] == self.__classes[3]:
            return Acrobat(chr_list[items][0], int(chr_list[items][2]), int(chr_list[items][3]),
                           int(chr_list[items][4]),
                           int(chr_list[items][5]), int(chr_list[items][6]), int(chr_list[items][7]),
                           int(chr_list[items][8]),
                           int(chr_list[items][9]), self.__weapons[weapon_index])

    def list_playing_characters(self):
        """
        Methode, welcher die Werte der Charaktere der spielenden Heldengruppe übergibt.
        :return: characters
        """
        characters = []
        for items_a in range(0, len(self.__current_group.get_heroes())):
            values = []
            for items_b in range(0, 11):
                values.append(self.__current_group.get_heroes()[items_a].get_name())
                values.append(self.__current_group.get_heroes()[items_a].get_class_name())
                values.append(self.__current_group.get_heroes()[items_a].get_lifepoints())
                values.append(self.__current_group.get_heroes()[items_a].get_strength())
                values.append(self.__current_group.get_heroes()[items_a].get_dexterity())
                values.append(self.__current_group.get_heroes()[items_a].get_intelligence())
                values.append(self.__current_group.get_heroes()[items_a].get_sleight_of_hand())
                values.append(self.__current_group.get_heroes()[items_a].get_charisma())
                values.append(self.__current_group.get_heroes()[items_a].get_stamina())
                values.append(self.__current_group.get_heroes()[items_a].get_intuition())
                values.append(self.__current_group.get_heroes()[items_a].get_weapon().get_name())
            characters.append(values)
        return characters

    def gameplay(self):
        """
        Die Methode, die den Spielverlauf regelt.
        """
        game_loop = True
        group_loop = True
        group_list = self.find_group_name()
        if len(group_list) > 0:
            while group_loop:                                                                                                               # While-Schleife die die Gruppenauswahl inkl. Fehlerabfang regelt.
                print("\n"+SEPERATOR+"\n")
                try:
                    for items in range(0, len(group_list)):
                        print("[{}] Name: {}".format(str(items), group_list[items]))
                    grp_input = input("\nWith what group do you want to play? (Write the ID)\n[x] to leave\n> ")
                    if grp_input == "x" or grp_input == "X":
                        group_loop = False
                        game_loop = False
                    elif int(grp_input) in range(0, len(group_list)):
                        self.create_weapons()                                                                                               # Beginnt das Spiel, werden die Waffen als Objekte erschaffen.
                        self.create_monsters()                                                                                              # Ebenso die Monster.
                        grp_input = int(grp_input)                                                                                          # Wandelt den Input in einen Integer um, sofern eine existierende Gruppe ausgewählt wurde.
                        group_loop = False
                    else:
                        print("\nThis group doesn't exist!")
                except ValueError:
                    print("\nOnly (full) numbers!")
            if type(grp_input) == int:
                self.playing_group(group_list[grp_input])                                                                                   # Erstellt die Spielergruppe mithilfe der playing_group-Methode
                if self.__current_group.get_experience() == 0:                                                                              # Sofern die Spielergruppe neu ist, wird jedem Helden eine zufällige Waffe gegeben.
                    for items in range(0, len(self.__current_group.get_heroes())):
                        self.__current_group.get_heroes()[items].set_weapon(self.__weapons[randint(0, len(self.__weapons))-2])
                print("\n"+"Your adventure begins here...".center(len(SEPERATOR))+"\n"+"\n"+SEPERATOR)
                sleep(1)
                map.map_creation()                                                                                                          # Die Spielkarte wird erschaffen.
                while len(self.__current_group.get_heroes()) > 0 and game_loop:                                                             # Das Spiel läuft solange, wie es Helden in der Gruppe gibt oder die Variable verändert wird.
                    test = True                                                                                                             # Setzt test zu Beginn jeder Runde wieder auf true
                    cont = None                                                                                                             # Um eine Bedingung vor der eigentlichen Deklarierung zu stellen, wird cont auf None gesetzt
                    while test is True:                                                                                                     # Wiederholt sich solange, bis ein neues Feld betreten wurde.
                        test = map.movement()                                                                                               # Methode die die Bewegung durch die Karte enthält.
                    if test is False:                                                                                                       # Sollte die Gruppe das Ende erreichen, wird die Schleife für das Spiel unterbrochen.
                        game_loop = False
                        cont = "x"                                                                                                          # cont wird auf "x" gesetzt, damit die Charaktere noch gespeichert werden.
                    chr_id = randint(0,len(self.__current_group.get_heroes())-1)                                                            # Ein zufälliger Charakter wird für die nächste Runde ausgewählt.
                    self.test(chr_id, test)                                                                                                 # Läuft in die Methode für den Test.
                    self.lifepoint_tester()                                                                                                 # Kontrolliert nach jeder Probe die LP des Charakters.
                    if len(self.__current_group.get_heroes()) > 0:
                        self.__current_group.level_check()                                                                                  # Kontrolliert nach jeder Probe das Level der Gruppe.
                        if cont is not "x":                                                                                                 # Die Bedingung wird nur bei erreichen des Ende der Karte übersprungen.
                            cont = input("\n[x] Stop the game (Progress will be saved!)\n[l] look into your group\n[anything] Continue\n> ")
                        print("\n"+SEPERATOR)
                        if cont == "x" or cont == "X":
                            with open(os.path.join("characterfiles",self.__current_group.get_name()+".txt"), "w") as group_file:            # Die .txt-Datei der Gruppe wird überschrieben.
                                for items in range(0, len(self.__current_group.get_heroes())):                                              # Es wird mit dem __current_group-Attribut gearbeitet, damit sichergestellt ist, dass die neuen Werte übernommen werden.
                                    group_file.write(self.__current_group.get_heroes()[items].get_name() + "\n" +
                                                     str(self.__current_group.get_heroes()[items].get_class_name()) + "\n" +
                                                     str(self.__current_group.get_heroes()[items].get_lifepoints()) + "\n" +
                                                     str(self.__current_group.get_heroes()[items].get_strength()) + "\n" +
                                                     str(self.__current_group.get_heroes()[items].get_dexterity()) + "\n" +
                                                     str(self.__current_group.get_heroes()[items].get_intelligence()) + "\n" +
                                                     str(self.__current_group.get_heroes()[items].get_sleight_of_hand()) + "\n" +
                                                     str(self.__current_group.get_heroes()[items].get_charisma()) + "\n" +
                                                     str(self.__current_group.get_heroes()[items].get_stamina()) + "\n" +
                                                     str(self.__current_group.get_heroes()[items].get_intuition()) + "\n" +
                                                     self.__current_group.get_heroes()[items].get_weapon().get_name() + "\n")
                                group_file.write(str(self.__current_group.get_experience())+"\n")
                                group_file.write(str(self.__current_group.get_level()))
                                group_file.close()
                            game_loop = False
                        if cont == "l" or cont == "L":                                                                                      # Hier werden die Charaktere sowie Gruppen-EP und Level ausgegeben, wählt man den Punkt im Spielmenü.
                            characters = self.list_playing_characters()
                            for items in range(0, len(self.__current_group.get_heroes())):
                                self.print_characters(characters, items)
                            print("\nLevel: {}".format(self.__current_group.get_level()))
                            print("Experience: {}\n".format(self.__current_group.get_experience()))
                            cont = input("Press anything to continue")
                if len(self.__current_group.get_heroes()) == 0:                                                                             # Ist jedes Mitglied der Gruppe gestorben, wird die .txt-Datei der Gruppe gelöscht.
                    os.remove(self.__current_group.get_name() + ".txt")
                    self.__current_group = None
                    print("\nYour party died. Their adventure ends here...")
                    sleep(3)
            else:
                pass
        else:
            print("You need a group!")


def menu():
    """
    Funktion für das Spielemenue.
    """
    menu_loop = True
    while menu_loop:
        try:
            print("\n"+"Rivers of Time".center(len(SEPERATOR), " ")+"\n\n"+SEPERATOR)
            menu_inp = int(input("\n[1] Create a character\n[2] Create a group of adventurers\n[3] Show characters"
                                 "\n[4] Show adventurer groups\n[5] Play\n[6] End Game\n\n> "))
        except ValueError:                                                                                                                  # Das Exception-Handling ist vor den if-Abfragen gesetzt, damit es nicht durch die einzelnen Methoden mitläuft.
            print("Only (full) numbers!")
            menu_inp = None
        if menu_inp == 1:
            game.create_character()
        elif menu_inp == 2:
            game.create_group()
        elif menu_inp == 3:
            game.characters_menu()
        elif menu_inp == 4:
            game.groups_menu()
        elif menu_inp == 5:
            game.gameplay()
        elif menu_inp == 6:
            print("\nUntil next time.")
            sleep(1)
            menu_loop = False


if __name__ == '__main__':

    try:
        os.makedirs("characterfiles")
    except FileExistsError:
        pass
    map = Map()                                                                                                                             # Objekt der Map-Klasse wird erstellt.
    game = Game()                                                                                                                           # Objekt der Game-Klasse wird erstellt.
    menu()