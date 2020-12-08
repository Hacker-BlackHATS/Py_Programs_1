"""
You have been asked to help study the population of birds migrating across the continent.
Each type of bird you are interested in will be identified by an integer value.
Each time a particular kind of bird is spotted, its id number will be added to your array
of sightings. You would like to be able to find out which type of bird is most common given
a list of sightings. Your task is to print the type number of that bird and if two or more
types of birds are equally common, choose the type with the smallest ID number.

Complete the migratoryBirds function in the editor below.
It should return the lowest type number of the most frequently sighted bird.
migratoryBirds has the following parameter(s):
    arr: an array of integers representing types of birds sighted
"""
#!/bin/python3

import math
import os
import random
import re
import sys


def migratoryBirds(arr):
    bird_sightings_count = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
    for i in arr:
        bird_sightings_count[str(i)] += 1
    max_value = bird_sightings_count["1"]
    max_type = "1"
    for i in bird_sightings_count.keys():
        if max_value < bird_sightings_count[i]:
            max_value = bird_sightings_count[i]
            max_type = i
    return max_type


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
