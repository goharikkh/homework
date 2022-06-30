def triple(n):
    # triple(n) multiplies by 3
    return n * 3


def map_(func, data):
    res = [None] * len(data)
    for i in range(len(data)):
        res[i] = func(data[i])
    return res


lst = [4, 15, 7, -1]
print(map_(triple, lst))


#######################################################


def sum_(a, b, c):
    return a + b + c


def map3(func, data1, data2, data3):
    res = [None] * len(data1)
    for i in range(len(data1)):
        res[i] = func(data1[i], data2[i], data3[i])
    return res


data1_ = [1, 2, 3]
data2_ = [10, 20, 30]
data3_ = [100, 200, 300]
print(map3(sum_, data1_, data2_, data3_))


############################################################
def pow_(base_, exp_):
    return base_ ** exp_


def map2(func, data1, data2):
    res = [None] * len(data1)
    for i in range(len(data1)):
        res[i] = func(data1[i], data2[i])
    return res


base = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
exp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(map2(pow_, base, exp))
