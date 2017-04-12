## Discussion Quiz 10 ##

class Stream:
    """A lazily evaluated linked list."""

    class empty:
        """The empty stream."""
        def __repr__(self):
            return 'Stream.empty'

    empty = empty()

    def __init__(self, first, compute_rest=empty):
        """A stream whose first element is FIRST and whose tail is either
        a stream or a stream-returning, parameterless function COMPUTE_REST."""
        self.first = first
        if compute_rest is Stream.empty or isinstance(compute_rest, Stream):
            self._rest, self._compute_rest = compute_rest, None
        else:
            assert callable(compute_rest), 'compute_rest must be callable'
            self._compute_rest = compute_rest

    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest

    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))

class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.first
    1
    >>> s.rest
    Link(2, Link(3))
    """
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

# Q1
def sweet(dreams):
    return Stream(Link(dreams), lambda: sweet(Link(dreams)))

def mix(tape):
    pre = match(lambda x: x.rest, tape.rest)
    temp = pre
    while temp.rest is not Link.empty:
        temp = temp.rest
    temp.rest = Link(tape.first.rest)
    return Stream(tape.first.first, lambda: mix(pre))

def match(dot, com):
    if com is Link.empty:
        return com
    return Link(dot(com.first), match(dot, com.rest))

s = mix(match(sweet, Link(1, Link(2, Link(3)))))

# Q2
class BinTree:
    empty = ()
    def __init__(self, label, left=empty, right=empty):
        self.label = label
        self.left = left
        self.right = right

    def __iter__(self):
        """Inorder traversal over the tree's elements.

        >>> bst = BinTree(5, BinTree(3, BinTree(2), BinTree(4)), BinTree(6))
        >>> list(bst)
        [2, 3, 4, 5, 6]
        >>> for thingy in bst: print(thingy)
        2
        3
        4
        5
        6
        """
        yield from self.left
        yield self.label
        yield from self.right
