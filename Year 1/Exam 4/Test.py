class Character:

    def __init__(self, test):
        self.__test = test

class Knight(Character):

    def __init__(self, test):
        Character.__init__(self, test)

    def get_test(self):
        self._Character__test += 10
        return self._Character__test

Test = Knight(10)
print(Test.get_test())