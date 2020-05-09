from subfiles.Character import Character
from random import randint


class Acrobat(Character):
    """
    Klasse der Heldenklasse Acrobat. Der Name der Klasse ist als globales Klassenattribut gesetzt.
    """
    __class_name = "Acrobat"

    def __init__(self, name, lifepoints, strength, dexterity, intelligence, sleight_of_hand, charisma, stamina, intuition, weapon, special_attack=0):
        """
        Enthält die übergebenen Werte der Character-Klase
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
        :param special_attack: Variable die entweder 1 oder 0 enthält und bestimmt, ob die SA ausgeführt werden kann.
        """
        Character.__init__(self, name, lifepoints, strength, dexterity, intelligence, sleight_of_hand, charisma, stamina, intuition, weapon)

    def get_class_name(self):
        return self.__class_name

    def assault(self):
        """
        Spezialangriff des Akrobaten.
        :return: True or False
        """
        self.set_special_attack(1)
        die_a = randint(1,20)
        die_b = randint(1,20)

        if die_a <= self._Character__dexterity and die_b <= self._Character__stamina:
            return True
        else:
            return False