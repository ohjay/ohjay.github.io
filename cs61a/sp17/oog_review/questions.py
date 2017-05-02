from math import sqrt
import random

# Question 0
# ----------

def mystery0(n):
    total = 0
    for i in range(n):
        total *= i
    for i in range(n // 2):
        total += i
    return total

# Individual Function Descriptions
# --------------------------------

def const(n):
    for _ in range(500):
        print('spam i am')

def log(n):
    if n <= 1:
        return 1
    return n * log(n // 2)

def lin(n):
    if n <= 1:
        return 1
    return n + lin(n - 1)

def quad(n):
    if n <= 1:
        return 1
    return lin(n) * quad(n - 1)

def exp(n):
    if n <= 1:
        return 1
    return exp(n - 1) * exp(n - 1)

def nlogn(n):
    for _ in range(n):
        _ = log(n)

# Questions 1 - 8
# ---------------

def mystery1(n):
    if n <= sqrt(abs(n)):
        return n
    return n + mystery1(n // 3)

def mystery2(n):
    while n > 1:
        x = n
        while x > 1:
            print(n, x)
            x = x // 2
        n -= 1

def mystery2f(n):
    while n > 1:
        x = n
        while x > 1:
            print(n, x)
            x -= 1
        n //= 2

def mystery3(n):
    result = 0
    for i in range(n // 10):
        result += 1
        for j in range(10):
            result += 1
            for k in range(10 // n):
                result += 1
    return result

def mystery4(n):
    total = 0
    for i in range(1, n):
        total *= 2
        if i % n == 0:
            total *= mystery4(n - 1)
            total *= mystery4(n - 2)
        elif i == n // 2:
            for j in range(1, n):
                total *= j
    return total

def mystery5(n):
    n, result = str(n), ''
    num_digits = len(n)
    for i in range(num_digits):
        result += n[num_digits - i - 1]
    return result

def mystery6(m, n):
    result = 0
    for i in range(1, m):
        j = i * i
        while j <= n:
            result, j = result + j, j + 1
    return result

def mystery7(n):
    if n < 1:
        return n
    def helper(n):
        i = 1
        while i < n:
            i *= 2
        return i
    return mystery7(n / 2) + mystery7(n / 2) + helper(n - 2)

def weighted_random_choice(lst):
    """Returns a random element from the list, where later-occurring elements
    are more likely to be selected.
    """
    temp = []
    for i in range(len(lst)):
        temp.extend([lst[i]] * (i + 1))
    return random.choice(temp)

# Summer 2013 MT2 | Q2
# --------------------

def fizzle(n):
    if n <= 0:
        return n
    elif n % 23 == 0:
        return n
    return fizzle(n - 1)

def boom(n):
    if n == 0:
        return 'BOOM!'
    return boom(n - 1)

def explode(n):
    if n == 0:
        return boom(n)
    i = 0
    while i < n:
        boom(n)
        i += 1
    return boom(n)

def dreams(n):
    if n <= 0:
        return n
    if n > 0:
        return n + dreams(n // 2)

# Spring 2014 MT2 | Q6
# --------------------

def umatches(S):
    result = set()
    for item in S:
        if item in result:
            result.remove(item)
        else:
            result.add(item)
    return result

# Summer 2015 MT2 | Q5(d)
# -----------------------

def append(link, value):
    """Mutates LINK by adding VALUE to the end of LINK."""
    if link.rest is Link.empty:
        link.rest = Link(value)
    else:
        append(link.rest, value)

def extend(link1, link2):
    """Mutates LINK_1 so that all elements of LINK_2
    are added to the end of LINK_1.
    """
    while link2 is not Link.empty:
        append(link1, link2.first)
        link2 = link2.rest

# Summer 2012 Final | Q2
# ----------------------

def collide(n):
    lst = []
    for i in range(n):
        lst.append(i)
    if n <= 1:
        return 1
    if n <= 50:
        return collide(n - 1) + collide(n - 2)
    elif n > 50:
        return collide(50) + collide(49)

def crash(n):
    if n < 1:
        return n
    return crash(n - 1) * n

def into_me(n):
    lst = []
    for i in range(n):
        lst.append(i)
    sum = 0
    for elem in lst:
        sum = sum + crash(n) + crash(n)
    return sum

# Spring 2014 Final | Q5(c)
# -------------------------

def a(m, n):
    for i in range(m):
        for j in range(n // 100):
            print('hi')

def b(m, n):
    for i in range(m // 3):
        print('hi')
    for j in range(n * 5):
        print('bye')

def d(m, n):
    for i in range(m):
        j = 0
        while j < i:
            j = j + 100

def f(m):
    i = 1
    while i < m:
        i = i * 2
    return i

# Link Class
# ----------

class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first, repr(self.rest))
