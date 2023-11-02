"""
Plus Minus

💛 문제
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, 
though answers with absolute error of up to  are acceptable.

Function Description
Complete the plusMinus function in the editor below.
plusMinus has the following parameter(s):
int arr[n]: an array of integers

💚 입출력
Sample Input
STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

Output
0.500000
0.333333
0.166667
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    posi = 0
    nega = 0
    zero = 0
    n = len(arr)
    
    for i in range(len(arr)) :
        if arr[i] > 0 :
            posi += 1
        elif arr[i] < 0 :
            nega += 1
        else :
            zero += 1
            
    print(posi/n)
    print(nega/n)
    print(zero/n)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
