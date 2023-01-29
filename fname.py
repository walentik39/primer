#!/usr/bin/env python3

import os
import fnmatch

for fname in os.listdir('.'):
    if fnmath.fnmatch(fname, '*.py'):
        print(fname)

