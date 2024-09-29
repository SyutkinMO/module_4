#______Функция деления на 0 с возвратом бесконечности_____

from math import inf

def divide (first, second):
    if second == 0:
        return inf
    else:
        return round(first / second, 2)

divide (5,0)