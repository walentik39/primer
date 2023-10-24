#!/usr/bin/env python3

import os
import fnmatch

for fname in os.listdir('.'):
    if fnmatch.fnmatch(fname, '*.py'):
        print(fname)

