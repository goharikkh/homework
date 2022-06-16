def min(data):
    '''min(data) return minimum value of the data'''
    i = 1
    min = data[0]
    while i < len(data):
        if data[i] < min:
            min = data[i]
        i +=1
    return min

data = [1,7,8,-1]
print(min(data))