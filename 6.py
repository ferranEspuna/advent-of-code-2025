import sys

def operate(operation):
    python_form = (' ' + operation[-1] + ' ').join(operation[: -1])
    return eval(python_form)

 
if __name__ == "__main__":
    lists = map(lambda x: x.split(' '), (map(str.rstrip, sys.stdin)))
    filtered = (filter( lambda x: x != '', map(str.strip, l)) for l in lists)
    operations = list(zip(* filtered))
    print(sum(map(operate, operations)))

