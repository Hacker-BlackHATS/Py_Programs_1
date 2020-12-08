#!/bin/python3
"""
Given a chocolate bar, two children, Lily and Ron, are determining how to share it.
Each of the squares has an integer on it. Lily decides to share a contiguous segment
of the bar selected such that:
    The length of the segment matches Ron's birth month, and,
    The sum of the integers on the squares is equal to his birth day.

You must determine how many ways she can divide the chocolate.

Consider the chocolate bar as an array of squares, s = [2,2,1,3,2]. She wants to find segments
summing to Ron's birth day, d = 4 with a length equalling his birth month, m = 2.
In this case, there are two segments meeting her criteria: [2, 2] and [1, 3].

Complete the birthday function in the editor below.
It should return an integer denoting the number of ways Lily can divide the chocolate bar.
birthday has the following parameter(s):
    s: an array of integers, the numbers on each of the squares of chocolate
    d: an integer, Ron's birth day
    m: an integer, Ron's birth month
"""

import math
import os
import random
import re
import sys


def birthday(s, d, m):
    count = 0
    var = m
    i = 0
    while len(s) - i >= m:
        total = 0
        for j in s[i:var]:
            total += j
        if total == d:
            count += 1
        i += 1
        var += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    dm = input().rstrip().split()
    d = int(dm[0])
    m = int(dm[1])
    result = birthday(s, d, m)
    fptr.write(str(result) + '\n')
    fptr.close()
