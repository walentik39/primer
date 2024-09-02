#!/usr/bin/env python3

t = int(input('Сколько градусов по цельсию? '))
if (t < -4):
    print('морозно')
elif (t< 0 and t >= -4):
    print('холодно')
elif (t >= 0 and t < 12):
    print('прохладно')
elif (t >= 12 and t < 27):
    print('тепло')
else:
    print('Жарко')
