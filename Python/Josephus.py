#  File: Josephus.py

#  Description: Program that determines which soldier can escape by 
# a series of eliminations based on a certain number

#  Student Name: Jiaxin Huang

#  Date Created: 04/09/2021

#  Date Last Modified: 04/11/2021

import sys

class Link(object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next


class CircularList(object):
  # Constructor
  def __init__ ( self ): 
      self.first = None # start with an empty link list

  # Insert an element (value) in the list
  def insert ( self, data ):
      # similar to insert_last on regular linked list
      new_link = Link(data)     # create a new link
      current = self.first 
      # when list is empty, add it to first and set next to first since circular
      if (self.is_empty and current == None):
          self.first = new_link
          self.first.next = self.first
          return
      else:
        # when it is not the last link
        while (current.next != self.first):
            current = current.next  # move to next link
        current.next = new_link     # set the link before the "last"
        new_link.next = self.first  # after inserting, point back to first since circular
        
  # Find the Link with the given data (value)
  # or return None if the data is not there
  def find ( self, data ):
      # similar to find_unordered in regular linked list
      current = self.first
      # return none if list is empty
      if (current == None):
          return None
      # go to the next link if it is not data
      while (current.data != data):
          if (current.next == self.first): # return None if back to first link
              return None
          else:
              current = current.next    # move on
      # print("find",(current.data))
      return current

  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there
  def delete ( self, data ):
      # similar to delete link in regular linked list
      previous = self.first     # keep track of previous link
      current = self.first
      # return none if empty list
      if (current == None):
          return None
      # when the data is the only link on list, set it to none and return it
      elif (current.data == data and self.get_num_links() == 1):
          self.first = None
          return self.first
      else:
          # while previous is not last number keep setting it to next until last
          while (previous.next != self.first):
              previous = previous.next
          # keep going through list if data not found on current link
          while (current.data != data):
              # return none if back to first link and data still not found
              if (current.next == self.first):
                  return None
              else:
                  previous = current    # track link before current
                  current = current.next
      # when data deleting is the first link, set the first to next link so first is gone
      if (current == self.first):   
          self.first = self.first.next
      previous.next = current.next # skip (delete) current
      return current

  # Delete the nth Link starting from the Link start 
  # Return the data of the deleted Link 
  # AND return the next Link for the deleted Link
  def delete_after ( self, start, n ):
      current = self.find(start) # starting from set parameter not first link
      # return None if empty
      if (self.first == None):
          return None
      elif (self.get_num_links() == 1):   # when the link is 0 after deleting return none for next
          return (current.data, None)
      else:
          counter = 1   # start counter with one since next num is 2
          # move to next data if counter is not equal to elim_num
          while (counter != n):
              current = current.next
              counter += 1
      self.delete(current.data) # delete the data on elim_num
      return (current.data, current.next)   # return data deleted and next link

  # Return a string representation of a Circular List
  # The format of the string will be the same as the __str__ 
  # format for normal Python lists
  def __str__ ( self ):
      the_list = []
      # strng = ""    # create empty string
      current = self.first
      if (self.is_empty()):
          return str([])
      # when the cycle is not restarting, add the data to strng
      while (current.next != self.first):
          #strng += str(current.data) + " "
          the_list.append(current.data)
          current = current.next
      #strng += str(current.data)    # final data add
      the_list.append(current.data)
      return str(the_list)

  # helper function to see if list is empty
  def is_empty (self):
      if (self.first == None):
          return True
      else:
          return False
  
  # helper function to find length of list
  def get_num_links(self):
      length = 1 # start with one because skip first link
      if (self.first == self.first.next):
          return length
      current = self.first.next
      if (current == None): # return 0 if link is empty
          return 0
      # add one to length when the loop does not go back to first
      while (current != self.first):
          length += 1
          current = current.next
      return length

def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int (line)
  
  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int (line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int (line)

  # your code
  circular_list = CircularList() # create circular linked list
  data_deleted = [] # list to store deleted info
  # add number 1 to user selected num of soldiers to linked list
  for i in range (1, num_soldiers + 1):
      circular_list.insert(i)
  # print(circular_list.get_num_links())
  #print("Original List: ", circular_list)
  # delete by increments of elim_num until all soldiers except last are deleted
  for i in range(num_soldiers - 1):
      elim, start_count = circular_list.delete_after(start_count, elim_num)
      # start the next start count data after the deleted data
      start_count = start_count.data
      # print(circular_list)
      data_deleted.append(elim) # add the data deleted in list
  # add the last soldier to list
  data_deleted.append(circular_list.first.data)
  # print all the deleted data in order
  for elim in data_deleted:
      print(elim)
  # print(circular_list)
  # print(data_deleted)

if __name__ == "__main__":
  main()