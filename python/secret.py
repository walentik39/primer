#!/usr/bin/env python3

import random

secret = random.randint(1, 100)
guess = 0
tries = 0
print("У меня , есть секрет!")
print("Это число от 1 до 100. У вас 6 попыток.")
while guess != secret and tries < 6:
    guess = int(input("Какой ваш ответ? "))
    if guess < secret:
        print("Слишко мало.")
    elif guess > secret:
        print("Слишком много.")
    tries = tries + 1
if guess == secret:
    print("Вы угадали.")
else:
    print("Больше никакких попыток.")
    print("секретное слово", secret)
