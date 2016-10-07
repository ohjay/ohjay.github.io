# Discussion 5 Notes
Section 111 | Thursday, October 6 2016

## Announcements
Guerrilla section on order of growth, OOP, and inheritance this Saturday (12-3pm)<br>
Outstanding assignments: HW6, Lab 6, HW7, Ants<br>
Extra (past exam) problems are online. My thoughts are...<br>
Discussion attendance: http://tiny.cc/denero

## Quiz (Route Ciphers and T/F)
There is indeed a quiz today.

## OOP I: Basics / Terminology
- **Object-oriented programming** = a formalization of data abstraction; a more structured system for treating our data as objects. Translation: constructors --> constructors, selectors --> attributes
- **Class** = implementation-wise, it is the blueprint for your objects. Intuitively, it is the "type" of your objects. But it's still an abstraction (ex. "pizza" as in "what is a pizza?", or "student"). It's like seeing a word in a dictionary
- **Instance** = a specific manifestation of a class. Suddenly, your class is actually a thing (ex. "pizza" as in "check out my slice of pizza", or "Kavi, a student"). It's like finding an example of a dictionary definition in real life
- **Instance attribute** = a property that pertains to an INSTANCE (ex. "Kavi's age is 12"). Note that methods are attributes too; they're just attributes that are functions
- **Class attribute** = a property that pertains to a CLASS, i.e. something that applies to the type in general (ex. "pizza: `contains_dough = True`")
- **Method** = a function tied to (i.e. one that is called by) an instance of a class
- **Bound method** = a method that has already had an instance passed in as its first argument. Methods are only (/always) bound if the thing before the dot is an instance

---

Evaluation of dot expressions (`<expression> . <name>`):

1. Evaluate the expression on the left of the dot.
2. If the expression is an instance, try and match `<name>` to an instance attribute value.
3. If `<name>` doesn't match any instance attributes, match it to a class attribute value.
4. Return the value. If the value is a function and `<expression>` is an instance, return a bound method instead.

## OOP II: Inheritance
Inheritance is a way to model hierarchical relationships without rewriting a bunch of stuff. Basically, code is passed on from base classes to subclasses.

**Base class**: class that is being inherited from<br>
**Subclass**: class that is inheriting from the base class. Relationship between the two: a subclass _is a_ more specific version of the base class

Even if you put nothing inside of it, the subclass will have everything (even the constructor and the class attributes!) that the base class has. You can override specific attributes if you want.
