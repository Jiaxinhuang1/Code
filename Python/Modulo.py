#  File: Modulo.py

#  Description: Determines if a list of integers is closed under modulo (x % y is also a member # of the list for any nonzero x and y in the list)

#  Student Name: Jiaxin Huang

import sys

# Input: lst is a list of positive integers that includes 0
# Output: return True if for any 2 nonzero elements x and y in the list, x % y is also in the list
# return False otherwise

def is_closed_modulo(lst):
    found = True
    for index in range(len(lst) - 1):
        for index2 in range(len(lst) - 1):
            if (lst[index] != 0) and (lst[index2] != 0):
                result = lst[index] % lst[index2]
                if result not in lst:
                    found = False
    if found == False:
        return False
    return True
                



def main(): 
    # read input file
    lst = [int(x) for x in sys.stdin.readline().strip().split(" ")]

    # get result from your call to is_closed_modulo()
    result = is_closed_modulo(lst)

    # print the result to standard output
    print(result)

if __name__ == "__main__":
    main()