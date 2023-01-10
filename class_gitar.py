#!/usr/bin/env python3

class Guitar:
    def __init__(self):
        self.n_strings = 6
        self.play()
    def play(self):
        print("pam pam pam pam pam pam pam")


class ElectricGuitar(Guitar):
    def __init__(self):
        super().__init__()
        self.n_strings = 8
        self.__cost = 50
    def playLouder(self):
        print("pam pam pam pam pam pam pam".upper())

my_guitar = ElectricGuitar()
my_guitar.playLouder()
print("chile class:",my_guitar.n_strings)
print("parent class:", Guitar().n_strings)
print(my_guitar._ElectricGuitar__cost)
