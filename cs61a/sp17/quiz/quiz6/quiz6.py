## Discussion Quiz 6 ##

class Foo:
    def __init__(self, n):
        self.n = n
        self.curr = 0
    def __next__(self):
        self.curr = (self.curr + 1) % self.n
        return self.curr
    def __iter__(self):
        return self
    
def fighters(m):
    print('a')
    it, x = Foo(4), 0
    while x < m:
        print('b')
        yield x
        print('c')
        x += next(iter(it))
