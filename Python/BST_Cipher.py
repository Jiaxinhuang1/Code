#  File: BST_Cipher.py

#  Description: Program that encrypts and decrypts strings
#  based on a certain key using binary trees

#  Student Name: Jiaxin Huang

#  Date Created: 04/20/2021

#  Date Last Modified: 04/21/2021

import sys

class Node (object):
    def __init__(self, ch):
        self.ch = ch
        self.lchild = None
        self.rchild = None

class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__ (self, encrypt_str):
        self.root = None
        lower = "abcdefghijklmnopqrstuvwxyz"    
        char_list = []
        # add char to list if its not in list and is a lower case letter or space
        for char in encrypt_str:
            if (char not in char_list):
                if ((char in lower) or (char == " ")):
                    char_list.append(char)
        # insert the char to tree
        for char in char_list:
            self.insert(char)
        
    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert (self, ch):
        # used code made in class
        new_node = Node(ch)
        # set root to new node if empty tree
        if (self.root == None): 
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            # loop while the tree is not finised (get out of loop when found place to insert)
            while (current != None):
                # parent will be node on top of current when assigned current to l or r child
                parent = current
                # keep going left if smaller
                if (ch < current.ch):
                    current = current.lchild
                # keep going right if bigger
                else:
                    current = current.rchild
            # insert left if smaller, insert right if bigger
            if (ch < parent.ch):
                parent.lchild = new_node
            else:
                parent.rchild = new_node


    # helper function to find the node with the given ch
    def search_helper(self, ch):
        # this is search function made in class
        current = self.root
        # loop while tree is not finished and data not found
        while ((current != None) and (current.ch != ch)):
            if (ch < current.ch):
                current = current.lchild
            else:
                current = current.rchild
        # when current is not empty and data is on current
        return current

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search (self, ch):
        strng = "" # create empty strng
        # return empty strng if ch not in tree
        if (self.search_helper(ch) == None):
            return strng
        else:
            current = self.root
            # if the ch is root add asterisk
            if (ch == current.ch):
                strng += "*"
            else:
                # loops until look over whole tree and current not found
                while ((current != None) and (current.ch != ch)):
                    # add < to strng and go left if ch is less
                    if (ch < current.ch):
                        strng += "<"
                        current = current.lchild
                    # add > to strng and go right if ch is more
                    elif (ch > current.ch):
                        strng += ">"
                        current = current.rchild
                # return empty strng check again if ch not found
                if (current == None):
                    return ""
        return strng

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding 
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse (self, st):
        # return the char in root if st equal to asterisk
        if (st == "*"):
            return self.root.ch
        else:
            current = self.root
            for sym in st:   
                # go left for every < in st and there is node on left
                if ((sym == "<") and (current.lchild != None)):
                    current = current.lchild
                # go right for every > in st and there is node on right
                elif ((sym == ">") and (current.rchild != None)):
                    current = current.rchild
                else:
                    return ""
        # after going through all st, return the current node ch
        return current.ch

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt (self, st):
        encrypted_strng = ""
        lower_strng = st.lower()    # convert strng to lowercase
        copy_strng = ""
        lower = "abcdefghijklmnopqrstuvwxyz"    
        # add char to copy_strng if is a lower case letter or space
        for char in lower_strng:
            if ((char in lower) or (char == " ")):
                copy_strng += char
        # add strngs of < or > or * depending on ch separated by a !
        for ch in copy_strng:
            encrypted_strng += self.search(ch) + "!"
        # return without the last !
        final_encrypted_strng = encrypted_strng[0:-1]
        return final_encrypted_strng

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt (self, st):
        decrypted_strng = ""   # empty strng to store result
        copy_strng = "" # empty strng to get rid of non <>!*
        strng_items = ["<", ">", "!", "*"]
        # add ch to copy_strng if its in strng_items
        for ch in st:
            if ch in strng_items:
                copy_strng += ch
        # split strng to list separated by !
        strng_list = copy_strng.split("!")
        # traverse (decrypt) through strngs in list and add it to resulting strng
        for ch in strng_list:
            decrypted_strng += self.traverse(ch)
        return decrypted_strng.strip()

def main():
    # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()

    # create a Tree object
    the_tree = Tree (encrypt_str)

    # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()

    # print the encryption
    print (the_tree.encrypt(str_to_encode))

    # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()
    
    # print the decryption
    print (the_tree.decrypt(str_to_decode))
 
if __name__ == "__main__":
    main()