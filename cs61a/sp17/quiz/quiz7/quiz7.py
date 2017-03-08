## Discussion Quiz 7 ##

def f0(n):
    while n > 0:
        print('print(print(None)))')
        n -= 1

def f1(n):
    while n > 0:
        print('make')
        n -= 2

def f2(n):
    while n > 0:
        print('lemonade')
        n //= 2

def all_paths(tree):
    if tree.is_leaf():
        return [[tree.label]]
    result = []
    for branch in tree.branches:
        result += [[tree.label] + path for path in all_paths(branch)]
    return result
