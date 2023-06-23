#  File: Geometry.py

#  Description: Program that uses classes and functions to test whether
# an object is inside another object

#  Student Name: Jiaxin Huang

#  Date Created: 02/09/2021

#  Date Last Modified: 02/11/2021

import math
import sys

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
    return '('+ str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
    return math.hypot(self.x - other.x, self.y - other.y, self.z - other.z)

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    tol = 1.0e-6
    return ((abs(self.x - other.x) < tol) 
    and (abs(self.y - other.y) < tol)
    and (abs(self.z - other.z) < tol))

class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.radius = float(radius)
    self.center = Point(x, y, z)

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
    return 'Center: (' + str(self.x) + ', ' + str(self.y) + ', '  + str(self.z) +'), Radius: ' + str(self.radius)

  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
    return 4 * math.pi * math.pow(float(self.radius), 2)

  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
    return (4/3) * math.pi * math.pow(float(self.radius), 3)

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
      return self.center.distance(p) < self.radius

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
    # Distance between the two centers plus radius of smaller sphere
    # must be less than the radius of the bigger sphere
    return (self.center.distance(other.center) + other.radius) < self.radius

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    # If all 8 corners are inside sphere, then cube is inside sphere
    return ((self.center.distance(a_cube.p1) < self.radius)
    and (self.center.distance(a_cube.p2) < self.radius)
    and (self.center.distance(a_cube.p3) < self.radius)
    and (self.center.distance(a_cube.p4) < self.radius)
    and (self.center.distance(a_cube.p5) < self.radius)
    and (self.center.distance(a_cube.p6) < self.radius)
    and (self.center.distance(a_cube.p7) < self.radius)
    and (self.center.distance(a_cube.p8) < self.radius))

  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
    # Inside if all the extreme points are inside
    return ((self.center.distance(a_cyl.p1) < self.radius)
    and (self.center.distance(a_cyl.p2) < self.radius)
    and (self.center.distance(a_cyl.p3) < self.radius)
    and (self.center.distance(a_cyl.p4) < self.radius)
    and (self.center.distance(a_cyl.p5) < self.radius)
    and (self.center.distance(a_cyl.p6) < self.radius)
    and (self.center.distance(a_cyl.p7) < self.radius)
    and (self.center.distance(a_cyl.p8) < self.radius))

  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
    # Intersects if distance between center is less than or equal to sum of their radius
    return (self.center.distance(other.center) <= self.radius + other.radius)

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
    # Intersect if there is a point inside and ouside the cube
    inside = False
    outside = False
    vertices = [a_cube.p1, a_cube.p2, a_cube.p3, a_cube.p4, a_cube.p5, a_cube.p6, a_cube.p7, a_cube.p8]
    for index in range(len(vertices)):
      if self.center.distance(vertices[index]) < self.radius:
          inside = True
      if self.center.distance(vertices[index]) > self.radius:
          outside = True
    if inside and outside:
        return True
    
  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
    # cube is totally inside and 8 corners on surface
    # center of cube = center of sphere
    # get side by diagonal (radius of sphere)
    # use side formulat a = 2r * sqrt(3)
    side = (2 * self.radius) / math.sqrt(3)
    circum_cube = Cube(self.x, self.y, self.z, side)
    return circum_cube

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.side = float(side)
    self.center = Point(x, y, z)
  # Finding the 8 vertices of cube
    self.p1 = Point( self.x - (self.side/2), self.y + (self.side/2), self.z + (self.side/2))
    self.p2 = Point( self.x + (self.side/2), self.y + (self.side/2), self.z + (self.side/2))
    self.p3 = Point( self.x - (self.side/2), self.y + (self.side/2), self.z - (self.side/2))
    self.p4 = Point( self.x + (self.side/2), self.y + (self.side/2), self.z - (self.side/2))
    self.p5 = Point( self.x - (self.side/2), self.y - (self.side/2), self.z - (self.side/2))
    self.p6 = Point( self.x - (self.side/2), self.y - (self.side/2), self.z + (self.side/2))
    self.p7 = Point( self.x + (self.side/2), self.y - (self.side/2), self.z + (self.side/2))
    self.p8 = Point( self.x + (self.side/2), self.y - (self.side/2), self.z - (self.side/2))
  # Finding the min and max of each coordinate
    self.xMax = self.x + (self.side/2)
    self.xMin = self.x - (self.side/2)
    self.yMax = self.y + (self.side/2)
    self.yMin = self.y - (self.side/2)
    self.zMax = self.z + (self.side/2)
    self.zMin = self.z - (self.side/2)
    
  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
    return 'Center: (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + '), Side: ' + str(self.side)

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
    return 6 * math.pow(float(self.side), 2)

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
    return math.pow(float(self.side), 3)

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
    # If x min of cube < x of point < x max of cube and
    # y min of cube < y of point < y max of cube and
    # z min of cube < z of point < z max of cube then is inside
    return ((self.xMin < p.x < self.xMax)
    and (self.yMin < p.y < self.yMax)
    and (self.zMin < p.z < self.zMax))

  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    #((self.center.__eq__(a_sphere.center)) and (self.side.__eq__(a_sphere.radius * 2)))
    # Put sphere in box
    sphere_side = a_sphere.radius * 2
    sphere_box = Cube(a_sphere.x, a_sphere.y, a_sphere.z, sphere_side)
    return self.is_inside_cube(sphere_box)

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
    # all 8 corners should be inside
    return (((other.xMin > self.xMin) and (other.xMax < self.xMax))
    and ((other.yMin > self.yMin) and (other.yMax < self.yMax))
    and ((other.zMin > self.zMin) and (other.zMax < self.zMax)))

  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):
    # cylinder in box an check if the corners of the box is inside the cube
    return (((a_cyl.xMin > self.xMin) and (a_cyl.xMax < self.xMax))
    and ((a_cyl.yMin > self.yMin) and (a_cyl.yMax < self.yMax))
    and ((a_cyl.zMin > self.zMin) and (a_cyl.zMax < self.zMax)))

  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
    # if its not inside and not outside then intersect
    return ((self.xMin < other.xMax and self.xMax > other.xMin)
    and (self.yMin < other.yMax and self.yMax > other.yMin)
    and (self.zMin < other.zMax and self.zMax > other.zMin))

  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
    # if dont intersect return 0
    # the differences between the min and max of each coordinate is equal to intersection coordinate
    if (self.does_intersect_cube(other)):
      if (self.xMin < other.xMax and self.xMax > other.xMin):
        final_x = other.xMax - self.xMin
      if (self.yMin < other.yMax and self.yMax > other.yMin):
        final_y = other.yMax - self.yMin
      if (self.zMin < other.zMax and self.zMax > other.zMin):
        final_z = other.zMax - self.zMax
      inter_volume = abs(final_x * final_y * final_z)
      return inter_volume
    return 0

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
    # center of the sphere is center of cube the radius of the sphere is half the size
    rad = self.side/2
    largest_sphere = Sphere(self.x, self.y, self.z, rad)
    return largest_sphere

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.radius = float(radius)
    self.height = float(height)
    self.center = Point(x, y, z)
    # Getting the extremes
    self.xMax = self.x + self.radius
    self.xMin = self.x - self.radius
    self.yMax = self.y + self.radius
    self.yMin = self.y - self.radius
    self.zMax = self.z + (self.height/2)
    self.zMin = self.z - (self.height/2)

    # Vertices of cyl when put inside rectangular prism
    self.p1 = Point( self.xMin, self.y, self.zMax )
    self.p2 = Point( self.xMax, self.y, self.zMax )
    self.p3 = Point( self.x, self.yMin, self.zMax )
    self.p4 = Point( self.x, self.yMax, self.zMax )
    self.p5 = Point( self.xMin, self.y, self.zMin )
    self.p6 = Point( self.xMax, self.y, self.zMin )
    self.p7 = Point( self.x, self.yMin, self.zMin )
    self.p8 = Point( self.x, self.yMax, self.zMin )

  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    return 'Center: (' + str(self.x) + ', ' + str(self.y) +', ' + str(self.z) + '), Radius: ' + str(self.radius) +', Height: ' + str(self.height)

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
    return (2 * math.pi * float(self.radius) * float(self.height)) + (2 * math.pi * math.pow(float(self.radius), 2))

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
    return math.pi * math.pow(float(self.radius), 2) * float(self.height)

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
    # If z min of cyl < z of point < z max of cyl and
    # dist from p to axis of cyl OR x/y coord ignoring z < radius of cyl
    point_a = Point(self.x, self.y, 0)
    point_b = Point(p.x, p.y, 0)
    return (self.zMin < p.z < self.zMax) and (point_a.distance(point_b) < self.radius)

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    # Inside if radius is smaller and if z value of center plus/minus radius is in between the zmin and zmax of cyl
    sphere_zMax = a_sphere.z + a_sphere.radius
    sphere_zMin = a_sphere.z - a_sphere.radius
    return (self.radius > a_sphere.radius) and (self.zMin < sphere_zMin) and (self.zMax > sphere_zMax)

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    # 8 corners of cube inside cylinder
    return ((self.is_inside_point(a_cube.p1)) 
    and (self.is_inside_point(a_cube.p2)) 
    and (self.is_inside_point(a_cube.p3)) 
    and (self.is_inside_point(a_cube.p4)) 
    and (self.is_inside_point(a_cube.p5)) 
    and (self.is_inside_point(a_cube.p6)) 
    and (self.is_inside_point(a_cube.p7)) 
    and (self.is_inside_point(a_cube.p8)))

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
    # put cylinder inside box and chekc if all 8 corners inside
    return ((self.is_inside_point(other.p1)) 
    and (self.is_inside_point(other.p2)) 
    and (self.is_inside_point(other.p3)) 
    and (self.is_inside_point(other.p4)) 
    and (self.is_inside_point(other.p5)) 
    and (self.is_inside_point(other.p6)) 
    and (self.is_inside_point(other.p7)) 
    and (self.is_inside_point(other.p8)))

  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):
    # if cylinder is not inside and outside (can write an outside function)
    # Find center while ignoring z
    cyl = Sphere(self.x, self.y, 0, self.radius)
    sph = Sphere(other.x, other.y, 0, other.radius)
    return ((cyl.does_intersect_sphere(sph)) 
    and (self.zMin < other.zMax and self.zMax > other.zMin))

def main():

  # read data from standard input
  # read the coordinates of the first Point p
    p_coord = sys.stdin.readline().split()
  # create a Point object
    point_p = Point(p_coord[0], p_coord[1], p_coord[2])
  # read the coordinates of the second Point q
    q_coord = sys.stdin.readline().split()
  # create a Point object 
    point_q = Point(q_coord[0], q_coord[1], q_coord[2])
  # read the coordinates of the center and radius of sphereA
    sphereA_coord = sys.stdin.readline().split()
  # create a Sphere object 
    sphereA = Sphere(sphereA_coord[0], sphereA_coord[1], sphereA_coord[2], sphereA_coord[3])
  # read the coordinates of the center and radius of sphereB
    sphereB_coord = sys.stdin.readline().split()
  # create a Sphere object
    sphereB = Sphere(sphereB_coord[0], sphereB_coord[1], sphereB_coord[2], sphereB_coord[3])
  # read the coordinates of the center and side of cubeA
    cubeA_coord = sys.stdin.readline().split()
  # create a Cube object 
    cubeA = Cube(cubeA_coord[0], cubeA_coord[1], cubeA_coord[2], cubeA_coord[3])
    #print('Cube ', cubeA.p1, cubeA.p2, cubeA.p3, cubeA.p4, cubeA.p5, cubeA.p6, cubeA.p7, cubeA.p8)
  # read the coordinates of the center and side of cubeB
    cubeB_coord = sys.stdin.readline().split()
  # create a Cube object 
    cubeB = Cube(cubeB_coord[0], cubeB_coord[1], cubeB_coord[2], cubeB_coord[3])
  # read the coordinates of the center, radius and height of cylA
    cylA_coord = sys.stdin.readline().split()
  # create a Cylinder object 
    cylA = Cylinder(cylA_coord[0], cylA_coord[1], cylA_coord[2], cylA_coord[3], cylA_coord[4])
    #print("CylA points", cylA.p1, cylA.p2, cylA.p3, cylA.p4, cylA.p5, cylA.p6, cylA.p7, cylA.p8)
  # read the coordinates of the center, radius and height of cylB
    cylB_coord = sys.stdin.readline().split()
  # create a Cylinder object
    cylB = Cylinder(cylB_coord[0], cylB_coord[1], cylB_coord[2], cylB_coord[3], cylB_coord[4])

  # Starts implementing functions to find relations

  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin
    origin = Point(0, 0, 0)
    if point_p.distance(origin) > point_q.distance(origin):
        print('Distance of Point p from the origin is greater than the distance of Point q from the origin')
    else:
        print('Distance of Point p from the origin is not greater than the distance of Point q from the origin')
    
  # print if Point p is inside sphereA
    if sphereA.is_inside_point(point_p):
        print('Point p is inside sphereA')
    else:
        print('Point p is not inside sphereA')

  # print if sphereB is inside sphereA
    if sphereA.is_inside_sphere(sphereB):
        print('sphereB is inside sphereA')
    else:
        print('sphereB is not inside sphereA')

  # print if cubeA is inside sphereA
    if sphereA.is_inside_cube(cubeA):
        print('cubeA is inside sphereA')
    else:
        print('cubeA is not inside sphereA')

  # print if cylA is inside sphereA
    if sphereA.is_inside_cyl(cylA):
      print('cylA is inside sphereA')
    else:
      print('cylA is not inside sphereA')

  # print if sphereA intersects with sphereB
    if sphereA.does_intersect_sphere(sphereB):
        print('sphereA does intersect sphereB')
    else:
        print('sphereA does not intersect sphereB')

  # print if cubeB intersects with sphereB
    if sphereB.does_intersect_cube(cubeB):
        print('cubeB does intersect sphereB')
    else:
        print('cubeB does not intersect sphereB')

  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA
    if (sphereA.circumscribe_cube()).volume() > cylA.volume():
      print('Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA')
    else:
      print('Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA')

  # print if Point p is inside cubeA
    if cubeA.is_inside_point(point_p):
      print('Point p is inside cubeA')
    else:
      print('Point p is not inside cubeA')

  # print if sphereA is inside cubeA
    if cubeA.is_inside_sphere(sphereA):
      print('sphereA is inside cubeA')
    else:
      print('sphereA is not inside cubeA')

  # print if cubeB is inside cubeA
    if cubeA.is_inside_cube(cubeB):
      print('cubeB is inside cubeA')
    else:
      print('cubeB is not inside cubeA')

  # print if cylA is inside cubeA
    if cubeA.is_inside_cylinder(cylA):
      print('cylA is inside cubeA')
    else:
      print('cylA is not inside cubeA')

  # print if cubeA intersects with cubeB
    if cubeA.does_intersect_cube(cubeB):
        print('cubeA does intersect cubeB')
    else:
        print('cubeA does not intersect cubeB')

  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
    if cubeA.intersection_volume(cubeB) > sphereA.volume():
      print('Intersection volume of cubeA and cubeB is greater than the volume of sphereA')
    else:
      print('Intersection volume of cubeA and cubeB is not greater than the volume of sphereA')

  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA
    if (cubeA.inscribe_sphere()).area() > cylA.area():
      print('Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA')
    else:
      print('Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA')

  # print if Point p is inside cylA
    if (cylA.is_inside_point(point_p)):
      print('Point p is inside cylA')
    else:
      print('Point p is not inside cylA')

  # print if sphereA is inside cylA
    if (cylA.is_inside_sphere(sphereA)):
      print('sphereA is inside cylA')
    else:
      print('sphereA is not inside cylA')

  # print if cubeA is inside cylA
    if (cylA.is_inside_cube(cubeA)):
      print('cubeA is inside cylA')
    else:
      print('cubeA is not inside cylA')

  # print if cylB is inside cylA
    if (cylA.is_inside_cylinder(cylB)):
      print('cylB is inside cylA')
    else:
      print('cylB is not inside cylA')

  # print if cylB intersects with cylA
    if (cylA.does_intersect_cylinder(cylB)):
      print('cylB does intersect cylA')
    else:
      print('cylB does not intersect cylA')

if __name__ == "__main__":
  main()