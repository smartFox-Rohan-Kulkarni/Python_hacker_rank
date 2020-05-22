#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    splitted = s.split(' ')
    sol = []
    space = ' '
    for w in splitted:
        sol.append(w.capitalize())
    return space.join(sol)

if __name__ == '__main__':
