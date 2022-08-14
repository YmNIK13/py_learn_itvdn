# print('# Вывод в консоль')
# print(1)
# print([1, 4, [5]])
# print('lists:', [1, 4, 5], [1, 4, 5])
#
# print('--------------')
# print('# длина объекта')
#
# print(len('dfgd'))
# print(len([1, 4, 5]))
# print(len([1, 4, [5]]))
# print('--------------')

# print('# Преобразование данных')
# x = 1
# x_str = str(x)
# print(x, type(x), 'В строку ', x_str, type(x_str))
#
# x = '1'
# x_int = int(x)
# print(x, type(x), 'В число ', x_int, type(x_int))
#
# x = ' 123 '
# x_int = int(x)
# print(x, type(x), 'В число ', x_int, type(x_int))

# # x = ' 12 3 '
# x = ' 12 3a '
# x_int = int(x)
# print(x, type(x), 'В число ', x_int, type(x_int))


# x = ' 123 '
# x_fl = float(x)
# print(x, type(x), 'В вещественное число ', x_fl, type(x_fl))
#
# # x = ' 123,5 ' # error
# x = ' 123.5 '  # error
# x_fl = float(x)
# print(x, type(x), 'В вещественное число ', x_fl, type(x_fl))
#
# x = []
# print('Пустой лист -', bool(x))
# x = {}
# print('Пустой словарь -', bool(x))
# x = None
# print('None -', bool(x))
# x = ''
# print('Пустая строка -', bool(x))
# x = ' '
# print('Строка с пробелом -', bool(x))
# x = '0'
# print('Строка "0" -', bool(x))
# print('--------------')

# print('# Агрегатные функции')
# x = [1, 2, 3, 4, 5]
# print('Sum:', sum(x))
# print('Average:', sum(x) / len(x))
# print('Max:', max(x))
# print('Min:', min(x))
# print('--------------')

# print('# Анонимные функции')
# x = [1, 2, 3, 4, 5]
#
#
# def make_smth(function):
#     for element in x:
#         print(function(element))
#
#
# make_smth(lambda a: a * 10 + 10)
# print('--------------')

# print('# Рекурсия')
#
#
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print('factorial: ', factorial(10))
# print('--------------')

print('# Примеры')


def do_n(n):
    for m in range(1, n + 1):
        print(m)


def sqr(height, length):
    return height * length


do_n(10)
print('+++')
print(sqr(2, 4))
