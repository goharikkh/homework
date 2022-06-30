def remove_all(data, value):
    # remove_all(data, value) remove all the elements that are equal to value
    i = 0
    while i < len(data):
        if data[i] == value:
            data.remove(value)
        i += 1
    return lst


lst = [5, 2, 1, 7]
print(remove_all(lst, 5))
