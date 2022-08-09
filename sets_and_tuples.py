pass  # =============  МНОЖЕСТВО [SETS] =====================
# a = {5, 1, 2, 2, 3, 3, 3, 4, 4, 4}
# print(a)
# a.clear()
# print(a)
#
# a = {4, 1, 2, 2, 3, 3, 3, 4, 4, 4}
# a.pop()
# print(a)

# print('--------------')
# a = {1, 2, 3}
# a.remove(1)
# # a.remove(4)
# a.discard(4)
# print(a)

# print('--------------')
# a = {1, 3, 5, 2}
# print(a)
# a.add(6)
# print(a)
# a.add(3)
# print(a)

# print('------  объединение --------')
# a = {1, 2, 3}
# b = {4, 5, 6}
# print(a.union(b))
# print('a=', a, 'b=', b)
#
# print('------ пересечение --------')
# a = {1, 2, 3}
# b = {3, 4, 5, 6}
# print('пересечение -', a.intersection(b))
# print('a=', a, 'b=', b)
# print('пересечение обновление -', a.intersection_update(b))
# print('a=', a, 'b=', b)

# print('------ разница --------')
# a = {1, 2, 3, 4}
# b = {3, 4}
# print('a=', a, 'b=', b)
# print('разница b in a -', a.difference(b))
# print('разница a in b -', b.difference(a))
# print('a=', a, 'b=', b)
# print('разница обновление -', a.difference_update(b))
# print('a=', a, 'b=', b)
#
# a = {1, 2, 3, 4}
# print('a=', a, '2 in a ->', 2 in a)
# print('a=', a, '10 in a ->', 10 in a)
# a.add(10)
# print('a=', a, '10 in a ->', 10 in a)
#
# b = [1, 2, 3, 4]
# print('b=', b, '10 in b ->', 10 in b)

pass  # =============  КАРТЕЖИ [TUPLES] =====================
a = (1, 2, 3, 4)
print(a)

a = (1, 2)
x, y = a
print('x=', x)
print('y=', y)
x, y = y, x
print('x=', x)
print('y=', y)

a = [(1, 2, 3), (4, 5, 6)]
for first, second, third in a:
    print(first, second, third)
