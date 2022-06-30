def is_even(n):
    if n % 2 == 0:
        return True
    return False


def double(num):
    return num * 2


def fast_mul(num1, num2):
    if num2 == 0:
        return 0
    if is_even(num2):
        return double(fast_mul(num1, num2 / 2))
    return num1 + fast_mul(num1, num2 - 1)


print(fast_mul(4, 5))
