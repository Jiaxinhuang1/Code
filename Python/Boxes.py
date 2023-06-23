#  File: Boxes.py

#  Description: Program that finds the number of boxes and sets of boxes
#  that fit inside each other given dimensions.

#  Student Name: Jiaxin Huang

#  Date Created: 03/25/2021

#  Date Last Modified:  03/26/2021

import sys

# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
  # Base Case: Add the all the possible subsets to list
  if (idx == len(box_list)):
    all_box_subsets.append(sub_set)
    return
  else:
    # examines each element in list and adds the box to basket or not
    # copies the lst
    c = sub_set[:]
    sub_set.append(box_list[idx])
    # one recursive added to basket and another is not added to basket
    # ex. First A added then not added then decision tree moves forward
    sub_sets_boxes(box_list, sub_set, idx + 1, all_box_subsets)
    sub_sets_boxes(box_list, c, idx + 1, all_box_subsets)

# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets (all_box_subsets):
  nested_sub = [] # stores all the nested subsets
  all_nesting_boxes = [] # stores the largest nesting subset boxes
  index_list = 0 
  isFit = False
  # loop thro all the subsets in list
  for subset in all_box_subsets:
    # check if there is more than one box on subset
    if len(subset) >= 2:
      for i in range(len(subset) - 1):
        # check if the left box fit inside the right
        if (does_fit(subset[i], subset[i+1])):
          index_list = i + 1
          isFit = True
        else:
          # break and move on to next subset if does not fit
          break
        # If all boxes in subset fits then add the subset to the nested sub list
        # and reset the fit to false
        if ((index_list == len(subset) - 1) and (isFit == True)):
          nested_sub.append(subset)
          isFit = False
  #print(nested_sub)
  nested_sub.sort() # sort the list
  largest_size = 0 # store the largest subset size

  # loop through all the subsets in nested_sub 
  for subset in nested_sub:
    # If the size of the subset is larger than the variable largest_size
    # set that size as the new largest_size
    if len(subset) > largest_size:
      largest_size = len(subset)

  # loop through all the subsets in nested_sub
  for sub_index in range(len(nested_sub)):
    # if the size of the subset is equal to the largest size, add
    # it to all_nesting_boxes (the largest subset of nesting boxes)
    if len(nested_sub[sub_index]) == largest_size:
      all_nesting_boxes.append(nested_sub[sub_index])

  return all_nesting_boxes

# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  '''
  # print to make sure that the input was read in correctly
  print (box_list)
  print()
  '''

  # sort the box list
  box_list.sort()

  '''
  # print the box_list to see if it has been sorted.
  print (box_list)
  print()
  '''

  # create an empty list to hold all subset of boxes
  all_box_subsets = []

  # create a list to hold a single subset of boxes
  sub_set = []

  # generate all subsets of boxes and store them in all_box_subsets
  sub_sets_boxes (box_list, sub_set, 0, all_box_subsets)

  # all_box_subsets should have a length of 2^n where n is the number
  # of boxes
  #print("all box subsets")
  #print(len(all_box_subsets))


  # go through all the subset of boxes and only store the
  # largest subsets that nest in all_nesting_boxes
  all_nesting_boxes = largest_nesting_subsets (all_box_subsets)
  '''
  print("Largest Subset of Nesting Boxes")
  for subset in all_nesting_boxes:
    for box in subset:
      print(box)
    print()
  '''  

  # print the largest number of boxes that fit
  print(len(all_nesting_boxes[0]))

  # print the number of sets of such boxes
  print(len(all_nesting_boxes))

if __name__ == "__main__":
  main()