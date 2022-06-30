def reverse(data):
    # reverse(data) function returns reversed list
    j = len(data) - 1
    i = 0
    while i < j:
        t = data[i]
        data[i] = data[j]
        data[j] = t
        i += 1
        j -= 1
    return data


lst = [1, 2, 3, 4, 5]
print(reverse(lst))
