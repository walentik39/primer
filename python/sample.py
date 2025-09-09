#!/usr/bin/env python3

import random
import time
for i in range(12):
    r = random.sample(range(500), 7)
    time.sleep(0.5)
    #print(sorted(r, reverse=True))
    random.shuffle(r)
    print(r)
    r_new = (sorted(r, reverse=False))
    print(r_new)
    #print(sorted(r, reverse=False))
