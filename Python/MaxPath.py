#  File: MaxPath.py

#  Description: Program that finds the maximum path sum using
#  brute force, greedy, divide and conquer, and dynamic programming 

#  Student Name: Jiaxin Huang

#  Date Created: 03/26/2021

#  Date Last Modified:  03/27/2021

import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search

def brute_force (grid):
  listed_sums = [] # stores sum for all the possible pathways
  # Call helper starting from top 
  brute_force_helper(grid, 0, 0, 0, listed_sums) 
  # Return the max sum from the list of sums
  maximum_path = max(listed_sums)
  return maximum_path

# Helper function that stores sum of every possible path in listed_sums
def brute_force_helper(grid, rows, cols, sums, listed_sums):
  # Add the path numbers to sum
  sums += grid[rows][cols]
  # Add the sum to listed_sum when added the number in last row
  if (rows == len(grid) - 1):
    listed_sums.append(sums)
  else:
    # Either add the number in right or number in left
    return (brute_force_helper(grid, rows + 1, cols, sums, listed_sums)
    or brute_force_helper(grid, rows + 1, cols + 1, sums, listed_sums))

# returns the greatest path sum using greedy approach
def greedy (grid):
  sums = grid[0][0] # Set the top value of the triange as sums
  row = 1 # Begin loop at the second row
  idx = 0 
  # Loop if the row is less than the amount of rows in grid 
  # and the column is less than column in the row
  while row < len(grid) and (idx < len(grid[row]) - 1):
    # If the right number is bigger, add the right number to sums
    # and increase the idx
    if (grid[row][idx] < grid[row][idx + 1]):
      sums += grid[row][idx + 1]
      idx += 1
    # If not, add the left column with same idx
    else:
      sums += grid[row][idx]
    row += 1 # Move to next row
  return sums
    
# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
  # Call helper function from top
  return divide_conquer_helper(grid, 0, 0)

def divide_conquer_helper(grid, row, col):
  # Separated base cases return if row index is equal to last row index in grid
  if row == len(grid) - 1:
    # return if reached end of grid
    return grid[row][col]
  else:
    # store the recursion in left and right so it does not have to be called again
    left_num = divide_conquer_helper(grid, row + 1, col)
    right_num = divide_conquer_helper(grid, row + 1, col + 1)
    # Add the greater sum of the recursion to the value
    if  left_num > right_num:
      return grid[row][col] + left_num
    else:
      return grid[row][col] + right_num

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  sum_grid = []
  # Create a list of 0s for sum
  for row in range(len(grid)):
    sum_grid.append([0 for num in range(row + 1)])
  
  # Loop through the new created list from bottom to top
  for row in range(len(sum_grid) - 1, -1, -1):
    for col in range(len(sum_grid[row])):
      # If the row is bottom, copy the bottom row of the grid to the new list
      if (row == len(sum_grid) - 1):
        sum_grid[row][col] = grid[row][col]
      # If it is not the bottom row
      else:
        # store the left and right numbers below the current row
        left_num = sum_grid[row + 1][col]
        right_num = sum_grid[row + 1][col + 1]
        # Add the bigger number (either right or left) to the current number
        # and place the sum on the position of the number added in the sum_grid
        if left_num > right_num:
          sum_grid[row][col] = grid[row][col] + left_num
        else:
          sum_grid[row][col] = grid[row][col] + right_num
  return sum_grid[0][0] # return the top number which is the max sum paath

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  '''
  # check that the grid was read in properly
  print (grid)
  '''

  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search
  print("The greatest path sum through exhaustive search is")
  print(str(brute_force(grid)))
  print("The time taken for exhaustive search in seconds is")
  print(times)
  print()
  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach
  print("The greatest path sum through greedy search is")
  print(str(greedy(grid)))
  print("The time taken for greedy search in seconds is")
  print(times)
  print()

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach
  print("The greatest path sum through recursive search is")
  print(str(divide_conquer(grid)))
  print("The time taken for recursive search in seconds is")
  print(times)
  print()

  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming
  print("The greatest path sum through dynamic programming is")
  print(str(dynamic_prog(grid)))
  print("The time taken for dynamic programming in seconds is")
  print(times)
  print()

if __name__ == "__main__":
  main()
