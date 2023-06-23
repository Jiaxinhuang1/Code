#  File: TestLinkedList.py

#  Description: Program that contains helper functions for the LinkedList class

#  Student Name: Jiaxin Huang

#  Date Created: 04/07/2021

#  Date Last Modified: 04/07/2021

import random
class Link (object):
  def __init__ (self, data, next = None):
      self.data = data
      self.next = next

class LinkedList (object):
  # create a linked list
  # you may add other attributes
  def __init__ (self):
      self.first = None # start with empty link

  # get number of links 
  def get_num_links (self):
      length = 0    # set count variable
      current = self.first
      if (current == None): # return 0 if empty list
          return 0
      while (current != None):   # increment length and move to next link when not end
          length += 1
          current = current.next
      return length    
  
  # add an item at the beginning of the list
  def insert_first (self, data):
      new_link = Link(data) # create a new link
      new_link.next = self.first # put previous first link to next link
      self.first = new_link # set the newly created link as first link

  # add an item at the end of a list
  def insert_last (self, data): 
      new_link = Link(data) # create new link
      current = self.first # set current as first link
      if (current == None):   # if the link is empty, added link = first link is the last
          self.first = new_link
          return
      while (current.next != None): # if not at last link
          current = current.next # move to next link
      current.next = new_link # when at last link, set the new link at end

  # add an item in an ordered list in ascending order
  # assume that the list is already sorted
  def insert_in_order (self, data): 
      new_link = Link(data)     # create a new link
      previous = self.first     # keep track of previous link
      current = self.first 
      # insert data to the beginning when empty list or data value less than first data
      if (current == None) or (data <= current.data):
          self.insert_first(data)
          return
      # loop through all the data when data bigger than current (start with first link)
      while (data > current.data):
          if(current.next == None): # insert data to last if current link is last in list
              self.insert_last(data)
              return
          else: # if it is not last, move on in the list
              previous = current
              current = current.next
      # when data is less than or equal to current data
      # place data before the current data
      previous.next = new_link  
      new_link.next = current


  # search in an unordered list, return None if not found
  def find_unordered (self, data): # sequential search
      current = self.first  # set current as first link
      if (current == None): # return none if empty 
          return None   
      while (current.data != data):  # go to next link if it is not data
          if(current.next == None): # return none if reached the end
              return None
          else:
              current = current.next    # set current to next link if not end
      return current    # return current (address: memory location) when found data

  # Search in an ordered list, return None if not found
  def find_ordered (self, data):   
      # same code as the find_unordered (sequential search) with small additions
      current = self.first
      if (current == None):
          return None
      while (current.data != data):
          if(current.next == None):
              return None
          else:
              # since ordered, not there if next link data is greater than data
              if(current.data > data): 
                  return None
              current = current.next    
      return current

  # Delete and return the first occurrence of a Link containing data
  # from an unordered list or None if not found
  def delete_link (self, data):  # take pointer of the previous link and attach to link after current
      previous = self.first   # keep track of previous link
      current = self.first
      if (current == None): # return none if empty list
          return None
      while (current.data != data):    # go to next link if not data
          if(current.next == None): # return none is last link
              return None
          else:
              previous = current    # track link before current
              current = current.next
      # found data
      if (current == self.first):   # when it is first link, set first to next
          self.first = self.first.next 
      else:
          previous.next = current.next  # when not first link, skip current
      return current # return what is deleted

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
      strng = "" # create empty string
      count_line = 0     # create variable to count how many data in line
      current = self.first
      # return empty string if list is empty
      if (self.is_empty()):
          return ""
      else:
          # add all the data in the list to the string
          for i in range(self.get_num_links()):
              # if the current is lask link, no spaces after strng of data
              if (current.next == None):
                  strng += str(current.data)
                  count_line += 1
              else:
                  # if need to switch line after, no spaces after strng of data
                  if (count_line + 1 == 10):
                      strng += str(current.data)
                      current = current.next
                      count_line += 1
                  else:
                    strng += str(current.data) + "  "
                    current = current.next
                    count_line += 1    # increment for every data added
              # move to the next line when there is 10 data in line
              if (count_line == 10):
                  count_line = 0 # reset the count
                  strng += "\n"
      return strng

  # Copy the contents of a list and return new list
  # do not change the original list
  def copy_list (self):
      copy_list = LinkedList() # create new list
      current = self.first
      # when not end of list, keep adding to end of new list
      # so that first added is at beginning and last added is at end
      while (current != None): 
          copy_list.insert_last(current.data)
          current = current.next # move on to next link
      return copy_list

  # Reverse the contents of a list and return new list
  # do not change the original list
  def reverse_list (self): 
      reversed_list = LinkedList()  # create new list
      current = self.first
      # when not end of list, keep adding to the beginning of new list
      # so that first added is at end and last added is at beginning (reversed)
      while (current != None):
          reversed_list.insert_first(current.data)
          current = current.next
      return reversed_list 

  # Sort the contents of a list in ascending order and return new list
  # do not change the original list
  def sort_list (self): 
      sorted_list = LinkedList()    # create new list
      current = self.first
      if (current == None):     # return the list as it is if orignal list is empty
          return sorted_list
      # insert all the original list data in order
      for i in range(self.get_num_links()): 
          sorted_list.insert_in_order(current.data)
          current = current.next
      return sorted_list

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
      # list is sorted if the sorted list is equal to the copy of original list
      if (self.sort_list().is_equal(self.copy_list())):
          return True
      else:
          return False
      
  # Return True if a list is empty or False otherwise
  def is_empty (self): 
      if(self.first == None):   # is empty when first link is None
          return True
      else:
          return False

  # Merge two sorted lists and return new list in ascending order
  # do not change the original lists
  def merge_list (self, other): 
      merged_list = LinkedList() # create a new list
      # set current link working with for both list
      my_current = self.first
      other_current = other.first
      # return a sorted version of other list is self list is empty
      if (my_current == None):
          return other.sort_list()
      # return a sorted version of self list if other list is empty
      elif (other_current == None):
          return self.sort_list()
      else:
          # insert in order all the data from self list
          for i in range(self.get_num_links()):
              merged_list.insert_in_order(my_current.data)
              my_current = my_current.next
          # insert in order all the data from other list
          for i in range(other.get_num_links()):
              merged_list.insert_in_order(other_current.data)
              other_current = other_current.next
      return merged_list


  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
      # if the length of the list is not equal, list not equal
      if (self.get_num_links() != other.get_num_links()):
          return False
      # if both list is empty, lists equal
      elif (self.is_empty() and other.is_empty()):
          return True
      # if all the data from beginning to end is equal, lists are equal
      else:
          # set the link working with on both sides
          my_current = self.first
          other_current = other.first
          # check if all the data on both lists are equal
          for i in range(self.get_num_links()):
              if (my_current.data != other_current.data):   # not equal if data not equal
                  return False
              else:
                  # move on to the next data
                  my_current = my_current.next
                  other_current = other_current.next
      return True   # equal if finished comparing all the data

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  # do not change the original list
  def remove_duplicates (self):
      unique_list = LinkedList()    # create a new linked list
      current = self.first  
      datas = []    # create list to store unique data (no repeated)
      # if list is empty, return the newly created empty list
      if (current == None):
          return unique_list
      # for all the data in linked list
      for i in range(self.get_num_links()):
          # add the current data of linked list to datas list if it is not already there
          if(current.data not in datas):
              datas.append(current.data)
          current = current.next    # move on to the next link
      # insert the data in datas list to the new linked list
      for data in datas:
          unique_list.insert_last(data)
      return unique_list

    
def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
  test_list = LinkedList()
  for i in range(1, 15):
      test_list.insert_first(i)
  print("Testing insert_first: \n", test_list, sep = "")
  print()
  # Test method insert_last()
  test_list_2 = LinkedList()
  for i in range(2, 26, 2):
      test_list_2.insert_last(i)
  print("Testing insert_last: \n", test_list_2, sep = "")
  print()
  # Test method insert_in_order()
  test_list_2.insert_in_order(15)
  print("Testing insert_in_order: \n", test_list_2, sep = "")
  print()

  # Test method get_num_links()
  print("Testing get_num_link:", test_list.get_num_links())
  print()

  # Test method find_unordered() 
  # Consider two cases - data is there, data is not there 
  test_list_random = LinkedList()
  for i in range(15):
      test_list_random.insert_first(random.randint(10, 100))
  test_list_random.insert_in_order(50)

  print("Printing Random List: \n", test_list_random, sep = "")
  print()
  print("Testing find_unordered data not there: ", test_list_random.find_unordered(123))
  print("Testing find_unordered data there: ", test_list_random.find_unordered(50))
  print()

  # Test method find_ordered() 
  # Consider two cases - data is there, data is not there 
  print("Testing find_ordered data not there: ", test_list_2.find_ordered(123))
  print("Testing find_ordered data there: ", test_list_2.find_ordered(20))
  print()

  # Test method delete_link()
  # Consider two cases - data is there, data is not there 
  print("Testing delete_link data not there: ", test_list_random.delete_link(123))
  print("Testing delete_link data there: ", test_list_random.delete_link(50))
  print("Random List After Deleting: \n", test_list_random, sep = "")
  print()
  # Test method copy_list()
  print("Testing copy_list: \n", test_list.copy_list(), sep = "")
  print()

  # Test method reverse_list()
  print("Testing reverse_list: \n", test_list.reverse_list(), sep = "")
  print()
  # Test method sort_list()
  print("Testing sort_list: \n", test_list_random.sort_list(), sep = "")
  print()

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  print("Testing is_sorted false: ", test_list_random.is_sorted())
  print("Testing is_sorted true: ", test_list_2.is_sorted())
  print()

  # Test method is_empty()
  print("Testing is_empty: ", test_list.is_empty())
  print()

  # Test method merge_list()
  print("Testing merged_list: \n", test_list.merge_list(test_list_2), sep = "")
  print()

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  print("Testing is_equal false: ", test_list.is_equal(test_list_random))
  print("Testing is_equal true: ", test_list.is_equal(test_list.copy_list()))
  print()

  # Test remove_duplicates()
  merged_list = test_list.merge_list(test_list_2)
  print("Testing remove_duplicates: \n", merged_list.remove_duplicates(), sep = "")
  
if __name__ == "__main__":
  main()