#!/bin/python3
"""
We define a magic square to be an n x n matrix of distinct positive integers from 1 to n^2
where the sum of any row, column, or diagonal of length n is always equal to the same number:
the magic constant.

You will be given a 3 x 3 matrix s of integers in the inclusive range [1, 9]. We can convert
any digit a to any other digit b in the range [1, 9] at cost of |a - b|. Given s, convert it
into a magic square at minimal cost. Print this cost on a new line.
Note: The resulting magic square must contain distinct integers in the inclusive range [1, 9].

Complete the formingMagicSquare function in the editor below.
It should return an integer representing the minimal total cost of converting the input square
to a magic square.
formingMagicSquare has the following parameter(s):
    int s[3][3]: a 3 x 3 array of integers
"""
# import os


# def formingMagicSquare(s):
#     cost = 0
#     return cost
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     s = []
#     for _ in range(3):
#         s.append(list(map(int, input().rstrip().split())))
#     result = formingMagicSquare(s)
#     fptr.write(str(result) + '\n')
#     fptr.close()


L = [
    [5, 3, 4],
    [1, 5, 8],
    [6, 4, 2]
]
n = 3
i = 0
items_count = [0]*9
for j in range(n):
    print(L[i][j], end=" ")
    if j == n-1:
        i += 1
        while i < n:
            print(L[i][j], end=" "),
            i += 1
        i -= 1
        if i == n-1:
            j -= 1
            while j > -1:
                print(L[i][j], end=" "),
                j -= 1
        j = 0
        i -= 1
        while i > -1:
            print(L[i][j], end=" "),
            i -= 1
