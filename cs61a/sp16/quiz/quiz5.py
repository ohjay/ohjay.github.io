## Tree ADT ##
def tree(label, children=[]):
    for child in children:
        assert is_tree(child), 'children must be trees'
    return [label] + list(children)

def label(tree):
    return tree[0]

def children(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for child in children(tree):
        if not is_tree(child):
            return False
    return True

def is_leaf(tree):
    return not children(tree)

def tree_path(t, num, directions):
    """Given a tree T that is filled with numbers, mutates DIRECTIONS
    so that it contains a path to NUM. DIRECTIONS is given as a
    list of child indices to follow.
    
    Note: If NUM is at the root (or NUM is not in the tree), 
    DIRECTIONS should be empty.
    
    >>> t = tree(1, [tree(2), \
                     tree(3, [tree(4, [tree(5)]), \
                              tree(6)]), \
                     tree(7, [tree(8)])])
    >>> directions = []
    >>> tree_path(t, 5, directions)
    >>> directions
    [1, 0, 0]
    >>> tree_path(t, 1, directions)
    >>> directions
    []
    """
    while directions:
        directions.pop()
    def helper(t):
        if label(t) == num:
            return True
        elif is_leaf(t):
            return False
        for i in range(len(children(t))):
            directions.append(i)
            if helper(children(t)[i]):
                return True
            else:
                directions.pop()
    helper(t)
