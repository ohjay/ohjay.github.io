# Discussion 2 Notes
Section 125 | Thursday, February 3 2016

## Announcements
Useful CS 61A resource as a whole: tinyurl.com/61a-unstuck. Includes guides for a wide range of topics.

## Quiz (10 minutes)
Take the quiz. Hand it in. That is your attendance for the day!

## Environment Diagrams (30 minutes)
Print out a copy of the rules and give it to every student. Go over all of them. (These are **free points** once you understand environment diagrams! You just have to be careful.)

## Recursion (20 minutes)
What is recursion? Recursion means something that's defined in terms of itself, so in 61A we'll see it as functions that call themselves. All recursive functions break into three parts. What are those parts?

1. Base case(s)
2. Way(s) to solve the smaller problem recursively
3. Solving the original problem given the solution to the smaller problem

Example:
```python
def countup(n):
    if n == 0:
        return
    else:
        countup(n-1)
        print(n)
```

(After `countup` hits its base case, it will return to the previous call and evaluate `print(n)`... before continuing up the remainder of the stack.)

Go through an example that describes the call stack. Then go through a bunch more examples.

#### How to start
1. Figure out the base case. "What is the simplest input for which we immediately get an answer?"
2. Figure out how to work toward that base case.

## Tree Recursion (15 minutes)
The three "recursive parts" still apply! Past that, tree recursion often comes down to making a choice. You either go left or go up. You either take one stair or two. You either use the largest coin or you don't...

Essential: draw the call tree!

## Advice for Midterm Preparation (5 minutes)
Practice with a lot of environment diagrams. Go through past exams.
