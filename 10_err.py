# ====================== Обработка исключений
# a = 10
# b = 0
#
# try:
#     c = a / b
# except:
#     print("division on zero")
#     c = 0
#
# print(c)
# ====================== Множественная обработка исключений
# def x():
#     a = 10
#
#
# try:
#     print(a)
# except ValueError as error:
#     print(error)
# except NameError as error:
#     print("No value a. Error: " + str(error))
# ====================== Обработка не верного значения
# try:
#     print(int('abc'))
# except ValueError as error:
#     print(error)
# ====================== Обработка не верного условия
# assert проверяет верность условия и кидает пустое исключение
# try:
#     assert 2 == 3
# except AssertionError as error:
#     print(error)
# ====================== Обработка не верного типа
# x = None
# try:
#     for elem in x:
#         print(elem)
# except TypeError as error:
#     print(error)
# # ======================

# Реализовать функцию, которая будет принимать на вход номер месяца,
# вернуть его название и реализовать в нем несколько обработок исключений
#
# def month_str(m):
#     months_dictionary = {
#         1: "January",
#         2: "February",
#         3: "March",
#         4: "April",
#         5: "May",
#         6: "June",
#         7: "July",
#         8: "August",
#         9: "september",
#         10: "October",
#         11: "November",
#         12: "December",
#     }
#
#     try:
#         return months_dictionary[m]
#     except KeyError as key_error:
#         print(key_error, 'Используйте числа только от 1-12')
#     except TypeError as type_error:
#         print(type_error, 'Используйте числа только от 1-12')
#
#
# print(month_str(1))
# print(month_str([1, 2]))
# print(month_str(13))
# # ======================

# Нужно проверить, все ли числа в последовательности уникальны
# и реализовать несколько обработок исключений.

def check(sequence):
    if len(set(sequence)) == len(sequence):
        return True
    return False


def check_sequence_unique(array):
    try:
        return check(array)
    except TypeError as type_error:
        print(type_error, 'Используйте строку, лист или сетс')


print(check_sequence_unique([1, 2, 3, 4]))
print(check_sequence_unique('abcdf'))
print(check_sequence_unique(False))
print(check_sequence_unique(None))
print(check_sequence_unique(123))
