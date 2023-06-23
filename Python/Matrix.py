#  File: Matrix.py

#  Description: Determines if a square 2d list of 1s and 0s has some "symmetry" where the matrix is 
#               the same after one of the following operations: rotate clockwise 90 degrees, rotate 
#               counterclockwise 90 degrees, flip horizontally, or flip vertically

#  Student Name: Jiaxin Huang

import sys

# Prints your 2d list
# Can be used for debugging purposes
def print_arr(temp):
    mx = max((len(str(ele)) for sub in temp for ele in sub))
    for row in temp:
        print(" ".join(["{:<{mx}}".format(ele,mx=mx) for ele in row]))
    print()


# Input: matrix is a 2d square list of 1s and 0s
# Output: return True if a rotation by 90 degrees in either direction (clockwise/counterclockwise)
# or a horizontal/vertical flip results in the matrix being equal to itself.
# return False otherwise
def matrix_has_symmetry(matrix):
    rotate_clockwise = []
    rotate_counter = []
    flip_vert = []
    flip_hort = []
    matrix_copy = matrix

    # matrix with clockwise 90 rotation
    for i in range(len(matrix)):
        rotate_clockwise.append([])
        num = len(matrix)
        for j in range(len(matrix[0])):
            num -= 1
            rotate_clockwise[i].append(matrix[num][i])
    #print_arr(rotate_clockwise)

    # matrix with counter clockwise 90 rotation
    num = len(matrix)
    for i in range(len(matrix)):
        rotate_counter.append([])
        num -= 1
        for j in range(len(matrix[0])):
            rotate_counter[i].append(matrix[j][num])
    #print_arr(rotate_counter)

    # matrix with flip horizontal
    for i in range(1, len(matrix_copy) + 1):
        flip_vert.append(matrix_copy[-i])
    #print_arr(flip_vert)

    # matrix with flip vertical
    for i in range(len(matrix_copy)):
        flip_hort.append([])
        for j in range(1, len(matrix_copy[0]) + 1):
            flip_hort[i].append(matrix_copy[i][-j])
    #print_arr(flip_hort)
    if (rotate_clockwise == matrix) or (rotate_counter == matrix) or (flip_vert == matrix) or (flip_hort == matrix):
        return True
    else:
        return False
    

def main(): 
    # read dimension of square matrix
    n = int(input())

    matrix = []
    # read data from standard input
    for i in range(n):
        matrix.append(list(map(int, input().split())))

    # get the result from your call to matrix_has_symmetry()
    result = matrix_has_symmetry(matrix)

    # print the result to standard output
    print(result)

if __name__ == "__main__":
    main()