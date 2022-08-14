# # --------- while ------------
#
# counter = 5
# while counter > 0:
#     print("iteration, counter =", counter)
#     counter = counter - 1
#
# print('---------------')
# print(counter)


# --------- for ------------
# for number in range(5):
#     print("iteration, number =", number)
#     print(number)

# print('---------------')
#
# for element in range(5):
#     if element == 3:
#         continue
#     print(element)
#
# print('---------------')
#
# for element in range(5):
#     if element == 1:
#         break
#     print(element)

print('---------------')

for num in range(102):
    if num % 2 == 0:
        print(num)

print('---------------')

words = 'hello'
words_res = ''
for char in words.lower():
    words_res += 's' if char == 'l' else char

print(words_res)

print('------ V1 ---------')

num_res = 0
for num_dev in range(100):
    if num_dev % 5 == 0:
        num_res = num_dev

print(num_res)

print('------ V2 ---------')
num_dev2 = 99
while num_dev2 >= 0:
    if num_dev2 % 5 == 0:
        print(num_dev2)
        break
    num_dev2 -= 1
