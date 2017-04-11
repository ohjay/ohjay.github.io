---
category: stealth
title: Lab 11&#58; Streams, Sets, and Binary Trees
---

## Streams
### Big Ideas
- **streams** are lazily evaluated linked lists
- "lazily evaluated" means that values are not computed until you ask for them through `<stream>.rest`
- we make this work by computing the `rest` of a stream using a function
- once a value has been computed, it never needs to be computed again – it'll already be sitting there
- like linked lists, streams have a `first` and a `rest`
- like linked lists, there is a `Stream.empty` element

### Examples
- As a basic example, here is an endless stream of increasing integers.

  ```python
  def make_integer_stream(first=1):
      def compute_rest(): # should return a Stream, or Stream.empty if no more elements
          return make_integer_stream(first + 1) # make_integer_stream does indeed return a stream!
      return Stream(first, compute_rest)
  ```
  
  We can use it as follows:
  ```python
  >>> stream = make_integer_stream(3)
  >>> stream.first
  3
  >>> stream.rest
  Stream(4, <...>)
  >>> stream.rest.rest.first
  5
  >>> [eval('stream' + '.rest' * i + '.first') for i in range(10)]
  [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  ```

- Next, we have a look-and-say stream.

  ```python
  from itertools import groupby
  def make_look_and_say_stream(first=1):
      def compute_rest():
          second = int(''.join(str(len(list(group))) + num for num, group in groupby(str(first))))
          return make_look_and_say_stream(second)
      return Stream(first, compute_rest)
  ```
  
  ```python
  >>> stream = make_look_and_say_stream()
  >>> [eval('stream' + '.rest' * i + '.first') for i in range(5)]
  [1, 11, 21, 1211, 111221]
  ```

- Finally, a stream that filters another stream according to a predicate `pred`.

  ```python
  def filter_stream(stream, pred):
      if stream is Stream.empty:
          return stream
      elif pred(stream.first):
          return Stream(stream.first, lambda: filter_stream(stream.rest, pred))
      else:
          return filter_stream(stream.rest, pred)
  ```
  
  ```python
  >>> positive_ints = make_integer_stream()
  >>> odds = filter_stream(positive_ints, lambda x: x % 2) # false if x is even
  >>> [eval('odds' + '.rest' * i + '.first') for i in range(5)]
  [1, 3, 5, 7, 9]
  ```

### Other Notes
- we'll use streams in both Python and Scheme (they're not a language-specific concept)
- streams are to linked lists what iterators are to lists
- with lazy evaluation, we can represent infinite sequences; you've already seen this with iterators because they utilize lazy evaluation as well

## Sets
### Big Ideas
- **sets** are unordered collections with no duplicates
- think of a set as a big bucket of unique stuff
- if you try to throw a duplicate in, it just won't do anything to the set
- create a set with `{<elements>}` or `set(<iterable>)`, e.g. `{1, 2, 3}` or `set([1, 2, 3])`
- many operations are supported:
  - `add`, `remove`, `in`, `union` (`|`), `intersection` (`&`), `difference` (`-`)

### Example
```python
>>> s = {1, 1, 2, 2, 3, 3}
>>> t = {3, 4, 4}
>>> len(s) # duplicates are removed
3
>>> len(t)
2
>>> t.remove(4)
>>> 4 in t # Python doesn't care that we originally added two 4s
False
>>> t.add(4) # at this point, t is {3, 4} again
>>> s - t # equivalent to s.difference(t); everything in s that's not in t
{1, 2}
>>> t - s
{4}
>>> s | t # equivalent to s.union(t); everything in either s or t
{1, 2, 3, 4}
>>> s & t # equivalent to s.intersection(t); everything in BOTH s and t
{3}
>>> s & t | s - t | t - s
{1, 2, 3, 4}
>>> s & t | t - s
{3, 4}
```

### Other Notes
- you can play SET every day on [this website](https://www.nytimes.com/crosswords/game/set/?page=set&difficulty=&_r=0)

## Binary Trees
### Big Ideas
- **binary trees** are just trees, except every node can have at most two children
- each `BinTree` has a `label`, a `left`, and a `right`
- there is also `BinTree.empty`, which represents the empty tree

---

- **binary search trees** are binary trees that store data in a more organized way
- at each node in a binary search tree, we impose the following constraints:
  - everything in the `left` subtree must be _less than or equal to_ the node's `label`
  - everything in the `right` subtree must be _greater than or equal to_ the node's `label`
- this allows us to find things more efficiently; with a perfectly balanced tree we eliminate half of the search space upon every comparison
