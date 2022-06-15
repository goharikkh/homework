def pow(base, exp):
    '''pow_base(base, exp) returns base ** exp'''
    if exp == 0:
        return 1
    elif exp > 0:
        res = 1
        count = 0
        while count < exp:
            res *= base
            count += 1
        return res
    else:
        return 1/pow(base, -exp)

print(pow(5,-3))