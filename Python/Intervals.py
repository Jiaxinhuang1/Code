#  File: Intervals.py

#  Description: Program take a set of intervals and collapse all 
# the overlapping intervals and print the smallest set of non-intersecting 
# intervals in ascending order of the lower end of the interval and then 
# print the intervals in increasing order of the size of the interval.

#  Student Name: Jiaxin Huang

#  Date Created: 02/03/2021

#  Date Last Modified: 02/04/2021

'''How to use this Template:
For this assignment, do not change the function names or parameters
You will need to read from standard input. In order to do this, when 
you run your program in the command line, you will do it as follows:

$ python3 Intervals.py < intervals.in

If you read intervals.in as a file, it will not work on HackerRank. 
You should be able to paste this whole file into HackerRank. Please 
run your code to ensure it passes, and write your own test cases to 
ensure your answer is correct.
'''

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
import sys

def is_inside(int_a, int_b): # return true if interval b is inside a
    return int_b[0] >= int_a[0] and int_b[0] <= int_a[1]


def merge_tuples (tuples_list):
    sort_list = sorted(tuples_list) # create new list of sorted intervals
    # print(sort_list)
    merged_list= [] # create empty list
    merged_list.append(sort_list[0]) # add 1st element of sorted list to empty
    for i in range(1, len(sort_list)): # loop each index of sorted list
        higher_value = -100000000000    # set imposible max value
        start = merged_list.pop(-1) # remove last element and return
        # print('pop', start)
        if is_inside(start, sort_list[i]):  #check if interval inside another
            if start[1] > sort_list[i][1]:  #find higher value for second element in tuple
                higher_value = start[1]
            else:
                higher_value = sort_list[i][1]
            new_tup = (start[0], higher_value)  # create new tuple
            merged_list.append(new_tup) # add new tuple to list
        else:
            merged_list.append(start)   # add the removed/returned element to list
            merged_list.append(sort_list[i]) # add the next tuple in list to merged list
    return merged_list


# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):
    mylist = [] # created two empty list
    mylist_final = []
    i = 0   # set i for index in list
    while i < len(tuples_list): # loop through all values in list
        diff = tuples_list[i][1] - tuples_list[i][0]    # find difference
        mylist.append([diff, tuples_list[i]])   # add list of diff and tuple to first list
        mylist = sorted(mylist) # sort the list based on smallest difference
        i += 1
    for row in mylist:  # loop throw each list within list
        mylist_final.append(row[1]) # add only the tuple to the final list (not diff)
    return mylist_final


def main():
  # read the input data and create a list of tuples
    list_of_tuples = []
    num_intervals = int(sys.stdin.readline().strip())

    for i in range(num_intervals):
        value = sys.stdin.readline().strip()
        mytuple = tuple(map(int, value.split(' ')))
        list_of_tuples.append(mytuple)       

  # merge the list of tuples
    merged_list = merge_tuples(list_of_tuples)
    print(merged_list)
  # print the merged list

  # sort the list of tuples according to the size of the interval
    sorted_merged = sort_by_interval_size(merged_list)
  # print the sorted list
    print(sorted_merged)


if __name__ == "__main__":
  main()