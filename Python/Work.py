#  File: Work.py

#  Description: Program that uses binary and linear search to find the minumum
#  amount of lines Vyasa must first write and the time for each function run before he falls asleep

#  Student Name: Jiaxin Huang

#  Date Created: 02/22/2021

#  Date Last Modified: 02/25/2021

import sys

import time

import math
# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
  # Placeholder num for coffe and code_after_coffee that can be changed
  coffee = 0
  # Set sum to v for beginning of addition
  sum_value = v
  code_after_coffee = 1
  # Loop whenever user can still write code after coffee
  while code_after_coffee != 0:
      # Increment coffee everytime user drinks
      coffee += 1
      # Amount of code written after coffee drank
      code_after_coffee = v // k ** coffee
      #print(code_after_coffee)
      # Add code written before and after coffee drank
      sum_value += code_after_coffee 
  return sum_value

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
  # Create list of from 1 to total code
  code_lines = [i for i in range(1, n + 1)]
  # Loop through list sequentialy to check if total code calculated in sum_series == n
  for index in range(len(code_lines)):
    v = code_lines[index]
    if (sum_series(v, k) >= n):
      # Return code written before coffee drank
      return v
  


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
  # Create list from 1 to total code
  code_lines = [i for i in range(1, n + 1)]
  # Set the low and high index for list
  low = 0
  high = len(code_lines) - 1
  # Loop all the time if the code written before coffee drank is inside list
  # and the total value calculated by sum_series == n
  while low <= high:
    # Set the middle index and middle value of list
    middle = (low + high) // 2
    mid_value = code_lines[middle]
    # Check second half of list if assigned total is greater than calculated total 
    if (n > sum_series(mid_value, k)):
      low = middle + 1
    # Check first half of list if assigned total is greater than calculated total 
    elif (n < sum_series(mid_value, k)):
      if n > sum_series(mid_value - 1, k):
        return mid_value
      high = middle - 1
    # Return mid_value if the assigned total is equal to calculated total
    elif (n == sum_series(mid_value, k)):
      return mid_value


# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases
  assert sum_series(152, 2) == 300
  return "all test cases passed"

def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()
