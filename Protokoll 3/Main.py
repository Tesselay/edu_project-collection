#!/usr/bin/env python
__author__ = "Dominique Lahl"
__copyright__ = "Copyright 2018, Dominique Lahl"
__version__ = "1.0.0"
__maintainer__ = "Dominique Lahl"
__email__ = "domee.lahl@gmail.com"
__status__ = "Development"

# Die benötigten Module/.py-Dateien werden importiert.
from random import randint
from time import sleep
import Character
import Weapon
import Monster
import CharacterGroup
import os

# Wichtige Variablen werden global gesetzt.
SEPERATOR = "-" * 50                                                                                                    # Trenner für versch. Menüpunkte, dient lediglich dem Design.


class Game:
    """
    Klasse die das Spiel samt seiner Funktionen enthält.
    """

    def __init__(self):
        """
        Der Konstruktor, welcher die Instanzen mit den gewünschten Werten erstellt.
        Kein Wert wird übergeben, es existiert eine Variable, die das Objekt der Heldengruppe enthalten wird, welche
        für das Spiel ausgewählt wird.
        """
        self.__current_group = None

    def create_character(self):
        """
        Diese Methode erstellt einen Charakter mit zufälligen Attributswerten und einer festgelegten Waffe. Der Name ist
        vom Spieler wählbar. Der Charakter wird dabei in eine Textdatei geschrieben.
        """
        print("\n"+SEPERATOR+"\n")
        name = input("What should your characters name be?\n> ")
        with open("characters.txt", "a") as character_file:                                                             # characters.txt wird für hinzufügen (append) geöffnet oder erstellt, falls nicht vorhanden.
            character_file.write(name+"\n"+str(30)+"\n"+str(randint(8,16))+"\n"+str(randint(8,16))+"\n"+                # Die Attribute werden als eine Zufallszahl zwischen 8 und 16 in die Datei geschrieben.
                                 str(randint(8, 16))+"\n"+str(randint(8,16))+"\n"+"Empty Hand\nX\n")                    # Die Standardwaffe wird lediglich mit ihrem Namen in die Datei geschrieben.
        character_file.close()                                                                                          # Zum Schluss wird ein X hinzugefügt um Charaktere leichter zu finden und deren Anzahl leichter zu entnehmen.

    def find_characters(self):
        """
        Ließt die Charaktere aus der .txt-Datei aus und speichert sie, samt Attributswerten und Waffenname, in einer
        Liste, welche dann zurückgegeben wird.
        :return: character_list
        """
        character_list = []
        with open("characters.txt", "r") as character_file:                                                             # Öffnet characters.txt zum lesen (read).
            chr_count = character_file.read().count("X")                                                                # Zählt, wie oft ein X in der Datei vorkommt und wie viele Charaktere es daher gibt.
            character_file.seek(0)                                                                                      # Springt zu Zeile 0 bzw. dem Beginn der Datei, um von dort wieder anzufangen.
            for items_a in range(0, chr_count):
                list = []                                                                                               # Erstellt eine temporäre Liste, die dem Speichern der Werte eines Charakters dient.
                for items_b in range(0, 7):
                    list.append(character_file.readline().rstrip("\n"))                                                 # Fügt der temporären Liste den Wert einer Zeile hinzu. Entfernt dabei \n, da dies sonst in ebenfalls mit dem Wert gespeichert wird.
                character_list.append(list)                                                                             # Fügt die temporäre Liste der Charakterliste hinzu.
                character_file.readline()                                                                               # Ließt eine Zeile aus. Dient dazu das X am Ende des Charakters zu überspringen.
        return character_list

    def delete_character(self, id, list):
        """
        Methode zum löschen eines Charakters.
        :param id: Die ID bzw. der Index, an welcher Stelle sich der Charakter innerhalb der Liste befindet.
        :param list: Die Liste, die den zu löschenden Charakter enthält.
        """
        character_list = list
        character_list.remove(character_list[id])                                                                       # Entfernt den Charakter an der Stelle der ausgewählten ID.
        with open("characters.txt", "w") as character_file:                                                             # Öffnet die characters.txt-Datei und überschreibt diese. Dabei werden alle Charaktere außer dem entfernten in die Datei geschrieben.
            for items in range(0, len(character_list)):
                character_file.write(character_list[items][0] + "\n" + character_list[items][1] + "\n" +
                                     character_list[items][2] + "\n" + character_list[items][3] + "\n" +
                                     character_list[items][4] + "\n" + character_list[items][5] + "\n" +
                                     character_list[items][6] + "\nX\n")
        character_file.close()

    def print_characters(self, chr_list):
        """
        Methode, welche die mit einer Liste übergebenen Charaktere samt ihrer Werte ausgibt.
        :param chr_list: Liste mit Charakteren.
        """
        character_list = chr_list
        for items in range(0, len(character_list)):
            print("\n[{}]\nName: {}\nLifepoints: {}\nStrength: {}\nDexterity: {}\nIntelligence: {}"
                  "\nSleight of hand: {}\nWeapon"
                  ": {}\n".format(str(items),
                                  character_list[items][0], character_list[items][1],
                                  character_list[items][2], character_list[items][3],
                                  character_list[items][4], character_list[items][5],
                                  character_list[items][6],
                                  ))
            cont = input("Press anything to continue!")

    def characters_menu(self):
        """
        Das Charaktermenü. Gibt die Charaktere aus und ermöglicht, einen Charakter zu löschen.
        """
        character_list = self.find_characters()                                                                         # Ließt die Charakterliste aus der get_characters-Methode in eine lokale Liste ein.
        chr_menu_loop = True
        print("\n" + SEPERATOR)
        while chr_menu_loop and len(character_list) > 0:
            print()
            menu_input = str(input(
                "Do you want to look into or delete a character?\n[l] look into a character"                            # Der Spieler kann eine ID auswählen und somit einen Charakter löschen oder das Charaktermenü verlassen.
                "\n[d] delete a character\n[x] leave\n\n> "))
            possible_inputs = ["x", "X", "d", "D", "l", "L"]                                                            # Liste mit den möglichen Inputs. Als Liste definiert um simpel Groß- und Kleinschreibung bei der Eingabe zu ermöglichen
            if menu_input in possible_inputs:
                if menu_input == "x" or menu_input == "X":                                                              # Als alleinstehende if-Abfrage gesetzt um danach einen input zu verlangen der für die beiden anderen Möglichkeiten wichtig ist.
                    break
                else:
                    try:
                        for items in range(0, len(character_list)):
                            print("[{}] Name: {}".format(str(items), character_list[items][0]))
                        chr_input = int(input("\nWhat character? (Write the ID)\n(Write anything else to get back)\n> "))
                        if chr_input in range(0, len(character_list)):
                            if menu_input == "d" or menu_input == "D":
                                self.delete_character(chr_input,character_list)                                         # Methode zum löschen eines Charakters. Übergibt die ausgewählte ID und die Charakterliste, in welcher sich dieser befindet.
                            elif menu_input == "l" or menu_input == "L":
                                print("\nName: {}\nLifepoints: {}\nStrength: {}\nDexterity: {}\nIntelligence: {}"
                                      "\nSleight of hand: {}\nWeapon"
                                      ": {}\n".format(character_list[items][0], character_list[items][1],
                                                      character_list[items][2], character_list[items][3],
                                                      character_list[items][4], character_list[items][5],
                                                      character_list[items][6],
                                                      ))
                        else:
                            print("This character doesn't exist!")
                    except ValueError:
                        print("Only (full) numbers.")
            else:
                print("You can only choose the given options.")
        if len(character_list) <= 0:
            print("There are no characters.")

    def create_group(self):
        """
        Diese Methode lässt den Spieler eine Gruppe aus den vorhandenen Charakteren erstellen und speichert die Gruppe
        in eine .txt-Datei mit dem Namen der Gruppe.
        """
        character_list = self.find_characters()                                                                         # Ließt die vorhandenen Charaktere in eine liste ein.
        if len(character_list) < 4:
            print("You need more heroes!")
        else:
            cg_loop = True
            print("\n"+SEPERATOR)
            while True:
                group_name = str(input("\nWhat should your group be called?\n[x] leave\n> "))
                if len(group_name) == 0:                                                                                # Es sind einige Bedingungen bezüglich des Namen gestellt.
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
                with open(group_name+".txt", "w") as group_file:                                                        # Eine Textdatei, welche die Helden enthält, wird mit dem Namen der Gruppe erstellt.
                    error_catch = 4                                                                                     # Die Wiederholungen der folgenden For-Schleife. Dient dem sicher gehen eines korrekten Ablaufs in Falle eines Fehlers.
                    while error_catch > 0:                                                                              # Eine while-, statt eine for-Schleife wird genutzt, da die übergebenen Werte für die range-Funktion nicht dynamisch sind.
                        try:
                            print()
                            for items in range(0, len(character_list)):                                                 # Zur besseren Übersicht, werden die Namen der Charaktere bei jeder Auswahl ausgegeben.
                                print("[{}] Name: {}".format(str(items), character_list[items][0]))
                            hero_input = int(input("\nWhich hero should be part of your endeavour?\n"
                                                   "(Write his/her ID)\n> "))
                            if hero_input > len(character_list):
                                print("\nThis character doesn't exist!")
                            else:
                                group_file.write(character_list[hero_input][0]+"\n"+character_list[hero_input][1]+"\n"+ # Ähnlich der .txt-Datei für Charaktere, werden die Werte der Charaktere in die Gruppendatei geschrieben.
                                                 character_list[hero_input][2]+"\n"+character_list[hero_input][3]+"\n"+
                                                 character_list[hero_input][4]+"\n"+character_list[hero_input][5]+"\n"+
                                                 character_list[hero_input][6]+"\n")
                                self.delete_character(hero_input, character_list)
                                error_catch -= 1
                        except ValueError:
                            print("\nOnly (full) numbers!")
                    group_file.write("0\n")                                                                             # Schreibt die Erfahrungspunkte der Gruppe in die Datei.
                    group_file.write("0")                                                                               # Schreibt das Level der Gruppe in die Datei.
                    group_file.close()
                    cg_loop = False

    def find_group_name(self):
        """
        Speichert die Namen der Gruppen in eine Liste und gibt diese aus.
        :return: group_list
        """
        group_list = []
        for file in os.listdir(os.getcwd()):                                                                            # Für jede Datei in dem Verzeichnis der .py-Datei, wird die For-Schleife durchlaufen.
            if file.endswith(".txt"):
                group_list.append(os.path.splitext(file)[0])                                                            # Die Dateiennamen werden ohne dem Datentyp-Indikator in die Liste hinzugefügt.
        group_list.remove("characters")                                                                                 # Die characters(.txt)-Datei wird aus der Liste entfernt.
        return group_list

    def find_group_members(self, name):
        """
        Speichert die Charaktere einer Gruppe samt den zugehörigen Werten in eine Liste und gibt diese aus. Kann dies
        auch für Gruppen tun, die weniger als 4 Mitglieder enthält.
        :param name: Übergibt den Namen der gewünschten Gruppe.
        :return: character_list
        """
        character_list = []
        with open(name+".txt", "r") as group_file:
            for counter, value in enumerate(group_file):                                                                # Zählt die Zeilen innerhalb der geöffneten Datei. Jeder Charakter entspricht genau 7 Zeilen,
                pass                                                                                                    # damit können die Charaktere innerhalb der Datei einfach gezählt werden.
            counter -= 1                                                                                                # Der Wert wird um 1 verringert, da die erste gezählte Zeile dem Wert 0 entspricht und am Ende der Datei zwei Zeilen für EP und Level stehen.
            counter = counter / 7                                                                                       # Wird durch 7 gerechnet um auf die Charakteranzahl zu kommen.
            group_file.seek(0)
            for items_a in range(0, int(counter)):
                list = []
                for items_b in range(0, 7):
                    list.append(group_file.readline().rstrip("\n"))
                character_list.append(list)
            experience = group_file.readline().rstrip("\n")                                                             # Die vorletze Zeile (Erfahrungspunkte der Gruppe) wird in eine Variable eingelesen.
            level = group_file.readline()                                                                               # Die letzte Zeile (Level der Gruppe) wird in eine Variable eingelesen.
            group_file.close()
        return character_list, experience, level

    def groups_menu(self):
        """
        Stellt das Menü für das Gruppenmanagement da. Ermöglicht die einzelnen Charaktere auszugeben und Gruppen zu
        löschen.
        """
        group_list = self.find_group_name()                                                                             # Namen der Gruppen werden in eine Liste eingelesen.
        grp_menu_loop = True
        if len(group_list) > 0:
            while grp_menu_loop:
                print("\n"+SEPERATOR+"\n")

                menu_input = str(input("Do you want to look into or delete a group?\n[l] look into a group"
                                       "\n[d] delete a group\n[x] leave\n\n> "))
                possible_inputs = ["x", "X", "d", "D", "l", "L"]                                                        # Liste mit den möglichen Inputs. Als Liste definiert um simpel Groß- und Kleinschreibung bei der Eingabe zu ermöglichen
                if menu_input in possible_inputs:
                    try:                                                                                                # Exception-Handling, da eine Eingabe in Integer umgewandelt wird.
                        if menu_input == "x" or menu_input == "X":                                                      # Die Eingabe für das Verlassen der Menü wird separat als erstes abgefangen, um einfacher mit den anderen Eingaben zu arbeiten.
                            break
                        for items in range(0, len(group_list)):
                            print("[{}] Name: {}".format(str(items), group_list[items]))
                        grp_input = int(input("\nWhich group? (Write the ID)\n(Write anything else to get back)\n> "))  # Die Eingabe für die ID,...
                        if grp_input <= len(group_list):
                            grp_list = self.find_group_name()                                                           # ...das speichern der Gruppennamen in eine lokale Liste...
                            chr_list, exp, level = self.find_group_members(grp_list[grp_input])                         # ... und das speichern der Charakterwerte etc werden vor den beiden anderen Auswahlmöglichkeiten ausgeführt, da beide Werte davon benötigen.
                            if menu_input == "l" or menu_input == "L":
                                self.print_characters(chr_list)
                                print("\nExperience: {}".format(str(exp)))
                                print("Level: {}".format(str(level)))
                            elif menu_input == "d" or menu_input == "D":
                                with open("characters.txt", "a") as character_file:                                     # Wird die Gruppe gelöscht, werden alle noch lebenden Charaktere wieder zur Auswahl in die characters.txt-Datei geschrieben.
                                    for items in range(0, len(chr_list)):
                                        character_file.write(chr_list[items][0] + "\n" + chr_list[items][1] + "\n" +
                                                             chr_list[items][2] + "\n" + chr_list[items][3] + "\n" +
                                                             chr_list[items][4] + "\n" + chr_list[items][5] + "\n" +
                                                             chr_list[items][6] + "\nX\n")
                                os.remove(str(grp_list[grp_input])+".txt")
                        else:
                            print("\nThis group doesn't exist!")
                    except ValueError:
                        print("\nOnly (full) numbers!")
                else:
                    print("You can only choose the given options.")
        else:
            print("There are no groups!")

    def test(self, chr_id):
        """
        Methode die die den Proben zugehörigen Werteveränderungen und die Kampf-Funktion für die Kampf-Probe enthält.
        :param chr_id: Der Index des Charakters, welcher getestet wird..
        """
        current_test = randint(1, 4)
        if current_test == 1:
            # Kampfprobe
            self.fight(chr_id)
        elif current_test == 2:
            # Fingerfertigkeitsprobe
            print("Your party finds an incautious traveller. {} gets carefully closer..."
                  .format(self.__current_group.get_heroes()[chr_id].get_name()))                                        # Die Funktion für das erhalten des Namen des Heldenobjekt innerhalb der spielenden Gruppe (Gruppenobjekt) wird direkt angesprochen.
            sleep(1)
            if self.__current_group.get_heroes()[chr_id].pickpocket() == True:
                self.__current_group.set_experience(self.__current_group.get_experience() + 10)
                print(self.__current_group.get_heroes()[chr_id].get_name() +
                      " was succesful! Your group earned 10 Experience.")
            else:
                print(self.__current_group.get_heroes()[chr_id].get_name() +
                      " failed! Nothing special happened.")
        elif current_test == 3:
            # Intelligenzprobe
            print("Your party encounters an unknown event. {} wonders what it could be..."
                  .format(self.__current_group.get_heroes()[chr_id].get_name()))
            sleep(1)
            if self.__current_group.get_heroes()[chr_id].wonder() == True:
                bonus_exp = self.__current_group.get_heroes()[chr_id].get_intelligence() * 2
                self.__current_group.set_experience(self.__current_group.get_experience()+bonus_exp)
                print(self.__current_group.get_heroes()[chr_id].get_name() +
                      " won new knowledge! Your group earned {} experience."
                      .format(bonus_exp))
            else:
                print(self.__current_group.get_heroes()[chr_id].get_name() +
                      " didn't think about something interesting.")
        elif current_test == 4:
            # Geschicklichskeitsprobe
            print("{} has to cross a dangerous river...".format(self.__current_group.get_heroes()[chr_id].get_name()))
            sleep(1)
            if self.__current_group.get_heroes()[chr_id].balance() == True:
                self.__current_group.set_experience(self.__current_group.get_experience() + 2)
                print(self.__current_group.get_heroes()[chr_id].get_name() +
                      " was succesful! Your group earned 2 Experience.")
            else:
                self.__current_group.get_heroes()[chr_id].set_lifepoints(self.__current_group.get_heroes()
                                                                         [chr_id].get_lifepoints() - 10)
                print(self.__current_group.get_heroes()[chr_id].get_name() +
                      " fell! She/He lost 10 lifepoints.")

    def lifepoint_tester(self):
        """
        Testet die Lebenspunkte der Charaktere der Spielgruppe und entfernt einen Charakter, sollten seine unter 0
        fallen.
        :param chr_id: Die ID des zu testenden Charakters wird übergeben.
        """
        for items in range(0, len(self.__current_group.get_heroes())):
            if self.__current_group.get_heroes()[items].get_lifepoints() <= 0:
                print(self.__current_group.get_heroes()[items].get_name() + " died!")
                self.__current_group.get_heroes().remove(self.__current_group.get_heroes()[items])                      # Mithilfe der .remove-Funktion wird der gestorbene Charakter direkt aus der Heldengruppe entfernt.
            else:
                pass

    def find_weapon(self, name):
        """
        Enthält die Waffen sowie deren zugehörigen Werte und kreirt aus ihnen Objekte der Klasse Waffe.
        :param name: Name der Waffe, welche benötigt wird/erstellt werden soll.
        :return: weapon
        """
        weapons_list = ["Axe", "Lance", "Wooden Sword", "Empty Hand"]                                                   # Empty Hand befindet sich in dieser Liste, um dem in die Textdatei geschriebenen Namen Werte zuordnen zu können.
        weapon_dmg = [7, 11, 2, 1]
        weapon_dur = [90, 120, 50, 0]                                                                                   # Der Haltbarkeitswert der Waffen.
        for items in range(0, len(weapons_list)):
            if name == weapons_list[items]:
                weapon = Weapon.Weapon(weapons_list[items], weapon_dmg[items], weapon_dur[items])
                return weapon

    def weapon_decider(self):
        """
        Sucht eine zufällige Waffe aus und gibt diese als Objekt zurück.
        :return: weapon
        """
        rand_weapon = randint(1,3)                                                                                      # Um einen Charakter nicht Empty Hand zu übergeben, stehen hier nur die drei anderen Waffen zur Auswahl.
        if rand_weapon == 1:
            weapon = self.find_weapon("Axe")
            return weapon
        elif rand_weapon == 2:
            weapon = self.find_weapon("Lance")
            return weapon
        elif rand_weapon == 3:
            weapon = self.find_weapon("Wooden Sword")
            return weapon

    def playing_group(self, name):
        """
        Erstellt aus den ausgewählten Gruppennamen die Charakter-Objekte sowie das Objekt für die Heldengruppe und
        speichert diese unter der Klassenvariable für die spielende Gruppe.
        :param name: Der Name der ausgewählten Gruppe.
        """
        chr_list, exp, lvl = self.find_group_members(name)
        hero_group = []
        for items in range(0, len(chr_list)):                                                                           # Wird so oft wiederholt wie es Charaktere in der gewünschten Gruppe gibt. Ermöglicht das Spielen mit weniger als 4 Charakteren.
            weapon = self.find_weapon(chr_list[items][6])
            character = Character.Character(chr_list[items][0], int(chr_list[items][1]), int(chr_list[items][2]),
                                  int(chr_list[items][3]),int(chr_list[items][4]), int(chr_list[items][5]), weapon)
            hero_group.append(character)
        self.__current_group = CharacterGroup.CharacterGroup(name, int(exp), int(lvl), hero_group)                      # Erfahrung und Level werden mit den in der Datei gespeicherten Werten übergeben.

    def monsters(self):
        """
        Enthält die Monster sowie deren zugehörigen Werte und erstellt aus Ihnen Objekte der Klasse Monster, welche in
        eine Liste gespeichert und übergeben werden.
        :return: monster_list
        """
        monster_list = []
        monster_names = ["Dire Wolf", "Treant", "Wraith"]
        monster_health = [15, 20, 8]
        monster_min_dmg = [4, 1, 8]
        monster_attribute = [16, 20, 8]
        for items in range(0, len(monster_names)):
            monster = Monster.Monster(monster_names[items], monster_health[items], monster_min_dmg[items], monster_attribute[items])
            monster_list.append(monster)
        return monster_list

    def fight(self, chr_id):
        """
        Methode für den Kampf, lässt im Falle der Kampfprobe den Spieler gegen einen zufällig ausgewähtles Monster
        kämpfen.
        :param chr_id: Der Index des Charakters innerhalb der Charakterlist, welcher kämpft.
        """
        fight_loop = True
        monster = self.monsters()[randint(0, len(self.monsters())-1)]                                                   # Wählt ein zufälliges Monster aus und speichert es lokal als Instanz.
        decider = randint(1,2)                                                                                          # Entscheidet per Zufall, welcher Charakter dran ist.
        print("\nA {} crosses your way, you're forced to fight.\n".format(monster.get_name()))
        sleep(1)
        while fight_loop:                                                                                               # Der Kampf läuft solange, bis einer der beiden Kontrahenten keine Lebenspunkte mehr besitzt.
            if decider == 1:
                if self.__current_group.get_heroes()[chr_id].attack() == True:                                          # Nur wenn die Kampfprobe positiv ausfällt, greift der Charakter an.
                    print(self.__current_group.get_heroes()[chr_id].get_name()+" strikes!")
                    monster.set_health(monster.get_health()-randint(1,6)-self.__current_group.get_heroes()[chr_id].
                                       get_weapon().get_damage())                                                       # Settet die LP des Monsters neu und übergibt dafür die "gegetteten" LP - Zufallszahl zwischen 1 und 6 und - Waffenschaden des Helden.
                    if monster.get_health() > 0:                                                                        # Falls das Monster nicht tot ist, werden die LP ausgegeben.
                        print("The monster has {} lifepoints left!".format(monster.get_health()))
                    else:                                                                                               # Falls doch, wird eine Nachricht für dessen Tod ausgegeben.
                        print("The monster died!")
                        fight_loop = False
                    self.__current_group.get_heroes()[chr_id].get_weapon().durability_damage()                          # Nach jedem Treffer verliert die Waffe durch die zugehörige Methde Haltbarkeit.
                else:
                    print("Your attack failed!")
                cont = input("Press anything to continue!\n")
                decider = 2                                                                                             # Setzt die Entscheider-Variable auf den Wert für den Kontrahenten.
            elif decider == 2:
                if monster.attack() == True:
                    print("The monster strikes!")
                    self.__current_group.get_heroes()[chr_id].set_lifepoints(self.__current_group.get_heroes()[chr_id].
                                                                             get_lifepoints()-monster.dmg_done())
                    if self.__current_group.get_heroes()[chr_id].get_lifepoints() > 0:
                        print("You have {} lifepoints left!".format(self.__current_group.get_heroes()[chr_id].
                                                                    get_lifepoints()))
                    else:
                        self.lifepoint_tester()
                        fight_loop = False
                else:
                    print("The monsters attack fails!")
                cont = input("Press anything to continue!\n")
                decider = 1
        if monster.get_health() > 0:
            print("The monster has won!")
        else:
            print("You've won!")

    def gameplay(self):
        """
        Die Methode, die den Spielverlauf regelt.
        """
        game_loop = True
        group_loop = True
        group_list = self.find_group_name()
        if len(group_list) > 0:
            while group_loop:                                                                                           # While-Schleife die die Gruppenauswahl inkl. Fehlerabfang regelt.
                print("\n"+SEPERATOR+"\n")
                try:
                    for items in range(0, len(group_list)):
                        print("[{}] Name: {}".format(str(items), group_list[items]))
                    grp_input = input("\nWith what group do you want to play? (Write the ID)\n[x] to leave\n> ")
                    if grp_input == "x" or grp_input == "X":
                        group_loop = False
                        game_loop = False
                    elif int(grp_input) in range(0, len(group_list)):
                        grp_input = int(grp_input)                                                                      # Wandelt den Input in einen Integer um, sofern eine existierende Gruppe ausgewählt wurde.
                        group_loop = False
                    else:
                        print("\nThis group doesn't exist!")
                except ValueError:
                    print("\nOnly (full) numbers!")
            if type(grp_input) == int:
                self.playing_group(group_list[grp_input])                                                               # Erstellt die Spielergruppe mithilfe der playing_group-Methode
                if self.__current_group.get_experience() == 0:                                                          # Sofern die Spielergruppe neu ist, wird jedem Helden eine zufällige Waffe gegeben.
                    for items in range(0, len(self.__current_group.get_heroes())):
                        self.__current_group.get_heroes()[items].set_weapon(self.weapon_decider())
                print("\n"+"Your adventure begins here...".center(len(SEPERATOR))+"\n"+"\n"+SEPERATOR)
                sleep(1)
                while len(self.__current_group.get_heroes()) > 0 and game_loop:                                         # Das Spiel läuft solange, wie es Helden in der Gruppe gibt oder...
                    chr_id = randint(0,len(self.__current_group.get_heroes())-1)                                        # Ein zufälliger Charakter wird für die nächste Runde ausgewählt.
                    print("\n"+self.__current_group.get_heroes()[chr_id].get_name(),"is at turn!")
                    self.test(chr_id)                                                                                   # Läuft in die Methode für den Test.
                    self.lifepoint_tester()                                                                             # Kontrolliert nach jeder Probe die LP des Charakters.
                    self.__current_group.level_check()                                                                  # Kontrolliert nach jeder Probe das Level der Gruppe.
                    cont = input("\n[x] Stop the game (Progress will be saved!)\n[anything] Continue\n> ")
                    print("\n"+SEPERATOR)
                    if cont == "x" or cont == "X":                                                                      # ... bis der Spieler das Spiel abbricht.
                        with open(self.__current_group.get_name() + ".txt", "w") as group_file:                                 # Die .txt-Datei der Gruppe wird überschrieben.
                            for items in range(0, len(self.__current_group.get_heroes())):                                      # Es wird mit dem __current_group-Attribut gearbeitet, damit sichergestellt ist, dass die neuen Werte übernommen werden.
                                group_file.write(self.__current_group.get_heroes()[items].get_name() + "\n" +
                                                 str(self.__current_group.get_heroes()[items].get_lifepoints()) + "\n" +
                                                 str(self.__current_group.get_heroes()[items].get_strength()) + "\n" +
                                                 str(self.__current_group.get_heroes()[items].get_dexterity()) + "\n" +
                                                 str(self.__current_group.get_heroes()[items].get_intelligence()) + "\n" +
                                                 str(self.__current_group.get_heroes()[items].get_sleight_of_hand()) + "\n" +
                                                 self.__current_group.get_heroes()[items].get_weapon().get_name() + "\n")
                            group_file.write(str(self.__current_group.get_experience())+"\n")
                            group_file.write(str(self.__current_group.get_level()))
                            group_file.close()
                        game_loop = False
                if len(self.__current_group.get_heroes()) == 0:                                                         # Ist jedes Mitglied der Gruppe gestorben, wird die .txt-Datei der Gruppe gelöscht.
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
    Funktion für das Spielemenü.
    """
    menu_loop = True
    while menu_loop:
        try:
            print("\n"+"Rivers of Time".center(len(SEPERATOR), " ")+"\n\n"+SEPERATOR)
            menu_inp = int(input("\n[1] Create a character\n[2] Create a group of adventurers\n[3] Show characters"
                                 "\n[4] Show adventurer groups\n[5] Play\n[6] End Game\n\n> "))
        except ValueError:                                                                                              # Das Exception-Handling ist vor den if-Abfragen gesetzt, damit es nicht durch die einzelnen Methoden mitläuft.
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

    game = Game()
    menu()