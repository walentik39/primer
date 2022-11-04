#!/usr/bin/env python3

numbers = [1, 8, 3, 2, 6]
size = 5
current_index = 0
max_numer_index = 0
max = numbers[0]
while(current_index < size):
    if(numbers[current_index] > max):
        max = numbers[current_index]
        max_number_index = current_index
    current_index = current_index + 1
print(max)
print(current_index) #Логическая ошибка, лишняя строчка#
