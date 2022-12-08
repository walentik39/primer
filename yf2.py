#!/usr/bin/env python3

def subr(n):
    yield f"[{n}] One"
    yield f"[{n}] Two"
    return f"[{n}] Finish"

def task():
    for i in range(3):
        res = yield from subr(i)
        yield f"{i} {res}"
    return "@END@"    


core = task()
try:
    while True:
        print(next(core))
except StopIteration as exc:
    print(exc.value)

