def contain(data, val):
    # contain(data, val) returns true if data contain val else it returns false
    i = 0
    while i < len(data):
        if data[i] == val:
            return True
        i += 1
    return False


lst = [5, 2, 1, 7]
print(contain(lst, 2))
