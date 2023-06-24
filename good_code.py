#!/usr/bin/env python3


import random

def generate_pin(length:int) -> str:
    return ''.join(str(random.randint(0,9)) for _ in range(length))

def replace_nums(a_list:list, value: str) -> list[str]:
    return [element.replace('2', value) for element in a_list]

def replace_nums_inplace(a_list:list, value: str):
    for index in range(len(a_list)):
        a_list[index] = a_list[index].replace('5', value)
    return None    

def write_file(filename: str, data: str):
    with open(filename,'w') as file:
        file.write(data)

if __name__=='__main__':
    pins = [generate_pin(8) for _ in range(8)]
    #pins_without_nums = replace_nums(pins, '6')
    replace_nums_inplace(pins, '6')
    #str_list = '\n'.join(pins_without_nums)
    str_list = '\n'.join(pins)
    write_file('test.odt', str_list)
    print(pins)
