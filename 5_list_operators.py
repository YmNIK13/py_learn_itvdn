pass  # =============  ЛИСТ =====================
pass  # додати
# print('--------------')
# a = [1, 2, 3]
# print(a)
# a.append(5)
# print(a)
#
# a.clear()
# print(a)
pass  # з'єднати
# print('--------------')
# a = [1, 8, 9]
# b = [4, 8, 6]
# print(a)
# a.extend(b)
# print(a)
# print(a.index(8))
# print(a[a.index(8)])
pass  # з'єднати 2
# print('--------------')
#
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)
# print(a)
# a += b
# print(a)
pass  # забрать по индексу / развернуть
# print('--------------')
# a = [1, 2, 3, 4]
# print(a)
# removed_element = a.pop(3)
# print(a)
# print(removed_element)
# a.reverse()
# print(a)
pass  # сортировка
# print('--------------')
# a = [5, 2, 1, 3, 4]
# a.sort()
# print(a)
# b = [5, 2, 1, 3, 4]
# b.sort(reverse=True)
# print(b)
pass  # обход списков
# print('--------------')
# my_list = [5, 4, 3, 2, 1]
# for element in my_list:
#     print(element)
pass  # Удалить все четные элементы
# print('--------------')
# my_list = [1, 2, 3, 4, 5, 6]
# even_list = []
# for element in my_list:
#     if element % 2 == 0:
#         even_list.append(element)
#
# print(even_list)
pass  # Возвести все элементы списка в квадрат
# print('--------------')
# my_list = [2, 4, 6, 8]
# squares_list = []
# for element in my_list:
#     squares_list.append(element ** 2)
#
# print(squares_list)
pass  # Найти максимальное/минимальное значение
print('--------------')
my_list = [3, 2, 1, 7, 0, -3, 25, -78, 100, -1, 10]
max_element = my_list[0]
min_element = my_list[0]
for element in my_list:
    if max_element < element:
        max_element = element
    if min_element > element:
        min_element = element

print(min_element, max_element)
