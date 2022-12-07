#!/usr/bin/env python3

class CM:
    def __init__(self, val = None):
        self.val = val


    def __enter__(self):
        print(">>>")


    def __exit__(self, *args):
        print("<<<",*(c for c in args if c), sep="/", end=">>>\n")
        return self.val

with CM(True) as f:
    print("Working")
    raise SyntaxError("What?")

print("Done")
