#!/usr/bin/env python3

class Human:

    default_name = "No name"
    default_age = 0
    
    def __init__(self, name=default_name, age=default_age):
        # Динамические поля
        # публичный
        self.name = name
        self.age = age
        #Приветные
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name:{self.name}')
        print(f'Age: {self.age}')
        print(f'Money:{self.__money}')
        print(f'House: {self.__house}')

    @staticmethod
    def default_info():
        print(f'Default Name: {Human.default_name}')
        print(f'Default Age: {Human.default_age}')

    def earn_money(self,amount):
        self.__money += amount
        print(f'Earn {amount} Money current value {self.__money}')

    def by_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print("Not amount money")

    #Привватный метод
    def __make_deal(self,house, price):
        self.__money -= price
        self.__house = house

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'Final_price : {final_price}')
        return final_price

class SmallHouse(House):
    default_area = 40

    def __init__(self,price):
        super().__init__(SmallHouse.default_area, price)

if __name__=='__main__':
    Human.default_info()
    aleksander = Human('Sasha', 27)
    aleksander.info()
    small_house = SmallHouse(8_500)

    aleksander.earn_money(5000)
    aleksander.by_house(small_house, 5)
    aleksander.earn_money(20000)
    aleksander.by_house(small_house, 5)
    aleksander.info()
