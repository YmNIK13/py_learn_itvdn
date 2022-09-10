pass  # =============  МНОЖЕСТВО [SETS] =====================
print('----- clear ---------')
a = {5, 1, 2, 2, 3, 3, 3, 4, 4, 4}
b = a.copy()
print('SET a -', a)
a.clear()
print('SET a -', a)
print('SET b -', b)

print('----- pop ---------')

a = b.copy()
print('SET a -', a)
a.pop()
print('SET a -', a)

print('------ remove/discard --------')
a = {1, 2, 3}
a.remove(1)
# a.remove(4)
a.discard(4)
print(a)

print('----- add ---------')
a = {1, 3, 5, 2}
print(a)
a.add(6)
print(a)
a.add(3)
print(a)

print('------  объединение --------')
a = {1, 2, 3}
b = {4, 5, 6}
print(a.union(b))
print('a=', a, 'b=', b)

print('------ пересечение --------')
a = {1, 2, 3}
b = {3, 4, 5, 6}
print('пересечение -', a.intersection(b))
print('a=', a, 'b=', b)
print('пересечение обновление -', a.intersection_update(b))
print('a=', a, 'b=', b)

print('------ разница --------')
a = {1, 2, 3, 4}
b = {3, 4}
print('a=', a, 'b=', b)
print('разница b in a -', a.difference(b), ' len=', len(a.difference(b)))
print('разница a in b -', b.difference(a), ' len=', len(b.difference(a)))
print('a=', a, 'b=', b)
print('разница обновление -', a.difference_update(b))
print('a=', a, 'b=', b)

a = {1, 2, 3, 4}
print('a=', a, '2 in a ->', 2 in a)
print('a=', a, '10 in a ->', 10 in a)
a.add(10)
print('a=', a, '10 in a ->', 10 in a)

b = [1, 2, 3, 4]
print('b=', b, '10 in b ->', 10 in b)
