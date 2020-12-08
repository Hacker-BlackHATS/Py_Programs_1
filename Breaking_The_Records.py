#!/bin/python3
"""
Maria plays college basketball and wants to go pro.
Each season she maintains a record of her play.
She tabulates the number of times she breaks her season record for most points
and least points in a game. Points scored in the first game establish her record
for the season, and she begins counting from there.

Complete the breakingRecords function in the editor below.
It must return an integer array containing the numbers of times she broke her records.
Index 0 is for breaking most points records, and index 1 is for breaking least points records.
breakingRecords has the following parameter(s):
    scores: an array of integers
"""

import os


def breakingRecords(scores):
    season_result_count = [0, 0]  # 0 = breaking most points records
    # 1 = breaking least points records
    min_point = max_point = scores[0]
    for i in scores:
        if i > max_point:
            season_result_count[0] += 1
            max_point = i
        elif i < min_point:
            season_result_count[1] += 1
            min_point = i
    return season_result_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
