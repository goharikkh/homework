# recursive
def f(n):
    if n <= 3:
        return n
    return f(n-1) + f(n-2) + f(n-3)


# iterative
def iterative(n):
    num0, num1, num2 = 0, 1, 2
    if n < 3:
        return n
    while n > 0:
        num0 = num0 + num1 + num2
        num0, num1, num2 = num1, num2, num0
        n -= 1
    return num0


# tail
def tail(num, num1=1, num2=2, num3=3):
    if num == 1:
        return num1
    if num == 2:
        return num2
    if num == 3:
        return num3
    return tail(num - 1, num2, num3, num1 + num2 + num3)


print(f(11))
print(iterative(11))
print(tail(11))
