## Discussion Quiz 6 ##

class Link:
    """A linked list, defined here for your convenience.

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

    def __len__(self):
        """Returns the number of items in the linked list.

        >>> s = Link(1, Link(2, Link(3)))
        >>> len(s)
        3
        >>> s = Link.empty
        >>> len(s)
        0
        """
        return 1 + len(self.rest)

    def __getitem__(self, i):
        """Returns the element found at index I.

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1]
        2
        >>> s[2]
        3
        """
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __setitem__(self, index, element):
        """Assigns ELEMENT to the value at the given index.

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1] = 5
        >>> s
        Link(1, Link(5, Link(3)))
        >>> s[4] = 5
        Traceback (most recent call last):
        ...
        IndexError
        """
        if index == 0:
            self.first = element
        elif self.rest is Link.empty:
            raise IndexError
        else:
            self.rest[index - 1] = element

    def __contains__(self, e):
        return self.first == e or e in self.rest

    def map(self, f):
        self.first = f(self.first)
        if self.rest is not Link.empty:
            self.rest.map(f)

def print_link(link):
    """Prints the elements of a linked list LINK.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> link1 = Link(1, Link(Link(2), Link(3)))
    >>> print_link(link1)
    <1 <2> 3>
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print_link(link1)
    <3 <4> 5 6>
    """
    print('<' + helper(link).rstrip() + '>')

def helper(link):
    if link == Link.empty:
        return ''
    elif isinstance(link.first, Link):
        return '<' + helper(link.first).rstrip() + '> ' + helper(link.rest)
    else:
        return str(link.first) +' '+  helper(link.rest)

# Q1: Linked List Basics
C = Link(1, Link(6))
C.rest.rest = Link(C.first, Link(C.rest.first))
S = C.rest.rest
C.rest.rest = C.rest.rest.rest
C.rest.rest.first = C.rest # try to never actually do this
C, C.rest.rest = S.rest.first, C

A = Link(0, Link(1, Link(2, Link(3))))
B = Link(A, Link(4, Link(6, Link(5))))
B.rest.rest.rest.rest = B.rest.rest
B.first.rest.rest.rest.rest = B.rest.rest

# Q2: Autocomplete
class Tree:
    def __init__(self, root=None, branches={}):
        self.root = root
        self.branches = branches
    
    def insert(self, chars, word):
        if len(chars) == 0:
            self.root = word
            return
        if chars[0] not in self.branches:
            self.branches[chars[0]] = Tree(None, {})
        self.branches[chars[0]].insert(chars[1:], word)
    
    def autocomplete(self, prefix):
        """Returns a list of full-word completions for the given prefix."""
        if len(prefix) == 0:
            return self.get_all_words()
        if prefix[0] not in self.branches:
            return []
        return self.branches[prefix[0]].autocomplete(prefix[1:])
    
    def get_all_words(self):
        """Returns all words contained within the current tree."""
        words = []
        if self.root is not None:
            words.append(self.root)
        for branch in self.branches.values():
            words += branch.get_all_words()
        return words
