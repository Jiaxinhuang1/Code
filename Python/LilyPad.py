#  File: LilyPad.py

#  Description: Determines the distinct amount of ways Foo can get to the other side
#               of a pond with n lily pads by hopping either 1 or 2 lily pads at a time

#  Student Name: Jiaxin Huang

import sys

# Input: n is an int of how many lily pads there are
# Output: return an integer of how many distinct ways there are to cross the pond (order matters)
def distinct_ways(n):
    memo = [0, 1]
    # using fib memorization from class
    return fib_memo(n + 1, memo)

def fib_memo(n, memo):
    if (n == 0) or (n == 1):
        return memo[n]
    else:
        if(n >= len(memo)):
            f = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
            memo.append(f)
            return f
        else:
            return memo[n]

def main(): 
    # read number of lily pads
    n = int(input())

    # get the result from your call to distinct_ways()
    result = distinct_ways(n)

    # print the result to standard output
    print(result)

if __name__ == "__main__":
    main()