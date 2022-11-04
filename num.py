#!/usr/bin/env python3
# найти сумму введённых цифр
a = int(input("Введите число: "))
s = 0
while a> 0:
    s += a% 10
    a = a//10
print(s)    
