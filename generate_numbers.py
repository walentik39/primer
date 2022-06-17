#!/usr/bin/env python3

def generate_numbers(N, M, prefix= None):
    if M == 0:
        print(prefix)
        return
    prefix = prefix or []
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()

generate_numbers(int(input()),int(input()))

