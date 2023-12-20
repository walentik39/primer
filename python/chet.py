#!/usr/bin/env python3

print("Найдём сумму всех четных:")
i = 1
sum1 = 0
n = int(input("Введите конечное число: "))
for i in range(1,n+1):
    if i%2==0:
        sum1 += i
        i += 1
print("Сумма всех чётных чисел","=",sum1)
