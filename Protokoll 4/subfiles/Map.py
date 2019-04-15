from random import randint


class Map:
    """
    Klasse, welche die Spielkarte samt Bewegungsfunktion enthält.
    """

    def __init__(self):
        """
        Dem Konstruktor werden keine Variablen übergeben, jedoch enthält er einige wichtige Variablen.
        __map: Enthält die Map in Form einer 2-Dimensionalen Liste
        __test_legend: Enthält die Buchstaben für die jeweiligen Proben.
        __save: Enthält den vorigen Wert des Feldes, auf dem die Heldengruppe sich bewegt.
        __save_index: Enthält den zugehörigen Index.
        """
        self.__map = []
        self.__test_legend = ["F", "F", "F", "F", "F", "P", "P", "P", "P", "P", "W", "W", "W", "W", "W", "B", "B", "B", "B", "B", "R"]
        self.__save = None
        self.__save_index = None

    def map_creation(self):
        """
        Erstellt die Spielkarte.
        """
        end_loop = True
        rows = randint(10, 20)
        columns = randint(10, 20)
        for items_a in range(0, rows):
            self.__map.append([])
            for items_b in range(0, columns):
                self.__map[items_a].append("#")
        self.__map[randint(0, len(self.__map)-1)][randint(0, len(self.__map[0])-1)] = "\033[1;33mH\033[1;m"                                 # Setzt die Heldengruppe zufällig auf irgendeine Stelle der Karte.
        while end_loop:                                                                                                                     # Schleife um das Ende zu setzen.
            rnd_a = randint(-1, len(self.__map)-1)
            rnd_b = randint(-1, len(self.__map[0])-1)
            if self.__map[rnd_a][rnd_b] == "\033[1;33mH\033[1;m":                                                                           # Falls das Ende genau auf dem Feld landen würde, wo der Start ist, wird der Befehl übersprungen.
                pass
            else:                                                                                                                           # Andernfalls setzt er das Ende.
                self.__map[rnd_a][rnd_b] = "\033[1;31mE\033[1;m"
                end_loop = False

    def map_print(self):
        """
        Gibt die Karte aus.
        """
        for items_a in self.__map:
            for items_b in items_a:
                print("["+items_b+"]", end="")
            print()
        print("\033[1;31mS\033[1;m - Start (Kann nicht betreten werden)\n\033[1;31mE\033[1;m - Ende\n\033[1;33mH\033[1;m - Heldengruppe\n"
              "F/P/W/B/R - Absolvierte Proben\n# - Unbekanntes Feld (Zufällige Probe)")

    def movement(self):
        """
        Methode, welche die Bewegung auf dem Feld regelt.
        :return: True or False or rnd_test
        """
        self.map_print()                                                                                                                    # Vor Beginn wird jedes Mal die Karte ausgegeben.
        direction = input("\nIn what direction do you want to move?\n[w] Up\n[s] Down\n[a] Left\n[d] Right\n\n> ")
        index_a, index_b = self.pathfinder()                                                                                                # Methode, die den Standort der Heldengruppe findet und den Index in Variablen speichert.
        if direction == "w" or direction == "W":
            fieldtest = self.box_checker(index_a-1, index_b)                                                                                # Methode, die nachguckt, was sich auf dem Feld befindet, auf das sich bewegt werden soll.
            if type(fieldtest) is str and fieldtest != "end":                                                                               # Falls ein Streng zurückgegeben wird, der nicht "end" ist, wird die Bedingung ausgeführt.
                self.__map[index_a-1].insert(index_b, "\033[1;33mH\033[1;m")                                                                # Fügt das Symbol der Heldengruppe an den gewünschten Ort ein.
                if self.__save is not None:                                                                                                 # Wird ausgeführt, wenn im Symbolspeicher ein Wert enthalten ist (also bei allem außer dem Spielbeginn).
                    self.__map[self.__save_index[0]][self.__save_index[1]] = self.__save                                                    # Setzt den Wert, vom dem sich bewegt wurde, gleich dem Wert im Symbolspeicher.
                else:
                    self.__map[index_a][index_b] = "\033[1;31mS\033[1;m"                                                                    # Bei Spielbeginn, wird das Symbol für den Start gesetzt.
                self.__save, self.__save_index = self.__map[index_a-1].pop(index_b+1), [index_a-1, index_b]                                 # Speichert die Werte auf die sich bewegt wurde im Zwischenspeicher. Durch .pop wird das .insert von zuvor ausgeglichen.
                if fieldtest == "test":                                                                                                     # Falls das betretene Feld ein Hashtag enthält, wird die Bedingung erfüllt ("test wird bei box.checker zurückgegeben).
                    rnd_test = randint(0, len(self.__test_legend) - 1)                                                                      # Speichert den Index eines zufälligen Tests in einer Variable.
                    self.__save = self.__test_legend[rnd_test]                                                                              # Setzt den Symbolspeicher auf das Symbol für den Test. Wird durch die Bedingung nur ausgeführt, sofern dort noch kein Wert war.
                    return rnd_test                                                                                                         # Gibt den Index des Testes zurück (wird für die Auswahl der Probe genutzt.)
            elif fieldtest == "end":                                                                                                        # Wird erfüllt, sofern die Heldengruppe am Ende ankommt.
                print("You've finished this map!")
                return False                                                                                                                # Gibt dafür False zurück
            else:
                print("You can't go in this direction!")
            return True                                                                                                                     # Gibt True zurück, sollte weder das Ende, noch ein Test erreicht worden sein.
        elif direction == "s" or direction == "S":
            fieldtest = self.box_checker(index_a+1, index_b)
            if type(fieldtest) is str and fieldtest != "end":
                self.__map[index_a+1].insert(index_b, "\033[1;33mH\033[1;m")
                if self.__save is not None:
                    self.__map[self.__save_index[0]][self.__save_index[1]] = self.__save
                else:
                    self.__map[index_a][index_b] = "\033[1;31mS\033[1;m"
                self.__save, self.__save_index = self.__map[index_a+1].pop(index_b+1), [index_a+1, index_b]
                if fieldtest == "test":
                    rnd_test = randint(0, len(self.__test_legend) - 1)
                    self.__save = self.__test_legend[rnd_test]
                    return rnd_test
            elif fieldtest == "end":
                print("Congratulations, you've finished this map!\nIf you want to continue playing, start another game.")
                return False
            else:
                print("You can't go in this direction!")
            return True
        elif direction == "a" or direction == "A":
            """
            Wird anders als die anderen Richtungen geregelt, da die Bewegung nach links durch die Art der Indexfindung der Heldengruppe und
            der Art der Funktionsweise der Zwischenspeicherung von Symbolen und der Bewegung zu Fehlern führte.
            """
            fieldtest = self.box_checker(index_a, index_b-1)
            if type(fieldtest) is str and fieldtest != "end":
                save = self.__map[index_a][index_b - 1]                                                                                     # Der Index auf dem sich bewegt wird, wird zuvor zwischengespeichert.
                self.__map[index_a].insert(index_b - 1, "\033[1;33mH\033[1;m")
                if self.__save is not None:
                    self.__map[self.__save_index[0]][self.__save_index[1]] = self.__save
                else:
                    self.__map[index_a][index_b] = "\033[1;31mS\033[1;m"
                self.__save = save                                                                                                          # Speichert den vorigen Wert im Symbolspeicher.
                self.__map[index_a].pop(index_b + 1)                                                                                        # Entfernt das überbleibende Symbol ohne es zu speichern, da sonst das Heldensymbol gespeichert wird.
                self.__save_index = [index_a, index_b-1]
                if fieldtest == "test":
                    rnd_test = randint(0, len(self.__test_legend) - 1)
                    self.__save = self.__test_legend[rnd_test]
                    return rnd_test
            elif fieldtest == "end":
                print("You've finished this map!")
                return False
            else:
                print("You can't go in this direction!")
            return True
        elif direction == "d" or direction == "D":
            fieldtest = self.box_checker(index_a, index_b+1)
            if type(fieldtest) is str and fieldtest != "end":
                self.__map[index_a].insert(index_b, "\033[1;33mH\033[1;m")
                if self.__save is not None:
                    self.__map[self.__save_index[0]][self.__save_index[1]] = self.__save
                else:
                    self.__map[index_a][index_b] = "\033[1;31mS\033[1;m"
                self.__save, self.__save_index = self.__map[index_a].pop(index_b+2), [index_a, index_b+1]
                if fieldtest == "test":
                    rnd_test = randint(0, len(self.__test_legend)-1)
                    self.__save = self.__test_legend[rnd_test]
                    return rnd_test
            elif fieldtest == "end":
                print("You've finished this map!")
                return False
            else:
                print("You can't go in this direction!")
            return True

    def box_checker(self, index_a, index_b):
        """
        Methode die kontrolliert, was sich in dem Feld befindet, auf das sich bewegt werden soll.
        :param index_a: Index der Hauptliste.
        :param index_b: Index der Liste innerhalb der Hauptliste.
        :return: "solved" or "test" or "end" or False
        """
        try:
            if index_a < 0 or index_b < 0:                                                                                                  # Erste Bedingung, die sicherstellt, dass man sich nicht out of boundary bewegt.
                raise IndexError
            elif self.__map[index_a][index_b] == "F" or self.__map[index_a][index_b] == "P" or self.__map[index_a][index_b] == "W" or \
                    self.__map[index_a][index_b] == "B" or self.__map[index_a][index_b] == "R":
                return "solved"
            elif self.__map[index_a][index_b] == "#":
                return "test"
            elif self.__map[index_a][index_b] == "\033[1;31mE\033[1;m":
                return "end"
        except IndexError:
            return False

    def pathfinder(self):
        """
        Methode, die den Ort des Spielers innerhalb der Liste sucht.
        :return: items, items_b
        """
        for items in range(0, len(self.__map)):
            for items_b in range(0, len(self.__map[0])):
                if self.__map[items][items_b] == "\033[1;33mH\033[1;m":
                    return items, items_b

