#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the bigSorting function below.
def bigSorting(unsorted):
    unsorted.sort(key = lambda x:(len(x),x))
    return unsorted





n = int(input())

unsorted = []
for i in range(n):
    unsorted_item = input()
    unsorted.append(unsorted_item)

result = bigSorting(unsorted)
print(result)

