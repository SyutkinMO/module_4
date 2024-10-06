# ______Пространство имен____


def test_function():
    def inner_function():
        print('Я в области видимости test_function')

    inner_function()


test_function()
# inner_function() - при вызове происходит ошибка
