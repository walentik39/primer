#!/usr/bin/env python3

# Кортеж это неизменяемый список.
#tuple_ = ('first',12, 56, 22,)
#tuple2 = ('second')
#print("Это :",  type(tuple_))
#print("Это :",  type(tuple2))
import random 

# Словари.
# Ключ : значение.
dict = {"яблоко" : 1,"груши": 3, "тыквы": 2}
for k in dict.keys():
    print(k)

for v in dict.values():
    print(v)

for y in dict.items():
    print(y)

print(dict["груши"])
dict["яблоко"] = 21
print(dict)
del(dict["тыквы"])
print(dict)
