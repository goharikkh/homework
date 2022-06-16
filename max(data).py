def max(data):
    '''max(data) return the maximum value of the data'''
    i = 1
    max = data[0]
    while i < len(data):
        if data[i] > max:
            max = data[i]
        i +=1
    return max

data = [1,7,8,-1]
print(max(data))