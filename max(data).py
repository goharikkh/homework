def max_(data):
    # max_(data) return the maximum value of the data
    i = 1
    max1 = data[0]
    while i < len(data):
        if data[i] > max1:
            max1 = data[i]
        i += 1
    return max1


data1 = [1, 7, 8, -1]
print(max_(data1))
