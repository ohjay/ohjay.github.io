from math import sqrt
import random

# An Example [Summer 2012 Final | Q2(c)]
# --------------------------------------

def carpe_noctem(n):
    if n <= 1:
        return n
    return carpe_noctem(n - 1) + carpe_noctem(n - 2)

def yolo(n):
    if n <= 1:
        return 5
    sum = 0
    for i in range(n):
        sum += carpe_noctem(n)
    return sum + yolo(n - 1)

# Individual Function Descriptions
# --------------------------------

def const(n):
    n = 902 + 54
    return 'hamburger'

def loga(n):
    if n <= 1:
        return 1
    return n * loga(n // 2)

def sqroot(n):
    lim = int(sqrt(n))
    for i in range(lim):
        n += 45
    return n

def lin(n):
    if n <= 1:
        return 1
    return n + lin(n - 1)

def quad(n):
    if n <= 1:
        return 1
    r = lin(n) * quad(n - 1)
    return r

def expo(n):
    if n <= 1:
        return 1
    r1 = expo(n - 1) + 1
    r2 = expo(n - 1) + 2
    return r1 * r2

# Exercise 1
# ----------

def mystery1(n):
    n, result = str(n), ''
    num_digits = len(n)
    for i in range(num_digits):
        result += n[num_digits - i - 1]
    return result

def mystery2(n):
    n, result = 5, 0
    while n <= 3000:
        result += mystery1(n // 2)
        n += 1
    return result

# Exercise 2
# ----------

def mystery3(n):
    if n < 0 or n <= sqrt(n):
        return n
    return n + mystery3(n // 3)

def mystery4(n):
    if sqrt(n) <= 50:
        return 1
    return n * mystery4(n // 2)
    
def mystery5(n):
    for _ in range(int(sqrt(n))):
        n = 1 + 1
    return n

# Exercise 3
# ----------

def mystery6(n):
    while n > 1:
        x = n
        while x > 1:
            print(n, x)
            x = x // 2
        n -= 1

def mystery7(n):
    result = 0
    for i in range(n // 10):
        result += 1
        for j in range(10):
            result += 1
            for k in range(10 // n):
                result += 1
    return result

# Exercise 4
# ----------

def mystery8(n):
    if n == 0:
        return ''
    result, stringified = '', str(n)
    for digit in stringified:
        for _ in range(n):
            result += digit
    result += mystery8(n - 1)
    return result

def mystery9(n):
    total = 0
    for i in range(1, n):
        total *= 2
        if i % n == 0:
            total *= mystery9(n - 1)
            total *= mystery9(n - 2)
        elif i == n // 2:
            for j in range(1, n):
                total *= j
    return total

# Exercise 5
# ----------

def mystery10(n):
    if n > 0:
        r1 = mystery10(-n)
        r2 = mystery10(n - 1)
        return r1 + r2
    return 1

def mystery11(n):
    if n < 1:
        return n
    def mystery12(n):
        i = 1
        while i < n:
            i *= 2
        return i
    return mystery11(n / 2) + mystery11(n / 2) + mystery12(n - 2)

# Exercise 6
# ----------

def mystery13(m, n):
    if n <= 1:
        return 0
    result = 0
    for i in range(3 ** m):
        result += i // n
    return result + mystery13(m - 5, n // 3)

def mystery14(m, n):
    result = 0
    for i in range(1, m):
        j = i * i
        while j <= n:
            result += j
            j += 1
        return result

# Exercise 7
# ----------

def weighted_random_choice(lst):
    """Returns a random element from the list, where later-occurring elements
    are more likely to be selected.
    """
    temp = []
    for i in range(len(lst)):
        temp.extend([lst[i]] * (i + 1))
    return random.choice(temp)

# Exercise 8
# ----------

def index_exists(A):
    def helper(lower, upper):
        if lower >= upper:
            return A[upper] == upper
        mid_idx = (lower + upper) // 2
        if A[mid_idx] == mid_idx:
            return True
        elif A[mid_idx] > mid_idx:
            return helper(lower, mid_idx - 1)
        else:
            return helper(mid_idx + 1, upper)
    return helper(0, len(A) - 1)

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
