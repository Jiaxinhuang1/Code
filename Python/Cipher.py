#  File: Cipher.py

#  Description: Program that encrypts and decrypts strings using matrix rotation

#  Student Name: Jiaxin Huang

#  Date Created: 02/05/2021

#  Date Last Modified: 02/06/2021

# Input: string is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
import sys
import math

"""
Test Input:
gonewiththewind
osotvtnheitersec

Test Output:
itwgnhiodetnwhe
thecontestisover

"""

def encrypt ( strng ):
    encrypted = ""
    strng_list = []
    strng_matrix = []
    encrypted_matrix = []
    # Find the length of strng
    strng_len = len(strng)
    # Make the variable for length of final string
    # If length is a perfect square, set the variable as its final length
    if math.sqrt(strng_len).is_integer():
        next_sqr_num = strng_len
        next_small_sqrt = int(math.sqrt(next_sqr_num)) 
    # If the length is not a perfect square, find the next perfect square
    else:
        next_small_sqrt = math.floor(math.sqrt(strng_len)) + 1
        next_sqr_num = int(math.pow(next_small_sqrt, 2))
    # Add asterisks to fill in the string if original length is not square num
    if strng_len < next_sqr_num:
        asterisks_needed = next_sqr_num - strng_len
        for i in range(asterisks_needed):
            strng = strng + '*'
    # Add all characters in strng to a list
    for char in strng:
        strng_list.append(char)
    # Convert the strng list into a 2D list or matrix
    # Dimensions will be the squareroot of the length of string
    index = 0
    for row in range(next_small_sqrt):
        strng_matrix.append([])
        for col in range(next_small_sqrt):
            strng_matrix[row].append(strng_list[index])
            index += 1
    # Encryption starts
    # Rotate the 90 degrees clockwise byappending it new new list
    # Position found by placing original characters into different positions
    for i in range(len(strng_matrix)):
        encrypted_matrix.append([])
        num = len(strng_matrix)
        for j in range(len(strng_matrix[0])):
            num -= 1
            encrypted_matrix[i].append(strng_matrix[num][i])
    # Loop through each character in 2D list and add it to empty string
    for row in range(len(encrypted_matrix)):
        for col in range(len(encrypted_matrix)):
            encrypted = encrypted + encrypted_matrix[row][col]
    # Create a new empty string for final result
    # Add character to new empty string if it is not asterisk
    encrypted_strng = ""
    asterisk = '*'
    if asterisk not in encrypted:
        return encrypted
    for i in range(len(encrypted)):
        if encrypted[i] != asterisk:
            encrypted_strng += encrypted[i]
    return encrypted_strng

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):
    decrypted = ""
    strng_list = []
    strng_matrix = []
    decrypted_matrix = []
    # Find the length of strng
    strng_len = len(strng)
    # Make the variable for length of final string
    # If length is a perfect square, set the variable as its final length
    if math.sqrt(strng_len).is_integer():
        next_sqr_num = strng_len
        next_small_sqrt = int(math.sqrt(next_sqr_num)) 
    # If the length is not a perfect square, find the next perfect square
    else:
        next_small_sqrt = math.floor(math.sqrt(strng_len)) + 1
        next_sqr_num = int(math.pow(next_small_sqrt, 2))
    # Add asterisks to fill in the string if original length is not square num
    if strng_len < next_sqr_num:
        asterisks_needed = next_sqr_num - strng_len
        for i in range(asterisks_needed):
            strng = strng + '*'
    # Add all characters in strng to a list
    for char in strng:
        strng_list.append(char)
    # Convert the strng list into a 2D list or matrix
    # Dimensions will be the squareroot of the length of string
    index = 0
    for row in range(next_small_sqrt):
        strng_matrix.append([])
        for col in range(next_small_sqrt):
            strng_matrix[row].append(strng_list[index])
            index += 1
    # Decryption starts
    # Rotate the 90 degrees counterclockwise by appending it new new list
    # Position found by placing original characters into different positions
    num = len(strng_matrix)
    for i in range(len(strng_matrix)):
        decrypted_matrix.append([])
        num -= 1
        for j in range(len(strng_matrix[0])):
            decrypted_matrix[i].append(strng_matrix[j][num])
    # Loop through each character in 2D list and add it to empty string    
    for row in range(len(decrypted_matrix)):
        for col in range(len(decrypted_matrix)):
            decrypted = decrypted + decrypted_matrix[row][col]
    # Create a new empty string for final result
    # Add character to new empty string if it is not asterisk
    decrypted_strng = ""
    asterisk = '*'
    if asterisk not in decrypted:
        return decrypted
    for i in range(len(decrypted)):
        if decrypted[i] != asterisk:
            decrypted_strng += decrypted[i]
    return decrypted_strng

def main():
  # read the two strings P and Q from standard imput
    strng_to_encrypt = sys.stdin.readline().strip()
    strng_to_decrypt = sys.stdin.readline().strip()
  # encrypt the string P
    encrypted_strng = encrypt(strng_to_encrypt)
  # decrypt the string Q
    decrypted_strng = decrypt(strng_to_decrypt)
  # print the encrypted string of P and the 
  # decrypted string of Q to standard out
    print(encrypted_strng)
    print(decrypted_strng)


if __name__ == "__main__":
  main()