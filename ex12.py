def pascal(row, pos):
    if pos in (1, row):
        return 1
    return pascal(row - 1, pos) + pascal(row - 1, pos - 1)


print(pascal(5, 4))