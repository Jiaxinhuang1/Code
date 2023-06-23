#  File: Palindrome.py

#  Description: Program that returns the smallest palindrome of a string

#  Student Name: Jiaxin Huang

#  Date Created: 02/25/2021

#  Date Last Modified: 02/25/2021

import sys
import math

# Function using recursive to check is string is palindrome
def isPalindrome(strng):
    if len(strng) == 0:
        # If the string is empty after all letters are check then is palindrom
        return True
    # Check each first and last letter to see if it is equal
    elif strng[0] == strng[-1]:
        # Go through the function again while deleting first and last letter
        return isPalindrome(strng[1:-1])
    else:
        return False

# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be 
#         made by adding characters to the start of the input string
def smallest_palindrome(str):
    # Create new string to store palindrome
    palin_str = ""
    # Duplicated string input to make delete letters when necessary 
    duplicate_str = str[::]
    # If string is palindrome return itself
    if isPalindrome(str):
        return str
    else:
        # Each time check if palindrome and add last letter to beginning if not
        while not isPalindrome(palin_str + str):
            palin_str += duplicate_str[-1]
            duplicate_str = duplicate_str[:-1]
        palin_str = palin_str + str
        return palin_str

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases
    assert smallest_palindrome("aa") == "aa"
    assert smallest_palindrome("cbabcde") == "edcbabcde"
    return "all test cases passed"

def main():
    # read the data
    # print(test_cases())
    for line in sys.stdin.readlines():
        strng = line.strip()
        palin = smallest_palindrome(strng)
        # print the smallest palindromic string that can be made for each input
        print(palin)

if __name__ == "__main__":
  main()