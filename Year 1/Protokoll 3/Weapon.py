from random import randint

class Weapon:
    """
    Klasse für die Waffen.
    """

    def __init__(self, name, damage, durability):
        """
        Der Konstruktor, welcher die Instanzen mit den gewünschten Werten erstellt.
        :param name: Name der Waffe.
        :param damage: Schaden der Waffe.
        :param durability: Haltbarkeit der Waffe.
        """
        self.__name = name
        self.__damage = damage
        self.__durability = durability

    def set_name(self, name):
        self.__name = name

    def set_damage(self, damage):
        self.__damage = damage

    def set_durability(self, durability):
        self.__durability = durability

    def get_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage

    def get_durability(self):
        return self.__durability

    def durability_damage(self):
        """
        Berechnet den Haltbarkeitsschaden der Waffe und führt einen Haltbarkeitstest mithilfe einer weiteren Methode aus.
        """
        die = randint(5,35)                                                                                             # Zieht zwischen 5 und 40 von der Haltbarkeit der Waffe ab.
        self.__durability -= die
        self.durability_check()                                                                                         # Methode zum Haltbarkeitstest.

    def durability_check(self):
        """
        Sofern die Haltbarkeit der Waffe unter 1 fällt, wird Name und Schaden der bestehenden Waffe überschrieben.
        """
        if self.__durability <= 0  and self.__name != "Empty Hand":                                                     # Die Methode wird nur ausgeführt, wenn es sich bei Waffe nicht um Empty Hand handelt.
            print("\nYour {} broke.".format(self.__name))                                                               # Dadurch kann der Spieler erkennen, wann die Waffe zerstört wurde.
            self.__name = "Empty Hand"
            self.__damage = 1