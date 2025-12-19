from itertools import chain
from functools import reduce
import sys

def zeros_between(x, y):
    if y == 0:
        return 0
    return (abs(y) - 1) // 100 + (1 if y < 0 and x != 0 else 0)

def rotate(start, rotation):

    x, curr_true_zeros, curr_passing_zeros = start
    moved = x + rotation
    result = moved % 100
    is_zero = 1 if result == 0 else 0
    n_new_passing_zeros = zeros_between(x, moved)
    return (result, curr_true_zeros + is_zero, curr_passing_zeros + n_new_passing_zeros)

def parse(step):
    return int(step[1:]) * (1 if step[0] == 'R' else -1)

if __name__ == "__main__":
    inputs = map(str.rstrip, sys.stdin)
    _, a, b = reduce(rotate, chain([(50, 0, 0)], map(parse, inputs)))
    print(a)
    print(a + b)
