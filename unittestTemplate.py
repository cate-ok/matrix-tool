# Модуль для юнит тестов
import unittest

# Код, который нужно протестировать (он должен лежать в других файлах)
def add(a, b):
    return a + b

def is_even(a):    # четное ли число
    if a % 2 == 0:
        return True
    return False

def get_double_list(list1):
    return list1 * 2


# Это класс, который содержит методы с тестами. Его можно назвать по-другому.
# unittest.TestCase - значит, этот класс наследуется от класса TestCase, его реализация в подключенном модуле
class TestMyMethods(unittest.TestCase):

    # В этой функции можно добавить свойства объекту self (экземпляр класса TestMyMethods) - например, если нужна какая-то
    # строка число или др.объект который нужно использовать в разных функциях ниже (чтобы повторно его не создавать каждый раз)
    # Обратиться к нему можно будет self.[имя], в нашем примере self.pi
    def setUp(self):
        self.pi = 3.14

    def test_add(self):   # имена этих функций, содержащих тесты, должны начинаться со слова test
        # Пишем тесты. Параметры - функция с параметрами, которую хотим проверить, и правильный результат
        self.assertEqual(add(5, 8), 13)
        self.assertEqual(add(5, 10), 15)
        self.assertEqual(add(10, 8), 18)

    def test_even_number(self):
        # Проверяет, возвращается ли True
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(16))

    def test_my_getlist_func(self):
        # Проверяет списки на равенство (аналогично тому, что было выше, но со списками - тк их сложнее сравнить)
        my_list = [1,5,2]
        self.assertListEqual(get_double_list(my_list), [1,5,2,1,5,2])

# Эти строчки значат, что этот файл (с тестами) должен быть запущен напрямую (не как подключенный модуль)
if __name__ == '__main__':
    unittest.main()

# Если тесты выполнены без ошибок, в консоли появится сообщение
# Process finished with exit code 0