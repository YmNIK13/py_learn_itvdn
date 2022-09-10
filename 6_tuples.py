pass  # =============  КАРТЕЖИ [TUPLES] - неизменяемый список по сути ENUM =====================
a = (1, 2, 3, 4)
b = [1, 2, 3, 4]
# a[1] = 7 # error
b[1] = 7
print('tuple a[1]-', a[1])
print('tuple b[1]-', b[1])

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
