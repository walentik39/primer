#!/usr/bin/env python3

import random
import time
for i in range(12):
    r = random.sample(range(500), 7)
    time.sleep(0.5)
    print(sorted(r, reverse=True))
