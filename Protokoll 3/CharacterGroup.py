from random import randint

SEPERATOR = "-" * 50

class CharacterGroup:
    """
    Klasse für die Heldengruppe, welche im Hauptspiel benötigt wird.
    """

    def __init__(self, name, experience, level, herolist):
        """
        Der Konstruktor, welcher die Instanzen mit den gewünschten Werten erstellt.
        :param name: Name der Heldengruppe.
        :param experience: Erfahrung der Heldengruppe.
        :param level: Die Stufe der Gruppe.
        :param herolist: Liste mit den Helden, welche Teil der Gruppe sind. Werden als Instanz innerhalb der Liste übergeben.
        """
        self.__name = name
        self.__experience = experience
        self.__level = level
        self.__heroes = herolist

    def set_name(self, name):
        self.__name = name

    def set_experience(self, exp):
        self.__experience = exp

    def set_heroes(self, heroes):
        self.__heroes = heroes

    def set_level(self, level):
        self.__level = level

    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def get_heroes(self):
        return self.__heroes

    def get_level(self):
        return self.__level

    def level_check(self):
        """
        Kontrolliert, ob die Erfahrung der Gruppe den Grenzwert für ein Level-Up überschritten hat. Kann multiple
        Stufenanstiege hintereinander ausführen und kann sicherstellen, dass die gesammelten Erfahrungspunkte nicht die
        vorigen Level immer wieder auslösen.
        """
        level_exp = [60, 120, 190, 270, 360, 460, 570, 690, 820, 960, 1100, 1260]                                       # Enthält die benötigten Mengen an Erfahrung für einen Stufenanstieg.
        for items in range(0, len(level_exp)):
            if self.__experience > level_exp[items] and self.__level == items:                                          # Der Level-Up wird nur ausgeführt, sofern die Erfahrung höher als der benötigte Wert sind und das Level dem Index
                print("\n"+SEPERATOR+"\n\nYour party leveled up!")                                                      # entspricht, an der die Erfahrunggrenze steht. Dadurch wird jeder Level-Up nur ein Mal ausgeführt.
                self.__level += 1
                self.level_up()

    def level_up(self):
        """
        Die Methode, welche die Punkteverteilung beim Stufenanstieg regelt.
        """
        for items in range(0, len(self.__heroes)):                                                                      # For-Schleife welche so oft ausgeführt wird, wie es Charaktere in der Heldenliste gibt.
            print("\n"+self.__heroes[items].get_name()+", which attribute do you want to improve?\n")                   # Ruft den Getter für den Namen, des Heldenobjekts auf.
            error_loop = True
            while error_loop:                                                                                           # While-Schleife die solange wiederholt wird, bis ein Attribut vergeben wird.
                try:                                                                                                    # Da der folgende Input in einen Integer verwandelt wird, wird ein Exceptionhandling eingebaut.
                    attribute = int(input("[1] Strength\n[2] Dexterity\n[3] Intelligence\n[4] Sleight of hand\n\n> "))
                    if attribute == 1:
                        self.__heroes[items].set_strength(self.__heroes[items].get_strength() + 1)                      # Ruft den Setter des Attributes auf und übergibt den momentanen Wert +1.
                        error_loop = False                                                                              # Schleife wird beendet.
                    elif attribute == 2:
                        self.__heroes[items].set_dexterity(self.__heroes[items].get_dexterity() + 1)
                        error_loop = False
                    elif attribute == 3:
                        self.__heroes[items].set_intelligence(self.__heroes[items].get_intelligence() + 1)
                        error_loop = False
                    elif attribute == 4:
                        self.__heroes[items].set_sleight_of_hand(self.__heroes[items].get_sleight_of_hand() + 1)
                        error_loop = False
                    else:
                        print("There are only four attributes.")
                except ValueError:
                    print("Only (full) numbers!")
        self.level_check()                                                                                              # Geht danach erneut in den level_check um zu testen, ob genug EP für zwei Level-Ups erreicht wurden.
                                                                                                                        # (Wenn bspw. zu Beginn mehr als 35 EP in einem Ereignis erhalten wurden.