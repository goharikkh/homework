import math


# 1
def reverse_num(a):
    s = 0
    while a != 0:
        s = s * 10 + a % 10
        a //= 10
    return s


print(reverse_num(123))


# 2
def tup_to_num(data):
    s = 0
    for i in data:
        s = s * 10 + i
    return s


print(tup_to_num((1, 2, 3)))


# 3
def sum_of_min_max(data):
    max_ = min_ = data[0]
    for i in data:
        if i > max_:
            max_ = i
        elif i < min_:
            min_ = i
    return min_ + max_


print(sum_of_min_max([1, 2, 3, 5]))


# 4
def even_num_index(data):
    for i in range(len(data)):
        if data[i] % 2 == 0:
            print(i)
    return None


print(even_num_index((1, 4, 18, 25, 28, 30, 127)))


# 5
def reverse_string(str1):
    res = ''
    for char in str1:
        res = char + res
    return res


print(reverse_string('Goharik'))


# 6
def is_prime(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True


def smallest_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n


print(smallest_prime(23))


# 7
def get_median(data):
    data.sort()
    if len(data) % 2 != 0:
        return data[len(data) // 2]
    else:
        return (data[int(len(data) / 2)] + data[int(len(data) / 2 - 1)]) / 2


print(get_median([1, 2, 5, 4, 6, 8]))


# 8
def month_days(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        if year % 4 == 0:
            return 29
        return 28
    return 30


print(month_days(3, 2000))


# 10
def same_parity(n, *args):
    res = []
    for i in args:
        if i % n == 0:
            res.append(i)
    return res


print(same_parity(10, 100, 25, 78, 500))
