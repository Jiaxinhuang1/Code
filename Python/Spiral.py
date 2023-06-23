#  File: Spiral.py

#  Description: Program that finds the sum of the adjacent numbers of a certain user-inputted number in a 2D spiral list

#  Student Name: Jiaxin Huang

#  Date Created: 01/30/2021

#  Date Last Modified: 01/30/2021

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
import sys
import math

def create_spiral ( n ):
    spiral = [] #create empty list
    if n%2 == 0: #if n is even add one to n
        n += 1
    for row in range(n):    #create empty rows and columns equal to dimensions
        spiral.append([])
        for col in range(n):
            spiral[row].append([])
    
    start_index = 0     #starting index that will change every loop
    end_index = n - 1   #ending index that will change every loop
    num = n * n     #largest number based on dimension (will be located top right)

    #loop continues until the num reaches 1
    while num >= 1:
        for pos in range(end_index, start_index - 1, -1):   #first row num-1 starting from right to left
            spiral[start_index][pos] = num  
            num -= 1
        start_index += 1    #first row filled so new starting index will be next row
        for pos in range(start_index, end_index + 1):   #first column num-1 starting from top to down
            spiral[pos][start_index-1] = num
            num -= 1
        for pos in range(start_index, end_index + 1):   #last row num-1 starting from left to right
            spiral[end_index][pos] = num
            num -= 1
        end_index -= 1  #last row filled so new ending index will be index before it
        for pos in range(end_index, start_index - 1, -1):   #last column num-1 from bottom to top
            spiral[pos][end_index + 1] = num
            num -= 1
    return spiral   #return the 2D spiral list


# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers (spiral, n):
    found = False 
    while found == False:   #loop through every row in spiral and count
        row_num = 0
        for row in spiral:
            last_row = int((math.sqrt(spiral[0][-1])) - 1)  #find index of last row (the dimensions - 1 )
            #print("Last row", last_row)
            last_col = -1   #right column
            if n not in row and row_num == last_row: #return 0 if n is outside range
                return 0
            if n in row:    #check if the n (input read from file) is in the row
                col = row.index(n)  #find the index column of the n
                found = True
                if row_num == 0 and col == 0:   #add adjacents of top left number
                    #print("top left")
                    result = (spiral[row_num][col + 1]
                            + spiral[row_num + 1][col + 1]
                            + spiral[row_num + 1][col])
                elif n == spiral[0][last_col]: #add adjacents of top right number
                    #print("top right")
                    result = (spiral[row_num][col - 1]
                            + spiral[row_num + 1][col - 1]
                            + spiral[row_num + 1][col])
                elif row_num == last_row and col == 0:  #add adjacents of bottom left number
                    #print("bottom left")
                    result = (spiral[row_num - 1][col]
                            + spiral[row_num - 1][col + 1]
                            + spiral[row_num][col + 1])
                elif n == spiral[last_row][last_col]:   #add adjacents of bottom right number
                    #print("bottom right")
                    result = (spiral[row_num][col - 1]
                            + spiral[row_num - 1][col - 1]
                            + spiral[row_num - 1][col])
                elif row_num == 0:  #add adjacents of top row
                    #print("top row")
                    result = (spiral[row_num][col - 1]
                            + spiral[row_num][col + 1]
                            + spiral[row_num + 1][col - 1]
                            + spiral[row_num + 1][col + 1]
                            + spiral[row_num + 1][col])
                elif row_num == last_row:   #add adjacents of bottom row
                    #print("bottom row")
                    result = (spiral[row_num][col - 1]
                            + spiral[row_num][col + 1]
                            + spiral[row_num - 1][col - 1]
                            + spiral[row_num - 1][col + 1]
                            + spiral[row_num - 1][col])
                elif col == 0:  #add adjacents of left column
                    #print("left column")
                    result = (spiral[row_num + 1][col]
                            + spiral[row_num - 1][col]
                            + spiral[row_num][col + 1]
                            + spiral[row_num - 1][col + 1]
                            + spiral[row_num + 1][col + 1])
                elif n == spiral[row_num][last_col]: #add adjacents of right column
                    #print("right column")
                    result = (spiral[row_num + 1][col]
                            + spiral[row_num - 1][col]
                            + spiral[row_num][col - 1]
                            + spiral[row_num - 1][col - 1]
                            + spiral[row_num + 1][col - 1])
                else:
                    #print("middle")
                    result = (spiral[row_num - 1][col] 
                            + spiral[row_num + 1][col]
                            + spiral[row_num][col + 1]
                            + spiral[row_num][col - 1]
                            + spiral[row_num + 1][col + 1]
                            + spiral[row_num + 1][col - 1]
                            + spiral[row_num - 1][col + 1]
                            + spiral[row_num - 1][col - 1])
                return result
            row_num += 1
        
def main():   
  # read the input file
    dimensions = int(sys.stdin.readline().strip())
  # create the spiral
    spiral = create_spiral(dimensions)

  # add the adjacent numbers
    for line in sys.stdin.readlines(): #read every line on file
        user_num = int(line)
        result = sum_adjacent_numbers(spiral, user_num)  

  # print the result
        print(result)

if __name__ == "__main__":
  main()
