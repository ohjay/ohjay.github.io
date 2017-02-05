## Discussion Quiz 3 ##

# Q1
def reverse(lst):
    if len(lst) <= 1:
        return lst
    return reverse(lst[1:]) + [lst[0]]

l = [1, [2, 3], 4]
rev = reverse(l)

# Q2
lst = [None for _ in range(10)]
for i in range(10):
    lst[i] = lambda: i

for func in lst:
    print(func())
