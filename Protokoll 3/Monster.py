from random import randint

class Monster:
    """
    Klasse, die die Monster für den Kampf im Spiel erstellt.
    """

    def __init__(self, name, health, min_damage, att):
        """
        Der Konstruktor, welcher die Instanzen mit den gewünschten Werten erstellt.
        :param name: Name des Monsters.
        :param health: Lebenspunkte des Monsters.
        :param min_damage: Der Schaden, den das Monster auf jeden Fall anrichtet.
        :param att: Das Testattribut, mit dem gewürfelt wird, ob das Monster trifft.
        """
        self.__name = name
        self.__health = health
        self.__min_damage = min_damage
        self.__attribute = att

    def set_name(self, name):
        self.__name = name

    def set_health(self, hp):
        self.__health = hp

    def set_min_damage(self, min_dmg):
        self.__min_damage = min_dmg

    def set_attribute(self, att):
        self.__attribute = att

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_min_damage(self):
        return self.__min_damage

    def get_attribute(self):
        return self.__attribute

    def dmg_done(self):
        """
        Berechnet den angerichteten Schaden.
        :return: self.__min_damage + dmg_bonus
        """
        dmg_bonus = randint(1,2)                                                                                        # Jeder Angriff erhält einen minimalen Bonusschaden. Der Kampf soll dadurch ein wenig mehr zufallsabhängig sein.
        return self.__min_damage + dmg_bonus

    def attack(self):
        """
        Die Probe mit der entschieden wird, ob das Monster trifft. Abhängig vom Attribut.
        :return:
        """
        die = randint(1, 20)
        if die <= self.__attribute:
            return True
        else:
            return False