from functools import reduce
def count(s):
    return s
x = map(count, [6, 7, 8, 9, 10])
result = reduce(lambda a, b: a * b, x)
print(result)