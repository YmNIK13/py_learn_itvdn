# product_price = 90
#
# if product_price > 600:
#     product_price *= 0.9
# elif product_price > 500:
#     product_price *= 0.95
# elif product_price > 100:
#     product_price *= 0.97
# else:
#     pass
#
# print(product_price)

################################
#
# value_str = "HEllo"
# print(None if value_str == "" else value_str)
# print(None if not value_str else value_str)

# ------------ Calc --------------

firs_value = 5
second_value = 0
operator = "/"
operator2 = "/"

if firs_value is None or second_value is None:
    print("Can't exist None value")
else:
    if operator == "+":
        print(firs_value + second_value)
    elif operator == "-":
        print(firs_value - second_value)
    elif operator == "/":
        if second_value == 0:
            print("Can't divide by '0'")
        else:
            print(firs_value / second_value)
    elif operator == "*":
        print(firs_value * second_value)
    else:
        print("Operator is wrong Choose from given: + - / *")
