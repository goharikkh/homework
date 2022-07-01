# 2
a = int(input('Enter the number '))


def baj(z):
    res_ = []
    for i in range(1, z // 2 + 1):
        if z % i == 0:
            res_.append(i)
    res_.append(z)
    return res_


print(baj(a))

# 3
a = int(input('Enter the number '))


def kat(x):
    s = 1
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            s += i
    return s == x


print(kat(a))


# 4
def zip_(data1, data2):
    lst = []
    for i in range(0, len(data1)):
        res1 = [data1[i], data2[i]]
        lst.append(res1)
    return lst


print(zip_([1, 2, 3], [2, 3, 4]))


# 5
def convert(string):
    li = list(string.split(' '))
    return li


def is_palindrome(str_):
    s = convert(str_)
    if s[::1] == s[::-1]:
        return True
    return False


str1 = str(input('Enter the sentence: '))
print(is_palindrome(str1))


# 7
def monoton(data):
    for i in range(0, len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True


n = int(input('Enter the number: '))
res = []
while n != 0:
    res.append(n)
    n = int(input('Enter the number: '))
print(res)

print(monoton(res))

# 8
