#!/usr/bin/env python3

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

# Driver Code
num = int(input("Введите число: "))
print("Factorial of",num,"is",factorial(num))