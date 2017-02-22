## Discussion Quiz 5 ##

# Q1
class LoopList:
    """
    >>> x = LoopList([3, 1, 4])
    >>> [x.at_index(i) for i in range(10)]  # loops around!
    [3, 1, 4, 3, 1, 4, 3, 1, 4, 3]
    """
    def __init__(self, lst):
        self.lst = lst
    
    def at_index(self, i):
        return self.lst[i % len(self.lst)]

# Q2
def campa(nile):
    def ding(ding):
        nonlocal nile
        def nile(ring):
            return ding
    return nile(ding(1914)) + nile(1917)

ring = campa(lambda nile: 100)
