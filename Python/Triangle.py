# File: Triangle.py

# Description: A basic 2D Triangle class

# Student Name: Jiaxin Huang

"""
Test Input:
0.0 0.0 3.0 0.0 0.0 4.0
3.0 3.0 6.0 3.0 3.0 7.0

Test Output:
Point1: (0.0, 0.0), Point2: (3.0, 0.0), Point3: (0.0, 4.0), Area: 6.0
Point1: (3.0, 3.0), Point2: (6.0, 3.0), Point3: (3.0, 7.0), Area: 6.0
True
True
True

Test Input 2:
3.3 6.6 4.4 8.8 9.9 12
0.0 -3.2 5.5 6.6 2.2 1.4

Test Output 2:
Point1: (3.3, 6.6), Point2: (4.4, 8.8), Point3: (9.9, 12.0), Area: 4.290000000000002
Point1: (0.0, -3.2), Point2: (5.5, 6.6), Point3: (2.2, 1.4), Area: 1.8699999999999974
True
True
False
"""

import sys
import math

TOL = 0.01

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

class Triangle (object):
    # constructor

    # TODO: 
  def __init__ (self, p1, p2, p3):
    self.p1 = p1
    self.p2 = p2
    self.p3 = p3
    self.side1 = self.p1.dist(self.p2)
    self.side2 = self.p2.dist(self.p3)
    self.side3 = self.p3.dist(self.p1)
    # print string representation of Triangle

    # TODO: 
  def __str__ (self):
    return "Point1: (" + str(self.p1.x) + ", " + str(self.p1.y) + "), Point2: (" + str(self.p2.x) +", " + str(self.p2.y) + "), Point3: (" + str(self.p3.x) + ", " + str(self.p3.y) + "), Area: " + str(self.area())

    # check congruence of Triangles with equality

    # TODO: YOUR CODE HERE
  def __eq__ (self, other):
    dist1 = [self.side1, self.side2, self.side3]
    dist2 = [other.side1, other.side2, other.side3]
    return dist1 == dist2

    # returns whether or not the triangle is valid

    # TODO: YOUR CODE HERE
  def is_triangle(self):
    return ((self.side1 + self.side2 > self.side3)
    and (self.side1 + self.side3 > self.side2)
    and (self.side2 + self.side3 > self.side1))


    # return the area of the triangle:

    # TODO: YOUR CODE HERE
  def area(self):
    return abs((self.p1.x * (self.p2.y - self.p3.y) + self.p2.x * (self.p3.y - self.p1.y) + self.p3.x * (self.p1.y - self.p2.y))/2)


######################################################
# The code below is filled out for you, DO NOT EDIT. #
######################################################

# takes a string of coordinates and changes it to a list of Points
def get_points(coords_str):
    coords = [float(c) for c in coords_str.split(" ")]
    return [Point(c[0], c[1]) for c in zip(*[iter(coords)]*2)]

def main():
    # read the two triangles
    pointsA = get_points(sys.stdin.readline().strip())
    pointsB = get_points(sys.stdin.readline().strip())

    triangleA = Triangle(pointsA[0], pointsA[1], pointsA[2])
    triangleB = Triangle(pointsB[0], pointsB[1], pointsB[2])

    # Print final output
    print(triangleA)
    print(triangleB)
    print(triangleA.is_triangle())
    print(triangleB.is_triangle())
    print(triangleA == triangleB)

if __name__ == "__main__":
    main()
