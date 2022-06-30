def pop(i, data):
    # pop(i, date) returns data without last element if i = None else returns i-rd element of data
    if i is None:
        n = len(data) - 1
        data.remove(data[n])
        return data
    return data[i]


data1 = [1, 5, 7, 8]
print(pop(None, data1))
