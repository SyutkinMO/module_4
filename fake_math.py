#______Функция деления на 0 с возвратом ошибки_____

def divide (first, second):
    if second == 0:
        return 'Ошибка'
    else:
        return round(first / second, 2)

divide (5,0)