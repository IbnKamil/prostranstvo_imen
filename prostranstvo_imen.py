def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
test_function()

# '''Проверка функции inner_function() в глобальной пространстве имен'''
# inner_function()