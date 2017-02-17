"""
Code for MT1 review worksheet.
Direct all complaints to Owen Jow (owenjow@berkeley).
"""

# Part 1: Control

x = (0 and 1 and 2) + (0 or 1 or 2)
((-4 or 0) and 4) / (-2 or (0 and 2))

if x <= 1:
    print('hello')
elif x <= 2:
    print(' world')
if x <= 3:
    print(' my name is inigo montoya')
else:
    print(' from the other side')

# Part 2: HOF / Lambdas

def f(v, x):
    def g(y, z):
        return y(x, z)(z, x)
    return g
u = lambda y, x: y * 4
v = lambda x, y: x * 3 + y
f(u, 1)(lambda x, y: lambda y, x: y * 3 + v(x, y), 2)

# Part 4: Environment Diagrams

def f(x, h):
    def g(y, i):
        f = i[:]
        h = [f, lambda: g(5, h)]
        return h
    return g(4, h)

x, y = 6, 7
f = f(3, [lambda: x * y])
g = f[-1]()[0][0][0]()
