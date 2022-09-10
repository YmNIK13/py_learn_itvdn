# Найдите максимальное значение в передаваемом в функцию списке и верните его,
# если оно больше 0, в ином случае верните сообщение о том, что число меньше 0.
def max_val(arr):
    result = arr[0]
    for num in arr:
        if num > result:
            result = num

    return result if result > 0 else 'в списке нет чисел больше нуля'


print(max_val([1, 5, 8, 7, 89, 7, 0]))
print(max_val([-1, -5, -8, -7, -89, -7, 0]))
print('--------------')


def count_str(str):
    return len(str)


print(count_str("Пырышки пупырышки"))
print('--------------')


def power(num, step):
    return num ** step if step > 0 else None


print(power(2, 4))
print(power(2, -4))
