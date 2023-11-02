"""
Diagonal Difference

💛 문제
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix  is shown below:
1 2 3
4 5 6
9 8 9  

The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .
Function description
Complete the  function in the editor below.
diagonalDifference takes the following

parameter:
int arr[n][m]: an array of integers
Return
int: the absolute diagonal difference

💚 입출력
Sample Input
3
11 2 4
4 5 6
10 8 -12

Output
15
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sum1 = 0
    sum2 = 0
    
    # [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    for i in range(len(arr)) :
        sum1 += arr[i][i]
        sum2 += arr[i][len(arr)- 1 - i]
    return abs(sum1 - sum2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
