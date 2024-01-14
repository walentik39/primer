#!/usr/bin/env python3

def factorial(n):

    res = 1

    for i in range(2, n+1):
        res *= i
    return res
 # Driver Code
num = int(input("Число : "))
print("Factorial of", num, "is",factorial(num))
