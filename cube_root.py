

def guess_enough(root, target):
    if abs(root**3 - target) < 0.0001:
        return True
    else:
        return False

def improve(root, target):
    return ((target / (root ** 2)) + (2 * root))/3

def cube_root(n):
    root = 1
    while not guess_enough(root, n):
        root = improve(root, n)
    return root

print(cube_root(5))


