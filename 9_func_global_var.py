# X = 1
# print(X)
#
#
# def f1():
#     X = 10
#     print("Increment X =", X + 1)
#
#
# f1()
# print(X)


def main():
    x = 10

    def internal():
        return 1

    internal_result = internal()
    return x + internal_result


m = main()
print(m)
