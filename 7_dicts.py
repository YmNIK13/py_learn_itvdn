pass  # =============  СЛОВАРИ  =====================
# # print('--------------')
# my_dict = {'key': 'value', 10: True, 0.2: 'hello'}
# print(my_dict)
#
# print(my_dict['key'])
# print(my_dict[10])
#
# # print(my_dict['value'])
# print('No key - ', my_dict.get('value'))
# print('No key (default) - ', my_dict.get('value', -1))

# print('--------------')
# d = {1: 10, 2: 20}
# print(d)
# d.clear()
# print(d)

# print('--------------')
# d = {1: 10, 2: 20}
# print(d.items())

# print('--------------')
# d = {'hello': 'world', 'hi': 'world', 'hello2': 'world', 'hi2': 'world'}
# print('d= ', d)
#
# # забираем из словаря по ключу
# print(d.pop('hello'))
# print('d= ', d)
#
# # забираем с конца елемент и возвращает в виде кортежа ключ-значение
# print(d.popitem())
# print('d= ', d)

print('--------------')
d = {1: 3, 2: 4, 5: 2}
print('d= ', d)

d.update({4: 30})
print('d= ', d)

d1 = {55: 6, 45: 3}
d.update(d1)
print('d= ', d)
print('d val = ', d.values())
