"""
Simple Array Sum

💛 문제
Given an array of integers, find the sum of its elements.
For example, if the array , , so return .

Function Description
Complete the simpleArraySum function in the editor below. 
It must return the sum of the array elements as an integer.

simpleArraySum has the following parameter(s):

ar: an array of integers

💚 입출력
Sample Input
6
1 2 3 4 10 11

Sample Output
31
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    sum = 0
    for i in ar :
        sum += i
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
