import sys
from utils import print_output
from itertools import chain
from functools import reduce

def set_invalid_ids_same_digits(x, y, reps=2):
    
    x_str = str(x)
    y_str = str(y)

    assert len(x_str) == len(y_str)

    if x > y:
        return set()
    if len(x_str) % reps != 0:
        return set()
    
    n_digits = len(str(x))
    rep_n_digits = n_digits // reps

    x_start = int(str(x)[: rep_n_digits])
    y_start = int(str(y)[: rep_n_digits])

    first_rep = x_start + (1 if int(str(x_start) * reps) < x else 0)
    last_rep = y_start - (1 if int(str(y_start) * reps) > y else 0)

    return set( int(str(i) * reps) for i in range(first_rep, last_rep + 1) )

def set_invalid_ids(x, y, reps=2):
    start_digits = len(str(x))
    end_digits = len(str(y))

    start_reps = (set_invalid_ids_same_digits(x, min(10 ** start_digits - 1, y), reps=reps), )
    mid_reps = (set_invalid_ids_same_digits(10 ** (d - 1), 10 ** d - 1, reps=reps) for d in range(start_digits + 1, end_digits))
    end_reps = (set_invalid_ids_same_digits(max(10 ** (end_digits - 1), x), y, reps=reps), )
    return reduce(set.__or__, chain(start_reps , mid_reps, end_reps ))


def sum_all_invalid_ids(x, y, upto_reps=None):

    max_reps = upto_reps if upto_reps else len(str(y))
    all_reps = (set_invalid_ids(x, y, reps) for reps in range(2, max_reps + 1))
    return sum(reduce(set.__or__, all_reps))
    
if __name__ == "__main__":
    inputs = next(map(str.rstrip, sys.stdin)).split(',')
    parsed = list(map(lambda x: list(map(int, x.split('-'))), inputs))
    print(sum(map(lambda p: sum_all_invalid_ids(*p, upto_reps=2), parsed)))
    print(sum(map(lambda p: sum_all_invalid_ids(*p), parsed)))
