from itertools import count, islice
from collections import deque
import sys

def sliding_window(it, n):
    window = deque(islice(it, n - 1), maxlen=n)
    for x in it:
        window.append(x)
        yield tuple(window)

def accessible(top, x, bottom):
    n = len(x)
    for i, c in zip(count(start=1, step=1), x[1 : -1]):
        nearby_paper = sum(1 if row[i + dx] == '@' else 0 for dx in range(-1, 2) for row in (x, top, bottom))
        yield 'x' if nearby_paper < 5 and c == '@' else c

def accessible_row(top, x, bottom):
    return ''.join(accessible(top, x, bottom))

def update(it):
    triples = sliding_window(padded, 3)
    yield from map(lambda x: accessible_row(* x),  triples)

def pad(it):
    first = next(it)
    yield '.' * (len(first) + 2)
    yield '.' + first + '.'
    for x in it:
        yield '.' + x + '.'
    yield '.' * (len(first) + 2)

if __name__ == "__main__":
    inputs = map(str.rstrip, sys.stdin)
    padded = pad(inputs)
    print(sum(
        u.count('x') for u in update(padded)
    ))
