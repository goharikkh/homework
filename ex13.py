def is_even(n):
    if n % 2 == 0:
        return True
    return False


def fast_pow(m, n):
    if n == 0:
        return 1
    if is_even(n):
        return fast_pow(m, n/2) * fast_pow(m, n/2)
    return m * fast_pow(m, n-1)


def fast_pow_iterative(m, n):
    count = 1
    if n == 0:
        return 1
    if is_even(n):
        while count < n / 2:
            m *= m
            count += 1
        return m * m
    while count < (n - 1) / 2:
        m *= m
        count += 1
        return m * m * m


print(fast_pow_iterative(2, 4))
