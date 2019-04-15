from random import randint

class Character:
    """
    Klasse für die einzelnen Charaktere.
    """

    def __init__(self, name, lifepoints, strength, dexterity, intelligence, sleight_of_hand, weapon):
        """
        Der Konstruktor, welcher die Instanzen mit den gewünschten Werten erstellt.
        :param name: Name des Helden.
        :param lifepoints: Lebenspunkte des Helden.
        :param strength: Stärke des Helden.
        :param dexterity: Geschicklichkeit des Helden.
        :param intelligence: Intelligenz des Helden.
        :param sleight_of_hand: Fingerfertigkeit des Helden.
        :param weapon: Waffe des Helden, als Instanz einer Klasse übergeben.
        """
        self.__name = name
        self.__lifepoints = lifepoints
        self.__strength = strength
        self.__dexterity = dexterity
        self.__intelligence = intelligence
        self.__sleight_of_hand = sleight_of_hand
        self.__weapon = weapon

    def set_name(self, name):
        self.__name = name

    def set_lifepoints(self, lp):
        self.__lifepoints = lp

    def set_strength(self, str):
        self.__strength = str

    def set_dexterity(self, dex):
        self.__dexterity = dex

    def set_intelligence(self, int):
        self.__intelligence = int

    def set_sleight_of_hand(self, soh):
        self.__sleight_of_hand = soh

    def set_weapon(self, weapon):
        self.__weapon = weapon

    def get_name(self):
        return self.__name

    def get_lifepoints(self):
        return self.__lifepoints

    def get_strength(self):
        return self.__strength

    def get_dexterity(self):
        return self.__dexterity

    def get_intelligence(self):
        return self.__intelligence

    def get_sleight_of_hand(self):
        return self.__sleight_of_hand

    def get_weapon(self):
        return self.__weapon

    def attack(self):
        """
        Methode für die Probe, welche auf Stärke basiert. Ausgabe von Erfolg der Probe abhängig.
        :return: True or False
        """
        die = randint(1,20)
        if die <= self.__strength:
            return True
        else:
            return False

    def pickpocket(self):
        """
        Methode für die Probe, welche auf Fingerfertigkeit basiert. Ausgabe von Erfolg der Probe abhängig.
        :return: True or False
        """
        die = randint(1,20)
        if die <= self.__sleight_of_hand:
            return True
        else:
            return False

    def wonder(self):
        """
        Methode für die Probe, welche auf Intelligenz basiert. Ausgabe von Erfolg der Probe abhängig.
        :return: True or False
        """
        die = randint(1,20)
        if die <= self.__intelligence:
            return True
        else:
            return False

    def balance(self):
        """
        Methode für die Probe, welche auf Geschicklichkeit basiert. Ausgabe von Erfolg der Probe abhängig.
        :return: True or False
        """
        die = randint(1,20)
        if die <= self.__dexterity:
            return True
        else:
            return False
