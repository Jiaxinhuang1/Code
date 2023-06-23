#  File: ExpressionTree.py

#  Description: Program that evalutes an infix expression and print the expression 
# in postfix and prefix order

#  Student Name: Jiaxin Huang

#  Date Created: 04/15/2021

#  Date Last Modified: 04/16/2021

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        # followed the steps on the assignment page
        # take in expression and break it into tokens
        tokens = expr.split(" ")
        # print (tokens)
        self.root = Node() # set root to empty node
        current = self.root # start with empty root node
        my_stack = Stack()  # create empty stack
        for token in tokens:
            # If the current token is a left parenthesis add a new node as the left child of the current node. 
            # Push current node on the stack and make current node equal to the left child.
            if (token == "("):
                current.lChild = Node()
                my_stack.push(current)
                current = current.lChild
            # If the current token is an operator set the current node's data value to the operator. 
            # Push current node on the stack. Add a new node as the right child of the current node 
            # and make the current node equal to the right child.
            elif (token in operators):
                current.data = token
                my_stack.push(current)
                current.rChild = Node()
                current = current.rChild
            # If the current token is a right parenthesis make the current node equal to the parent node
            # by popping the stack if it is not empty.
            elif (token == ")"):
                if (not my_stack.is_empty()):
                    current = my_stack.pop()
            # If the current token is an operand (integer or float), set the current node's data value 
            # to the operand and make the current node equal to the parent by popping the stack.
            else:
                current.data = eval(token)
                current = my_stack.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        # return the data of the node if it is not in operators (meaning its an operand)
        # isinstance returns true if aNode.data is an int or float
        if (isinstance(aNode.data, int)) or (isinstance(aNode.data, float)):
            return float(aNode.data)
        else:
            # continue operating on the left and right child based on the parent node
            if (aNode.data == "+"):
                return self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild)
            elif (aNode.data == "-"):
                return self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild)
            elif (aNode.data == "*"):
                return self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild)
            elif (aNode.data == "/"):
                return self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild)
            elif (aNode.data == "//"):
                return self.evaluate(aNode.lChild) // self.evaluate(aNode.rChild)
            elif (aNode.data == "%"):
                return self.evaluate(aNode.lChild) % self.evaluate(aNode.rChild)
            elif (aNode.data == "**"):
                return self.evaluate(aNode.lChild) ** self.evaluate(aNode.rChild)    

    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        # modified code from class
        if (aNode != None):
            # recursive : pre order traversal - center, left, right
            # stop when aNode == None
            return str(aNode.data) + " " + self.pre_order(aNode.lChild) + self.pre_order(aNode.rChild)
        else:
            return ""
    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        # modified code from class
        if (aNode != None):
            # recursive : post order traversal - left, right, center
            # stop when aNode == None
            return self.post_order(aNode.lChild) + self.post_order(aNode.rChild) + " " + str(aNode.data)
        else:
            return ""

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()