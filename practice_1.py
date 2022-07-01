import math

# 1
print('Gohar Khachatryan')

# 2
name = input('what is your name?')
print('Hello', name + '!')

# 3
length = float(input('Enter the length of the room'))
width = float(input('Enter the width of the room'))
s = length * width
print('S = ', s, 'm^2')

# 4
length = float(input('Enter the length of the land'))
width = float(input('Enter the width of the land'))
s = (length * width) / 43560
print('S = ', s, 'akr')


# 5


def bottle(a, b):
    return float(a) * 0.10 + float(b) * 0.25


# 6
m = input('how much money order cost?')


def tip(a):
    return float(a) * 0.18


def tax(a):
    return float(tip(a)) * 0.2


print(f'Tips {tip(m):.2f}$')
print(f'Taxes {tax(m):.2f}$')
print(f'Total {tip(m) + tax(m):.2f}$')


# 7
def sum1_a(n):
    s = 1
    for i in range(2, n):
        s += i
    return s


# 8
def bottle(x, y):
    return x * 112 + y * 75


# 9
i = 0.04
A = input('Enter the input money')

for t in range(1, 4):
    print('A = ', float(A) * (1 + i * float(t)))

# 10
a = float(input("Enter the number"))
b = float(input("Enter the number"))

print("a + b = ", a + b)
print("a - b = ", a - b)
print("a / b = ", a / b)
print("a // b = ", a // b)
print("a % b = ", a % b)
print("lna = ", math.log10(a))

# 11
mpg = float(input('input MPG '))
print(f'L/100km = {235.215 / mpg :.2f}')

# 13
hight_f = float(input(f'hight in feets '))
hight_i = float(input(f'hight in inches '))
print(f'hight in cm {(hight_f * 12 + hight_i) * 2.154}')

# 14
r = input('Enter the radius of the circle ')


def circle_area(x):
    return math.pi * (x ** 2)


def sphere_volume(y):
    return 4.0 / 3.0 * (math.pi * (y ** 3))


print("area = ", circle_area(float(r)))
print("volume = ", sphere_volume(float(r)))


# 15
def cylinder_vol(r, h):
    return math.pi * r ** 2 * h


# 16
def velocity(h):
    g = 9.8
    return math.sqrt(2 * g * h)


hight = float(input('enter hight = '))
print(f'velocity is {velocity(hight):.2f}')


# 17
def triangle_area(b, h):
    return (float(b) * float(h)) / 2


# 18
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


# 19
day = int(input('enter days = '))
hour = int(input('enter hours = '))
minuit = int(input('enter minuits = '))
second = int(input('enter seconds = '))
print(f'timeframe in seconds {day * 86400 + hour * 3600 + minuit * 60 + second}')

# 20
import time

print(time.asctime())


# 21

# 22
def sonant_vowel(letter):
    if letter == 'y':
        print('sonant and vowel')
    elif letter in ('a', 'e', 'i', 'o', 'u'):
        print('vowel')
    else:
        print('sonant')


# 26
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    print(i)
