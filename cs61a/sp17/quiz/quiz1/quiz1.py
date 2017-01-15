## Discussion Quiz 1 ##

isRaining = True
fallsBehind = False
doesProcrastinate = True
numExamsTaken = 45
addictedToCandy = False
will_ace_this_class = (not fallsBehind and not doesProcrastinate and numExamsTaken == 45 or isRaining) and not addictedToCandy

def hof8(input_fn):
    """Returns a version of the input function that trolls you upon every eighth call.
    
    >>> f = hof8(max)
    >>> f(1, 2) + f(f(f(f(f(f(3, 4), 5), 6), 7), 8), 9) # 7 calls
    11
    >>> f(10, 11) # 8th call
    gr8 m8 i r8 8/8
    11
    >>> f(12, 13) # 9th call; message should not be printed
    13
    """
    callCount = [0] # this is a list; update w/ callCount[0] = <whatever>
    def inner(*args):
        if (callCount[0] + 1) % 8 == 0:
            print('gr8 m8 i r8 8/8')
        callCount[0] = callCount[0] + 1
        return input_fn(*args)
    return inner
