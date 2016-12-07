# Notes from/for Today's Review Session
Big-O: it will grow no faster than `f(n)` for large `n`. Important for providing guarantees about efficiency. In 61A, we'll usually be concerned about the order of growth of running time.

### `mystery6` Commentary
If we switch the updates from the inner and the outer loop:

```python
def switched(n):
    while n > 1:
        x = n
        while x > 1:
            x -= 1
        n = n // 2
```

This is `O(n)` (not `O(nlogn)`) because the total amount of work done is approximately `n` + `n / 2` + `n / 4` + ... + `1`. Before this change, the total amount of work would be about `log(n)` + `log(n - 1)` + `log(n - 2)` + ... + `1` – which is of course different.

### `mystery9` Commentary
When calculating the order of growth, we're _always_ just summing up (_adding_) the amount of work done overall. Think 1 + 1 + 1 + 1, where the 1 represents every constant-time step we're taking. So when is this large enough to go to `n^2` instead of just `n`? When we're going to do `n` work an amount of times that depends on `n` (and NOT when we're going to do `n` work an amount of times that's upper bounded by a constant).
