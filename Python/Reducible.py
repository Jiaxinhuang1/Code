#  File: Reducible.py

#  Description: Program that finds the longest reducible word in text file

#  Student Name: Jiaxin Huang

#  Date Created: 03/31/2021

#  Date Last Modified:  04/01/2021

import sys
import math

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
    # similar to hash_word but with the step (constant)
    # stepSize = constant - (key % constant) while constant is prime less than size
    # and hash_word returns (hash_idx * 26 + letter) % size with since as a int inputed by user
    return const - (hash_word(s, const))

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
    # set the index of the initial position
    pos_idx = hash_word(s, len(hash_table))
    # assign random constant (prime smaller than size)
    constant = 11
    
    # if spot is empty, place the word in that pos
    if (hash_table[pos_idx] == " "):
        hash_table[pos_idx] = s
    # if the spot is not empty, use double hashing to find new spot
    elif (hash_table[pos_idx] != " "):
        # set index of next position in table and increment until empty spot is found
        # double hash formula (h1(key) + i * h2(key)) % (tablesize)
        next_idx = step_size(s, constant)
        i = 1
        while (hash_table[(pos_idx + i * next_idx) % len(hash_table)] != " "):
            i += 1
        # place s at that empty spot found by double hashing
        hash_table[(pos_idx + i * next_idx) % len(hash_table)] = s
        
# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
    # set index of the initial position
    pos_idx = hash_word(s, len(hash_table))
    # assign random constant (prime smaller than size)
    constant = 11
    # if word in table where initial index is at return true
    if (hash_table[pos_idx] == s):
        return True
    # if not, check the position of the double hashing
    elif (hash_table[pos_idx] != " "):
        next_idx = step_size(s, constant)
        i = 1
        # if that position is s then return true
        # double hash formula (h1(key) + i * h2(key)) % (tablesize)
        while (hash_table[(pos_idx + i * next_idx) % len(hash_table)] != " "):
            if (hash_table[(pos_idx + i * next_idx) % len(hash_table)] == s):
                return True
            i += 1
    else:
        return False


# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
    # if one letter word is a or i or o then return true if not, return false
    one_letter_words = ["a", "i", "o"]
    if (len(s) == 1):
        if (s in one_letter_words):
            return True
        else:
            return False
    # if word in hash_memo then return true
    elif find_word(s, hash_memo):
        return True
    # if word in hash_table then return true
    elif find_word(s, hash_table):
        for idx in range(len(s)):
            # if the word in hash_table and is reducible, then take one letter out
            # and check if reducible, if it is, add every reducible word to hash_memo
            if (is_reducible(s[:idx] + s[idx + 1:], hash_table, hash_memo)):
                insert_word(s, hash_memo)
                return True
    else:
        return False
    

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
    # assign max_len to smallest word length
    max_len = 1
    # if word in string_list is greater in length, change max_len to length of that word
    for word in string_list:
        if len(word) > max_len:
            max_len = len(word)
    
    max_len_words = []
    # if word length is equal to max_len, append to max_len_words list
    for word in string_list:
        if len(word) == max_len:
            max_len_words.append(word)
    return max_len_words


def main():
  # create an empty word_list
  word_list = []

  # read words from words.txt and append to word_list
  for line in sys.stdin:
    line = line.strip()
    word_list.append (line)
  # find length of word_list
  list_len = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
  prime_num = list_len * 2
  prime_found = False
  # continue to increment 1 to prime_num if prime is not found
  while not prime_found:
      if not is_prime(prime_num):
          prime_num += 1
      else:
          prime_found = True

  # create an empty hash_list
  hash_list = []

  # populate the hash_list with N blank strings
  for blank in range(prime_num):
      hash_list.append(" ")

  # hash each word in word_list into hash_list
  # for collisions use double hashing 
  for word in word_list:
      insert_word(word, hash_list)

  # create an empty hash_memo of size M
  hash_memo = []
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
  memo_len = math.ceil(0.2 * len(word_list)) # ceil changes num to int
  sec_prime_found = False
  # continue to increment 1 to memo_len if prime is not found
  while not sec_prime_found:
      if not is_prime(memo_len):
          memo_len += 1
      else:
          sec_prime_found = True

  # populate the hash_memo with M blank strings
  for blank in range(memo_len):
      hash_memo.append(" ")

  # create an empty list reducible_words
  reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  # as you recursively remove one letter at a time check
  # first if the sub-word exists in the hash_memo. if it does
  # then the word is reducible and you do not have to test
  # any further. add the word to the hash_memo.
  for word in word_list:
      if (is_reducible(word, hash_list, hash_memo)):
          reducible_words.append(word)

  # print(reducible_words)
  
  # find the largest reducible words in reducible_words
  largest_reducibles = get_longest_words(reducible_words)

  # print the reducible words in alphabetical order
  # one word per line
  largest_reducibles.sort()
  for word in largest_reducibles:
      print(word)

if __name__ == "__main__":
  main()