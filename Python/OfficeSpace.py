#  File: OfficeSpace.py

#  Description: Programs that determines the amount of office space requested
#  by each employee, by none employee, and by both employees. 

#  Student Name: Jiaxin Huang

#  Date Created: 02/15/2021

#  Date Last Modified: 02/15/2021

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
import sys

def area (rect):
    # Multiply the difference between the x's and y's to get area
    x1 = rect[0]
    y1 = rect[1]
    x2 = rect[2]
    y2 = rect[3]
    area = (x2 - x1) * (y2 - y1)
    return area

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
    # Separate the tuples by their point values
    rect1_x1 = rect1[0]
    rect1_y1 = rect1[1]
    rect1_x2 = rect1[2]
    rect1_y2 = rect1[3]
    rect2_x1 = rect2[0]
    rect2_y1 = rect2[1]
    rect2_x2 = rect2[2]
    rect2_y2 = rect2[3]
    # The overlapping points is depended on the min and max of the four points
    if (rect1_x1 < rect2_x2 and rect1_x2 > rect2_x1) and (rect1_y1 < rect2_y2 and rect1_y2 > rect2_y1):
        overlap_x1 = max(rect1_x1, rect2_x1)
        overlap_y1 = max(rect1_y1, rect2_y1)
        overlap_x2 = min(rect1_x2, rect2_x2)
        overlap_y2 = min(rect1_y2, rect2_y2)
        return (overlap_x1, overlap_y1, overlap_x2, overlap_y2)
    # Return tuple of 0 when not overlapping
    else:
        return (0, 0, 0, 0)

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
    count = 0
    # Add one to count for every 0 value in 2D list
    for row in bldg:
        for col in row:
            if col == 0:
                count += 1
    return count

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
    count = 0
    # Add one to count for every value greater than 1 in 2D list
    # Value > 1 shows the area is requested more than once
    for row in bldg:
        for col in row:
            if col > 1:
                count += 1
    return count

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
    count = 0
    # Find the corners of the rect space requested
    x1 = rect[0]
    y1 = rect[1]
    x2 = rect[2]
    y2 = rect[3]
    # Add one to count for every 1 value inside the rect space requested
    for i in range(x1, x2):
        for j in range(y1, y2):
            # -j - 1 since 0,0 is at the bottom left instead of top left
            # This changes 0 to -1 and 1 to -2 as index for rows
            if bldg[-j-1][i] == 1:
                count += 1
    return count

# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
    # Width and Height of the 2D list is dependent on the tuple
    # office = (0, 0, width, height)
    width = office[2]
    height = office[3]
    # Create a 2D list of 0s with width x height dimensions
    bldg = [[0 for x in range(width)] for x in range(height)]
    # 2nd line in the stdin file
    num_people = len(cubicles)
    # Loop through every tuple from employee
    for i in range(num_people):
        x1 = cubicles[i][0]
        y1 = cubicles[i][1]
        x2 = cubicles[i][2]
        y2 = cubicles[i][3]
        # Add 1 to every spot requested by an employee for every employee
        for i in range(x1, x2):
            for j in range(y1, y2):
                # -j - 1 since 0,0 is at the bottom left instead of top left
                # This changes 0 to -1 and 1 to -2 as index for rows
                bldg[-j-1][i] += 1
    return bldg

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert area ((0, 0, 1, 1)) == 1
  # write your own test cases

  return "all test cases passed"

def main():
  # read the data
    dimensions = sys.stdin.readline().split()
    cols, rows = dimensions[0], dimensions[1]
    # create tuple for rect with 0, 0 origin and cols, rows as x2, y2
    office = (0, 0, int(cols), int(rows))
    # Read total employees
    num_employees = int(sys.stdin.readline().strip())
    employees_data = [] # ex. [['Alice', '2', '3', '10', '11']]
    cubicles = [] # list of list of coordinates ex. [[2, 3, 10, 11]]
    cubicles_tuple = [] # list of tuple of coordinates ex. [(2, 3, 10, 11)]
    # Loop through each employee and add it to list
    for employee in range(num_employees):
        data = sys.stdin.readline().strip().split()
        employees_data.append(data)
        cubicles.append([])
        # Add only the coordinates not the names
        for value in range(1, 5):
            cubicles[employee].append(int((data[value])))
    # Changing list of lists to list of tuples in a new list
    for row in cubicles:
        cubicles_tuple.append(tuple(row))
        
    #print(employees_data)
    #print(cubicles)
    #print(cubicles_tuple)

  # print the following results after computation
    office_space = request_space(office, cubicles_tuple)
    # office_space is the 2D list

  # compute the total office space
    total = area(office)
    print("Total", total)

  # compute the total unallocated space
    unallocated_area = unallocated_space(office_space)
    print("Unallocated", unallocated_area)

  # compute the total contested space
    contested_area = contested_space(office_space)
    print("Contested", contested_area)
    
    #print(overlap(cubicles_tuple[0], cubicles_tuple[1]))
  # compute the uncontested space that each employee gets
    for employee in range(len(employees_data)):
        uncontested_area = uncontested_space(office_space, cubicles_tuple[employee])
        print(employees_data[employee][0], uncontested_area)
        

if __name__ == "__main__":
  main()