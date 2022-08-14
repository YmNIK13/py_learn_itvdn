pass  # Посчитать с помощью словаря сколько раз элемент повторяется в списке
# print('--------------')
# my_list = [3, 2, 1, 7, 0, 3, 25, 2, 1, 7, 0, -3, 25, -78, 1, 7, 0, -3, 25, -78, 100, -1, -3, 25, -78, 100, -1, 10]
# my_list.sort()
# dicts = {}
#
# for number in my_list:
#     counter = dicts.get(number, 0) + 1
#     dicts.update({number: counter})
#
# print(dicts)
#
# pass  # Пройтись по словарю и вывести все значения, у которых четный ключ
#
# for k, v in dicts.items():
#     if k % 2 == 0:
#         print(k, ' => ', v)


pass  # Удалить все ключи, значения которых начинаются с буквы а.
d = {'hello': 'a_world', 'hi': 'world', 'hello2': 'a_world', 'hi2': 'world'}
d0 = {}
print('d= ', d)
print('d0= ', d0)

for k, v in d.items():
    if k[0] != 'a':
        d0.update({k: v})

print('d= ', d)
print('d0= ', d0)
