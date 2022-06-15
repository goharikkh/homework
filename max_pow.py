def max_pow(x,y,z):
    '''max_pow(x,y,z) returns the sum of the 2 biggest numbers square '''
    if x < y < z:
        return y**2 + z**2
    elif y < x < z:
        return x**2 + z**2
    else:
        return x**2 + y**2

print(max_pow(2,3,4))