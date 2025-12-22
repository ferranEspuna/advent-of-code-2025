from itertools import count, islice
from collections import deque
import sys

def sliding_window(li, n):
    if n > len(li):
        return iter([])
    for i in range(0, len(li) - n + 1):
        yield tuple(li[ i: i+n])

def accessible(top, x, bottom):
    n = len(x)
    for i, c in zip(count(start=1, step=1), x[1 : -1]):
        nearby_paper = sum(1 if row[i + dx] == '@' else 0 for dx in range(-1, 2) for row in (x, top, bottom))
        yield 'x' if nearby_paper < 5 and c == '@' else c

def accessible_row(top, x, bottom):
    return ''.join(accessible(top, x, bottom))

def update(li):
    triples = sliding_window(pad(li), 3)
    yield from map(lambda x: accessible_row(* x),  triples)

def reduce(li):

    current_xs = sum(row.count('x') for row in li)
    li_next = list(update(li))
    next_xs = sum(row.count('x') for row in li_next)
    if next_xs != current_xs:
        return reduce(li_next)
    else:
        return li_next

def pad(li):
    l = len(li[0])
    return ['.' * (l + 2)] + ['.' + x + '.' for x in li] + ['.' * (l + 2)]

if __name__ == "__main__":
    inputs = map(str.rstrip, sys.stdin)
    grid = list(inputs)

    print(sum(
        u.count('x') for u in update(grid)
    ))

    print(sum(
        u.count('x') for u in reduce(grid)
    ))

