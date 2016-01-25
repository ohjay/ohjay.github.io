# Discussion 1 Notes
Section 125 | Thursday, January 28 2016

## Attendance
Form to be found at this link: http://tiny.cc/discussion_one

## Public Service Announcement
FOLLOW THE RULES. 

Follow all of the evaluation rules mechanically. _Become_ Python Tutor. Forget your intuition; the one and only source of truth is The Interpreter itself. Blindly follow the rules as we've described them and try things out in said interpreter (you can start it up with `python3`). Eventually, true intuition will follow.

P.S. You don't have to think in code. You just have to translate _into_ code.

#### The Rules
Wake up every day and look at these rules!

##### Function Calls
1. Evaluate the operator, and then the operands (left to right).
2. Apply the operator to the operand values.
3. Create a new frame; bind the formal parameter names to the actual argument values.
4. Evaluate the body of the function in the context of this new frame.

##### Assignment
1. Evaluate all of the expressions on the right-hand side of the equals sign, from left to right.
2. Bind all of the names on the LHS to the resulting values, in the current frame.

##### Lookup
1. Look for the name in the current local frame.
2. If not found, go and look in the global frame. If it's not there, error.

## Control (30 minutes)
Control: deciding (in the program) what to do next, based on some state.

Data in boolean contexts: either truthy or falsy values.<br>
**False-y values**: 0, None, False, and empty stuff.<br>
**Truthy values**: everything else.

## Higher Order Functions (40 minutes)
Functions are data. What’s the difference between `square(4)` and `square`? `square(4)` is a function call, and `square` is the function itself. (Just another value.)

Reminder: evaluate the operator and then the operand(s) in order to properly evaluate a function call!

```python
def make_adder(n):
    def adder(x):
        return x + n
    return adder

make_adder(3)(4)
```

- Given this expression as a whole, what's the operator? (Answer: `make_adder(3)`)
- Given this expression as a whole, what's the operand? (Answer: `4`)

## Environment Diagrams (10 minutes)
Environment diagrams are important to understand. Not only because we put them on every test, but also because they basically have a one-to-one correspondence with your understanding of how programs are evaluated.

Go over an environment diagram for the following code segment:

```python
from operator import add

def sub(a, b):
    sub = add
    return a - b

add = sub
sub = min

print(add(2, sub(2, 3)))
```

Python Tutor's solution can be found [here](http://pythontutor.com/composingprograms.html#code=from+operator+import+add%0Adef+sub(a,+b)%3A%0A++++sub+%3D+add%0A++++return+a+-+b%0A++++%0Aadd+%3D+sub%0Asub+%3D+min%0A%0Aprint(add(2,+sub(2,+3)))&mode=display&origin=composingprograms.js&cumulative=true&py=3&rawInputLstJSON=%5B%5D&curInstr=0).

## Print vs. Return
What is a function? It's something that takes input and gives you output. The `return` _is that output_. Printing _is not_. It doesn't signify that the function is complete, and it's used only for displaying stuff. It's actually a function call in itself, one that always returns `None`.

Printing gives the value to the <u>user</u>. Returning gives the value to the <u>program</u>.

```python
def r(x):
    return x

def p(x):
    print(x)

4 + r(3) # gives you 7
4 + p(3) # error!
```

## Testing for Misconceptions
```python
>>> 3 + 4
7
>>> '3' + 4
Error
>>> '3 + 4'
'3 + 4'
>>> def boom(): # the body isn't evaluated
...   return 1 / 0
...
>>> boom()
Error
```

```python
>>> from operator import add
>>> def square(x):
...   return x * x
...
>>> def so_slow(num):
...   return num
...
>>> square(so_slow(5)) # return kicks you out of the fn
25
```

## Quine
[ Redacted for future semesters. ]
