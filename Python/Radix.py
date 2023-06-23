#  File: Radix.py

#  Description: Program that uses radix sort to sort a 
# string with a mix of numbers and letters using queues in lexical order

#  Student Name:  Jiaxin Huang

#  Date Created:  04/01/2021

#  Date Last Modified:  04/06/2021

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
  digits_place = 1 # keep track of what digits place working with
  is_sorted = False # controls when to exit loop
  # represent the queues
  characters = "0123456789abcdefghijklmnopqrstuvwxyz"
  max_length = 0 # assigns the max word length in list
  balance = []  # list containing trailing asterisks to balance word length
  ast_str = "" 
  # loops through list to find the max word length
  for word in a:
    if (len(word) > max_length):
        max_length = len(word)
  
  # Add asterisk at at end of short words to match the max word length
  for word in a:
    if (len(word) < max_length):
        diff = max_length - len(word)
        for ast in range(diff):
            ast_str += "*"
        word =  word + ast_str
    # append the new balanced word to new list and empty the strng 
    balance.append(word)
    ast_str = "" 

  # if the list is not sorted, keep going through every character
  while not is_sorted:
    # create a 2D list of queues to store strings digit by digit
    queues = []
    for i in range(len(characters)):
      queues.append([])
    # loop through each string in given list
    for word in balance:
      word_str = str(word) # convert the word to string 
      # add to the queue 0 if the word is shorter than the current digits place
      if(digits_place > len(word_str)): 
        queues[0].append(word)
      # if the word is equal to or less than the digits place then..
      else:
        word_let = word_str[-digits_place] # assign the character working with currently from right to left
        # if the current char is * then the word digit is 0 so add to queue 0
        if (word_let == "*"):
            word_digit = 0
        else:
            # else find the index of the current character in the characters string
            word_digit = find_idx(characters, word_let) 
        queues[word_digit].append(word) # add the word to the queue based on index 

    # list is sorted when the first queue contains all the words 
    if(len(queues[0]) == len(balance)):
      is_sorted = True
    # if its not sorted, empty the list and add the current pass
    # keep occuring until all the words are inside queue
    balance = []
    for queue in queues:
      for word in queue:
        balance.append(word)
    digits_place += 1 # move on to the next digit

  # when the list is sorted (condition for exiting while loop)
  if is_sorted:
      result = [] 
      # create empty list and add the cleaned strng (without the asterisk) inside and return
      for word in balance:
          clean_word = clean_str(word)
          # print(clean_word)
          result.append(clean_word)
      return result 

# helper function to find the index of a letter in strng 
def find_idx(strng, key):
  return strng.index(key)

# helper function to clean up the strng by removing trailing asterisks
def clean_str(strng):
    if strng[-1] != "*":
        return strng
    else:
        return clean_str(strng[:-1])

def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  
  # print word_list
  #print (word_list)
  

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()

    
