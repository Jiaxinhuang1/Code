#  File: InterestingDrink.py

#  Description: Implement find_purchase_options function that given a list of integers named prices that contains
#               the price of coffee in each store, and a list of integers named money that contains the amount of money
#               Peter will spend in a given day, returns a list of integers representing how many different shops
#               Peter can buy a cup of coffee.

#  Student Name: Jiaxin Huang

import sys


# Input: prices a list of integers containing the price of coffee in each store
#        money  a list of integers containing the amount of money Peter will spend in a given day
# Returns: a list of integers representing how many different shops Peter can buy a cup of coffee.

"""
Test Input:
3 10 8 6 11
1 10 3 11

Test Output:
Result by calling find_purchase_option [0, 4, 1, 5]

Test Input 2:
868 987 714 168 123
424 192 795 873 117 914 735 158 631 471

Test Output 2:
Result by calling find_purchase_option [2, 2, 3, 4, 0, 4, 3, 1, 2, 2]
"""
def find_purchase_options(prices, money):
    # TODO: write your code below.
    # create list of 0s for each day
    result = [0] * len(money)
    # add one to list if money during that day is more than prices of coffee
    for per_day in range(len(money)):
        for coffee in range(len(prices)):
            if(money[per_day] >= prices[coffee]):
                result[per_day] += 1
    return result
  

#######################################################################################################
# No need to change the main()
# The input format the the main is two lines, each line contains some integers split by a single space.
# For example:
# 3 10 8 6 11
# 1 10 3 11
#######################################################################################################
def main():
    # Read the prices list
    prices = [*map(int, sys.stdin.readline().split())]
    # Read the money list
    money = [*map(int, sys.stdin.readline().split())]
    # print the answer
    ans = find_purchase_options(prices, money)
    sys.stdout.write(f'Result by calling find_purchase_option {ans}')


if __name__ == '__main__':
    main()
