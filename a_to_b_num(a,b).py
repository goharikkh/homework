def a_to_b_num(a,b):
    sum = 0
    if a > b:
        t=a
        a=b
        b=t
    while a < b-1:
        a += 1
        sum += a
    return sum

print(a_to_b_num(1,5))
