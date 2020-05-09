# coding=utf-8
# coding=utf-8
# coding=utf-8
from random import randint

class Monster:
    """
    Klasse, die die Monster für den Kampf im Spiel erstellt.
    """

    def __init__(self, name, health, att, experience):
        """
        Der Konstruktor, welcher die Instanzen mit den gewünschten Werten erstellt.
        :param name: Name des Monsters.
        :param health: Lebenspunkte des Monsters.
        :param attribute: Das Testattribut, mit dem gewürfelt wird, ob das Monster trifft. Bestimmt ebenfalls Schaden.
        :param experience: Die Erfahrungspunkte, die das Monster bei Tod bringt.
        """
        self.__name = name
        self.__health = health
        self.__attribute = att
        self.__experience = experience

    def set_name(self, name):
        self.__name = name

    def set_health(self, hp):
        self.__health = hp

    def set_attribute(self, att):
        self.__attribute = att

    def set_experience(self, exp):
        self.__experience = exp

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_attribute(self):
        return self.__attribute

    def get_experience(self):
        return self.__experience

    def attack(self):
        """
        Die Probe mit der entschieden wird, ob das Monster trifft. Abhängig vom Attribut.
        :return:
        """
        return self.__attribute + randint(1,6)
