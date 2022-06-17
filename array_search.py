#!/usr/bin/env python3

def array_search(A:list, N:int, x:int):
    """ Осуществляет поиск числа x в массиве A
        от 0 до N-1 индекса включительно.
        Возвращает индекс элемента x в массиве A,
        Или -1, если такого нет.
        Если в массиве несколько одинаковых элементов,
        равных x, то вернуть индекс первого по счёту.
    """
    for k in range(N):
        if A[k] == x:
            return k
    return -1

def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    A2 = [10, 20, 30, 40, 50]
    m = array_search(A2, 5, 55)
    if m == 4:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

    A3 = [-3, -2, -1, 0, 1]
    m = array_search(A3, 5, 0)
    if m == 3:
        print("#test3 - ok")
    else:
        print("#test3 -fail")

test_array_search()        
