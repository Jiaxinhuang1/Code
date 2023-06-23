#  File: Hull.py

#  Description: Program that finds the vertices of the convex hull 
#  for a set number of points and the area of polygon created

#  Student Name: Jiaxin Huang

#  Date Created: 02/20/2021

#  Date Last Modified: 02/20/2021

import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
    # Find determinant by (x2-x1)(y3-y1) - (y2-y1)(x3-x1)
    # If result 0 then collinear, if + then left turn (counter-clockwise), if - then right turn (clockwise)
    determinant = ((q.x - p.x) * (r.y - p.y)) - ((q.y - p.y) * (r.x - p.x))
    return determinant 

# Functions that returns a boolean depending on whether 3 points is right turn, left turn, or collinear
def right_turn(p, q, r):
    return det(p, q, r) < 0

def left_turn(p, q, r):
    return det(p, q, r) > 0

def collinear(p, q, r):
    return det(p, q, r) == 0

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
    # Create empty list and append first two points of sorted_points inside
    upper_hull = []
    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])
    # For i going from 3 to n, append p[i] to upper_hull
    for i in sorted_points[2:]:
        upper_hull.append(i)
        # While upper_hull has 3 or more points and last 3 points do not make right turn
        while len(upper_hull) >= 3 and (not right_turn(upper_hull[-3], upper_hull[-2], upper_hull[-1])):
            # delete the middle of the last three points
            del upper_hull[-2]
    
    # Create a new list that is the reverse of sorted_points
    reversed_points = sorted_points[::-1]
    # Create empty list and append first two points of sorted_points inside
    lower_hull = []
    lower_hull.append(reversed_points[0])
    lower_hull.append(reversed_points[1])
    # For i going from 3 to n, append p[i] to lower_hull
    for i in reversed_points[2:]:
        lower_hull.append(i)
        # While lower_hull has 3 or more points and last 3 points do not make right turn
        while len(lower_hull) >= 3 and (not right_turn(lower_hull[-3], lower_hull[-2], lower_hull[-1])):
            # delete the middle of the last three points           
            del lower_hull[-2]
    
    # Remove first and last points for lower_hull to avoid duplication with upper_hull
    del lower_hull[0]
    del lower_hull[-1]
    # New list containing powers from upper and lower hull
    convex_hull = upper_hull + lower_hull

    return convex_hull

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
    # Store total number of points in list
    num_points = len(convex_poly)
    # Create two empty list for the pos and neg terms 
    pos_list = []
    neg_list = []
    # Loop through each point
    for i in range(len(convex_poly) - 1):
        # Multiply the x of one point with the y of the point after it
        pos_total = convex_poly[i].x * convex_poly[i+1].y
        # Append product to list
        pos_list.append(pos_total)
        # Multiply the y of one point with the x of the point after it
        neg_total = convex_poly[i].y * convex_poly[i+1].x 
        # Append the product to list
        neg_list.append(neg_total)

    # Multiply the last x with the first y in the list and append
    last_pos = convex_poly[num_points - 1].x * convex_poly[0].y
    pos_list.append(last_pos)
    # Multiply the last y with the first x in the list and append
    last_neg = convex_poly[num_points - 1].y * convex_poly[0].x
    neg_list.append(last_neg)

    # Add the products of each list
    total_pos = sum(pos_list)
    total_neg = sum(neg_list)
    # Determinant is the difference between the pos terms and neg terms
    det = total_pos - total_neg
    # Area formula 
    area = (1/2) * abs(det)
    return area

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

    return "all test cases passed"

def main():
    # create an empty list of Point objects
    points_list = []

    # read number of points
    line = sys.stdin.readline()
    line = line.strip()
    num_points = int (line)

    # read data from standard input
    for i in range (num_points):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        x = int (line[0])
        y = int (line[1])
        points_list.append (Point (x, y))

    # sort the list according to x-coordinates
    sorted_points = sorted (points_list)

    # print the sorted list of Point objects
    #for p in sorted_points:
    # print (str(p))
    print("Convex Hull")
    # get the convex hull
    convex_points = convex_hull(sorted_points)

    # print your results to standard output
    # print the convex hull
    for p in convex_points:
        print (str(p))
    print()
    # get the area of the convex hull
    total_area = area_poly(convex_points)
    # print the area of the convex hull
    print("Area of Convex Hull =", total_area)

if __name__ == "__main__":
  main()