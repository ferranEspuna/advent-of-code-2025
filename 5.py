
import sys

def check(x, ranges):
    return any(a <= x <= b for a, b in ranges)

def interval_len(a, b):
    return b - a

def interval_presence(a, b, ranges):

    first_in = check(a, ranges)
    last_in = check(b, ranges)

    if first_in and last_in:
        return b - a
    if last_in:
        return 1
    return 0

def total_interval_length(ranges):
    ids_to_check = sorted(list(set([a - 1 for a, b in ranges] + [a for a, b in ranges] + [a + 1 for a, b in ranges] + [b - 1 for a, b in ranges] + [b for a, b in ranges] + [b + 1 for a, b in ranges])))
    startings = ids_to_check[: -1]
    endings = ids_to_check[1 :]
    return sum(interval_presence(u, v, ranges) for u, v in zip(startings, endings))

if __name__ == "__main__":
    inputs = list(map(str.rstrip, sys.stdin))

    ranges_st = []
    ids_st = []

    for i, x in enumerate(inputs):
        if not x:
            ranges_st = inputs[: i]
            ids_st = inputs[i + 1 :]
            break

    ranges = [tuple(map(int, range_st.split('-'))) for range_st in ranges_st]
    ids = list(map(int, ids_st))

    print(sum((1 if check(x, ranges) else 0 for x in ids)))
    print(total_interval_length(ranges))
