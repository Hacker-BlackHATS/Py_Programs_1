"""
A teacher asks the class to open their books to a page number. A student can either start
turning pages from the front of the book or from the back of the book. They always turn pages
one at a time. When they open the book, page 1 is always on the right side.
When they flip page 1, they see pages 2 and 3. Each page except the last page will always be
printed on both sides. The last page may only be printed on the front, given the length of the
book. If the book is n pages long, and a student wants to turn to page p, what is the minimum
number of pages to turn? They can start at the beginning or the end of the book.
Given n and p, find and print the minimum number of pages that must be turned in order to
arrive at page p.

Complete the pageCount function in the editor below.
It should return an integer representing the minimum number of pages to turn.
pageCount has the following parameter(s):
    int n: the number of pages in the book
    int p: the page number to turn to
"""

#!/bin/python3

import os


def pageCount(n, p):
    if p == 1 or p == n or (n % 2 != 0 and p == n-1):
        return 0
    else:
        min_page = 1
        a = 2
        ini = 1
        if n % 2 == 0:
            end = n
        else:
            end = n - 1
        while (ini + a) < p < (end - a):
            ini += a
            end -= a
            min_page += 1
        return min_page


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    p = int(input())
    result = pageCount(n, p)
    fptr.write(str(result) + '\n')
    fptr.close()
