def min_(data):
    # min(data) return minimum value of the data
    i = 1
    min1 = data[0]
    while i < len(data):
        if data[i] < min1:
            min1 = data[i]
        i += 1
    return min1


data1 = [1, 7, 8, -1]
print(min(data1))
