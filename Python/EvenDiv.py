#  File: EvenDiv.py

#  Description: Program that finds the minimum absolute value of the difference
# between two separated sublists.

#  Student Name:  Jiaxin Huang

#  Date Created:  04/01/2021

#  Date Last Modified:  04/01/2021

# Input: a is a list of positive integers. 2 < len(a) < 20

# Output: divide the list a into two sub-lists. Get the sum of the two sub-lists. 

# Get the absolute value of the difference between the two sums.

# Return the minimum absolute value difference between the sums of the two sub-lists.
import sys

"""
Test Input:
4 9 1 5

Test Output:
1

Test Input 2:
9999999 1 2

Test Output 2:
9999996

"""
def even_div ( a ):
  # crete empty list to store all the differences like brute force approach
  diff_list = []
  # call helper function to get list of differences and find min
  even_div_helper(a, 0, 0, 0, diff_list)
  min_diff = min(diff_list)
  return min_diff


def even_div_helper(a, lista_sum, listb_sum, diff, diff_list):
  # subtract when list is empty and add result to diff_list
  if len(a) == 0:
    diff = abs(lista_sum - listb_sum)
    diff_list.append(diff)
  else:
    # Either add to lista_sum or listb_sum
    return (even_div_helper(a[1:], lista_sum + a[0], listb_sum, diff, diff_list)
    or even_div_helper(a[1:], lista_sum, listb_sum + a[0], diff, diff_list))

def main():
  # read the stdin 
  line = sys.stdin.readline()
  # convert to string list
  line_list = line.strip().split()
  num_list = []
  # change string to int and append to num_list
  for num in line_list:
    number = int(num)
    num_list.append(number)
  #print(num_list)
  print(even_div(num_list))

  

if __name__ == "__main__":
  main()