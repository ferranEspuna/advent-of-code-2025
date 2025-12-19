import sys 
from functools import reduce

def first_max_char(s):
    return max((c, -i, i) for i, c in enumerate(s))

def max_substring(s, n):
    if n == 0:
        return ''
    c, _, i = first_max_char(s[: len(s) - n + 1])
    return c + max_substring(s[i+1 :], n - 1)

def sum_tuple(x, y):
    return tuple(a + b for a, b in zip(x, y))


if __name__ == "__main__":
    inputs = map(str.rstrip, sys.stdin)
    part1, part2 = reduce(
        sum_tuple,
        map(
            lambda x: (int(max_substring(x, 2)), int(max_substring(x, 12))),
            inputs
        )
    )
    print(part1)
    print(part2)
