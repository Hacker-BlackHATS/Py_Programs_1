#!/bin/python3
"""
You are given an array of n integers, ar = [ar[0], ar[1],...., ar[n - 1]], and a positive
integer, k. Find and print the number of (i, j) pairs where i < j and ar[i] + ar[j]
is divisible by k.

Complete the divisibleSumPairs function in the editor below.
It should return the integer count of pairs meeting the criteria.
divisibleSumPairs has the following parameter(s):
    n: the integer length of array ar
    ar: an array of integers
    k: the integer to divide the pair sum by
"""
import os


def divisibleSumPairs(n, k, ar):
    pair_count = 0
    i = 0
    while n - i >= 2:
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                pair_count += 1
        i += 1
    return pair_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    ar = list(map(int, input().rstrip().split()))
    result = divisibleSumPairs(n, k, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
