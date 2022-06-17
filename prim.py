#!/usr/bin/env python3

from random import randint

numbers = []
for x in range(12):
    numbers.append(randint(0,57))
size = len(numbers)
i =0
count = 0
print("No sorted:\t", numbers)
while(i<=size - 1):
    j =0
    while(j<=size-2):
        if(numbers[j] > numbers[j+1]):
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
            count +=1
            print(numbers)
        j = j + 1
    i = i + 1    
print("Sorted :\t\t", numbers)
print(count)
