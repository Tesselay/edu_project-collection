# coding=utf-8
# coding=utf-8
# coding=utf-8
# coding=utf-8
# coding=utf-8
# coding=utf-8
from random import randint

class Character:
    """
    Klasse für die einzelnen Charaktere.
    """

    def __init__(self, name, lifepoints, strength, dexterity, intelligence, sleight_of_hand, charisma, stamina, intuition, weapon):
        """
        Der Konstruktor, welcher die Instanzen mit den gewünschten Werten erstellt.
        :param name: Name des Helden.
        :param lifepoints: Lebenspunkte des Helden.
        :param strength: Stärke des Helden.
        :param dexterity: Geschicklichkeit des Helden.
        :param intelligence: Intelligenz des Helden.
        :param sleight_of_hand: Fingerfertigkeit des Helden.
        :param charisma: Charisma des Helden.
        :param stamina: Ausdauer des Helden.
        :param intuition: Intuition des Helden.
        :param weapon: Waffe des Helden, als Instanz einer Klasse übergeben.
        __special_attack = Nur gesetzt um eine Referenz für Getter und Setter zu haben. Spielt erst in den Heldenklassen eine Rolle.
        """
        self.__name = name
        self.__lifepoints = lifepoints
        self.__strength = strength
        self.__dexterity = dexterity
        self.__intelligence = intelligence
        self.__sleight_of_hand = sleight_of_hand
        self.__charisma = charisma
        self.__stamina = stamina
        self.__intuition = intuition
        self.__weapon = weapon
        self.__special_attack = 0

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

    def set_charisma(self, cha):
        self.__charisma = cha

    def set_stamina(self, sta):
        self.__stamina = sta

    def set_intuition(self, ini):
        self.__intuition = ini

    def set_weapon(self, weapon):
        self.__weapon = weapon

    def set_special_attack(self, integer):
        self.__special_attack = integer

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

    def get_charisma(self):
        return self.__charisma

    def get_stamina(self):
        return self.__stamina

    def get_intuition(self):
        return self.__intuition

    def get_weapon(self):
        return self.__weapon

    def get_special_attack(self):
        return self.__special_attack

    def attack(self):
        """
        Methode für die Probe, welche auf Stärke basiert. Ausgabe von Erfolg der Probe abhängig.
        :return: True or False
        """
        if self.__special_attack == 1:
            self.set_special_attack(0)
        die_a = randint(1,20)
        die_b = randint(1,20)
        print("{} rolled {} and {} for an maximum threshold of respectively {} Strength and {} Stamina.".format(self.__name, die_a, die_b, self.__strength, self.__stamina))
        if die_a <= self.__strength and die_b <= self.__stamina:
            return randint(1,6) + self.__weapon.get_damage()
        else:
            return False

    def pickpocket(self):
        """
        Methode für die Probe, welche auf Fingerfertigkeit basiert. Ausgabe von Erfolg der Probe abhängig.
        :return: True or False
        """
        die_a = randint(1, 20)
        die_b = randint(1, 20)
        print("{} rolled {} and {} for an maximum threshold of respectively {} Sleight of Hand and {} Charisma.".format(self.__name, die_a, die_b, self.__sleight_of_hand, self.__charisma))
        if die_a <= self.__sleight_of_hand and die_b <= self.__charisma:
            print("{} was succesful! Your group earned 10 experience.".format(self.__name))
            return True
        else:
            print("{} failed. Nothing special happened.".format(self.__name))
            return False

    def wonder(self):
        """
        Methode für die Probe, welche auf Intelligenz basiert. Ausgabe von Erfolg der Probe abhängig.
        :return: True or False
        """
        die_a = randint(1, 20)
        die_b = randint(1, 20)
        print("{} rolled {} and {} for an maximum threshold of respectively {} Intelligence and {} Intuition.".format(self.__name, die_a, die_b, self.__intelligence, self.__intuition))
        if die_a <= self.__intelligence and die_b <= self.__intuition:
            print("{} won new knowledge! Your group earned {} experience.".format(self.__name, self.__intelligence*2))
            return True
        else:
            print("{} didn't think about something interesting.".format(self.__name))
            return False

    def balance(self):
        """
        Methode für die Probe, welche auf Geschicklichkeit basiert. Ausgabe von Erfolg der Probe abhängig.
        :return: True or False
        """
        die_a = randint(1, 20)
        die_b = randint(1, 20)
        print("{} rolled {} and {} for an maximum threshold of respectively {} Dexterity and {} Stamina.".format(self.__name, die_a, die_b, self.__dexterity, self.__stamina))
        if die_a <= self.__dexterity and die_b <= self.__stamina:
            print("{} was succesful! Your group earned 2 Experience.".format(self.__name))
            return True
        else:
            self.__lifepoints -= 10
            print("{} fell! She/He lost 10 lifepoints and has {} lifepoints left.".format(self.__name,self.__lifepoints))
            return False

    def rest(self):
        """
        Methode die die rest-Möglichkeit des Spiels enthält. Regeneriert Lebenspunkte und repariert die Waffe.        """
        lp_regen = randint(10,20)
        if self.__weapon.get_name() == "Empty Hand":
            print("{} regenerated {} lifepoints.".format(self.__name, lp_regen))
        else:
            print("{} regenerated {} lifepoints and repaired his weapon.".format(self.__name, lp_regen))
        self.__lifepoints += lp_regen
        self.__weapon.set_durability(self.__weapon.get_durability()+randint(10,20))