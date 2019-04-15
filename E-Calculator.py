class CALCULATOR:

    def __init__(self):
        self.name = "E-Taschenrechner"
        self.operation_counter = 0

    def menu(self):
        print(self.name)
        file = open("ausgabe.txt", "w")
        file.write("Ausgaben\n")
        while True:
            decider = input("\nWelche Operation wollen Sie nutzen?\n\n[1] Ohmsche Gesetz\n[2] Leitwert\n[3]"
                            " Gesamtwiderstand - Serienschaltung\n[4] Gesamtwiderstand - Parallelschaltung\n[5] "
                            "Frequenz\n[6] Anzahl der Operationen\n\n[Enter] Beenden\n\n> ")
            if decider == "1":
                self.resistance(file)
            elif decider == "2":
                self.conductance(file)
            elif decider == "3":
                self.serial_resistance(file)
            elif decider == "4":
                self.parallel_resistance(file)
            elif decider == "5":
                self.frequency(file)
            elif decider == "6":
                print("Operationen: " + str(self.operation_counter))
            elif decider == "":
                file.write("\n\nAnzahl der Operationen: "+str(self.operation_counter))
                file.close()
                break

    def resistance(self, file):
        print("\nOhmsche Gesetz")
        loop = True
        while loop:
            try:
                decider = input("\nWelche Form?\n\n[1] U = R * I\n[2] R = U / I\n[3] I = U / R\n\n[Enter] Abbruch\n\n> ")
                print("\nDenken Sie daran, dass die Werte gleichwertig sind (heißt gleiches Vorzeichen).")
                if decider == "1":
                    R = float(input("\nGeben Sie den Widerstandswert an.\n> "))
                    I = float(input("\nGeben Sie Stromstärkewert an.\n> "))
                    print("\nDer Spannungswert beträgt: {}".format(R * I))
                    self.operation_counter += 1
                    file.write("\n" + str(R) + " * " + str(I) + " = " + str(R*I))
                elif decider == "2":
                    U = float(input("\nGeben Sie den Spannungswert an.\n> "))
                    I = float(input("\nGeben Sie Stromstärkewert an.\n> "))
                    print("\nDer Widerstandswert beträgt: {}".format(U / I))
                    self.operation_counter += 1
                    file.write("\n" + str(U) + " / " + str(I) + " = " + str(U / I))
                elif decider == "3":
                    U = float(input("\nGeben Sie den Spannungswert an.\n> "))
                    R = float(input("\nGeben Sie Widerstandswert an.\n> "))
                    print("\nDer Stromstärkewert beträgt: {}".format(U / R))
                    self.operation_counter += 1
                    file.write("\n" + str(U) + " / " + str(R) + " = " + str(U / R))
                elif decider == "":
                    loop = False
            except ValueError:
                print("\nBitte geben Sie eine Zahl an.\n")
            except ZeroDivisionError:
                print("\nKeine Division durch Null.\n")

    def conductance(self, file):
        print("\nElektrischer Leitwert\n")
        loop = True
        while loop:
            try:
                decider = input("Welche Form?\n\n[1] I = G * U\n[2] G = I / U\n[3] U = I / G\n\n[Enter] Abbruch\n\n> ")
                print("\nDenken Sie daran, dass die Werte gleichwertig sind (heißt gleiches Vorzeichen).")
                if decider == "1":
                    G = int(input("\nGeben Sie den Leitwert an.\n> "))
                    U = int(input("\nGeben Sie Spannugnswert an.\n> "))
                    print("\nDer Stromstärkewert beträgt: {}".format(G * U))
                    self.operation_counter += 1
                    file.write("\n" + str(G) + " * " + str(U) + " = " + str(G * U))
                elif decider == "2":
                    I = int(input("\nGeben Sie Stromstärkewert an.\n> "))
                    U = int(input("\nGeben Sie den Spannungswert an.\n> "))
                    print("\nDer Leitwert beträgt: {}".format(I / U))
                    self.operation_counter += 1
                    file.write("\n" + str(I) + " / " + str(U) + " = " + str(I / U))
                elif decider == "3":
                    I = int(input("\nGeben Sie den Stromstärkewert an.\n> "))
                    G = int(input("\nGeben Sie Leitwert an.\n> "))
                    print("\nDer Spannungswert beträgt: {}".format(I / G))
                    self.operation_counter += 1
                    file.write("\n" + str(I) + " / " + str(G) + " = " + str(I / G))
                elif decider == "":
                    loop = False
            except ValueError:
                print("\nBitte geben Sie eine Zahl an.\n")
            except ZeroDivisionError:
                print("\nKeine Division durch Null.\n")
            except:
                print("\nUnbekannter Fehler.\n")

    def serial_resistance(self, file):
        print("\nGesamtwiderstand - Serienschaltung\n")
        loop = True
        while loop:
            try:
                decider = input("[1] Abfrage\n[Enter] Abbruch\n\n> ")
                if decider == "1":
                    resistances = []
                    counter = 0
                    max_resistance = 0
                    amount = int(input("Wie viele Widerstände exisierten in der Schaltung?\n>"))
                    print("\nDie Widerstände werden nacheinander abgefragt.\n")
                    for items in range(1, amount):
                        resistor = int(input("Widerstandswert: "))
                        resistances.append(resistor)
                    for items in range(1, len(resistances)):
                        max_resistance += resistances[counter]
                        counter += 1
                    print("Der Gesamtwiederstand beträgt: {}".format(max_resistance))
                    self.operation_counter += 1
                    str_resistances = " + ".join(str(e) for e in resistances)
                    file.write("\n" + str_resistances + " = " + max_resistance)
                elif decider == "":
                    loop = False
            except ValueError:
                print("\nBitte geben Sie eine Zahl an.\n")
            except:
                print("\nUnbekannter Fehler.\n")

    def parallel_resistance(self, file):
        print("\nGesamtwiderstand - Parallelschaltung")
        loop = True
        while loop:
            try:
                decider = input("\n[1] Abfrage\n[Enter] Abbruch\n\n> ")
                if decider == "1":
                    resistances = []
                    counter = 1
                    amount = int(input("\nWie viele Widerstände exisierten in der Schaltung?\n> "))
                    print("\nDie Widerstände werden nacheinander abgefragt.\n")
                    for items in range(1, amount+1):
                        resistor = int(input("Widerstandswert: "))
                        resistances.append(resistor)
                    multiplier_resistance = resistances[0]
                    addition_resistance = resistances[0]
                    for items in range(1, len(resistances)):
                        multiplier_resistance *= resistances[counter]
                        addition_resistance += resistances[counter]
                        counter += 1
                    print("Der Gesamtwiederstand beträgt: {}".format(multiplier_resistance / addition_resistance))
                    self.operation_counter += 1
                    multiplier_resistances = " * ".join(str(e) for e in resistances)
                    addition_resistances = " + ".join(str(e) for e in resistances)
                    file.write("\n" + multiplier_resistances + " / " + addition_resistances + " = " +
                               multiplier_resistance / addition_resistance)
                elif decider == "":
                    loop = False
            except ValueError:
                print("\nBitte geben Sie eine Zahl an.\n")
            except ZeroDivisionError:
                print("\nKeine Division durch Null.\n")

    def frequency(self, file):
        print("\nFrequenz\n")
        loop = True
        while loop:
            try:
                decider = input("Welche Form?\n\n[1] f = 1/T\n[2] T = 1/f\n\n[Enter] Abbruch\n\n> ")
                if decider == "1":
                    T = int(input("\nGeben Sie die Periodendauer an.\n> "))
                    print("\nDie Frequenz beträgt: {}".format(1 / T))
                    self.operation_counter += 1
                    file.write("\n" + "1 / " + str(T) + " = " + str(1 / T))
                elif decider == "2":
                    f = int(input("\nGeben Sie die Frequenz an.\n> "))
                    print("\nDie Periodendauer beträgt: {}".format(1 / f))
                    self.operation_counter += 1
                    file.write("\n" + "1 / " + str(f) + " = " + str(1 / f))
                elif decider == "":
                    loop = False
            except ValueError:
                print("\nBitte geben Sie eine Zahl an.\n")
            except ZeroDivisionError:
                print("\nKeine Division durch Null.\n")


if __name__ == "__main__":
    Calculator = CALCULATOR()
    Calculator.menu()
