#  File: CubeRoot.py

#  Description: Program that uses binary search to find cube root

#  Student Name: Jiaxin Huang

#  Date Created: 03/03/2021

import sys

#   Input: n is a floating point number
#   Output: returns the cube root of n for a given tolerance
def cube_root ( n ):
    neg = False
    if (n < 0):
        neg = True
    low = 0 
    high = n
    tolerance = 1.0e-6
    while neg == False:
        middle = (high + low) / 2
        if n > middle ** 3:
            low = middle
        elif n < middle ** 3:
            high = middle
        if abs((middle ** 3) - n) <= tolerance:
            return middle
    while neg == True:
        middle = (high + low) / 2
        if n > middle ** 3:
            high = middle
        elif n < middle ** 3:
            low = middle
        if abs((middle ** 3) - n) <= tolerance:
            return middle

def main():
    #  read n
    line = sys.stdin.readline()
    line = line.strip()
    n = float (line)

    # compute the cube root of n and print result
    print ( cube_root ( n ) )

if __name__ == "__main__":
    main()