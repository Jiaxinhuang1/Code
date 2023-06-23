#  File: TestBinaryTree.py

#  Description: Program that contains helper functions of binary trees to
# find similar trees, nodes in level, height of tree, and number of nodes

#  Student Name: Jiaxin Huang

#  Date Created: 04/21/2021

#  Date Last Modified: 04/22/2021

import sys

class Node (object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree (object):
    def __init__ (self):
        self.root = None

    # print tree function in piazza
    def print_tree(self):
        self.print_tree_helper(self.root, 0)

    def print_tree_helper(self, aNode, space):
        SPACE = 5
        if (aNode != None):
            space += SPACE
            self.print_tree_helper(aNode.rchild, space)
            print()
            for i in range(SPACE, space):
                print(end = " ")
            print(aNode.data)
            self.print_tree_helper(aNode.lchild, space)

    # Insert data into the tree (code from class)
    def insert(self, data):
        new_node = Node(data)
        if (self.root == None): # if the tree is empty
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            # loop while the tree is not finished (get out of loop when found place to insert)
            while (current != None):
                # parent will be node on top of current when assigned current to l or r child
                parent = current  
                if (data < current.data):
                    current = current.lchild
                else:
                    current = current.rchild
            # found place to insert
            if (data < parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node

    # Returns true if two binary trees are similar
    def is_similar (self, pNode):
        my_list = []
        other_list = []
        # True if both trees are empty
        if ((self.root == None) and (pNode.root == None)):
            return True
        # False if the trees have different heights
        elif (self.get_height() != pNode.get_height()):
            return False
        # False if the trees have different number of nodes
        elif (self.num_nodes() != pNode.num_nodes()):
            return False
        # cheat function given in piazza (works but found another way)
        # elif (self.print_tree() == pNode.print_tree()):
            # return True
        else:
            # loop through all the levels
            for i in range(self.get_height()):
                # add all the nodes datas of both tree to a different list
                for aNode in self.get_level(i):
                    my_list.append(aNode.data)
                for aNode in pNode.get_level(i):
                    other_list.append(aNode.data)   
        # returns True if the lists are equal
        return (my_list == other_list)
            
    # Returns a list of nodes at a given level from left to right
    def get_level (self, level): 
        # used similar method as the brute force
        # empty list to store the nodes of the level
        node_list = []
        # return empty list if the tree is empty
        if ((self.root == None) or (self.get_height() == 0)):
            return node_list
        # return the list with only the root if the level looking for is the root level
        elif (level == 0):
            node_list.append(self.root)
            return node_list
        # return the list with all the data of the level appended
        else:
            self.get_level_helper(self.root, node_list, level, 0)
            return node_list
   
    # helper function to find the list of nodes at given level
    def get_level_helper (self, aNode, node_list, wanted_lvl, cur_lvl):
        # return if the tree is looked over or if passed wanted level
        if ((cur_lvl > wanted_lvl) or (aNode == None)):
            return
        # append all the node of the wanted lvl if it is on the current lvl
        elif (cur_lvl == wanted_lvl):
            node_list.append(aNode)
        else:
            # move on to the next level if it is not the wanted one
            self.get_level_helper(aNode.lchild, node_list, wanted_lvl, cur_lvl + 1)
            self.get_level_helper(aNode.rchild, node_list, wanted_lvl, cur_lvl + 1)

    # Returns the height of the tree
    def get_height (self): 
        # start from the root of the tree
        return self.get_height_helper(self.root)
    
    # helper function for getting the height of left and right
    def get_height_helper(self, aNode):
        # add 0 if to bottom of tree
        if (aNode == None):
            return 0
        # if not to bottom, choose the higher side and add one to it
        else:
            return 1 + max(self.get_height_helper(aNode.rchild), self.get_height_helper(aNode.lchild))
        

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):
        # use helper functions starting from root
        return self.num_nodes_helper(self.root)

    # helper function to count number of nodes left and right child of root
    def num_nodes_helper (self, aNode):
        # add 0 to count when get to bottom of tree
        if (aNode == None):
            return 0
        # when not to bottom, keep adding right and left 
        else:
            return 1 + self.num_nodes_helper(aNode.rchild) + self.num_nodes_helper(aNode.lchild)

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line)) 	# converts elements into ints
    # print(tree1_input)

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list (map (int, line)) 	# converts elements into ints
    # print(tree2_input)

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list (map (int, line)) 	# converts elements into ints
    # print(tree3_input)
    
    # create the trees
    tree_one = Tree()
    tree_two = Tree()
    tree_three = Tree()

    # insert all the data from the user input to the trees
    for num in tree1_input:
        tree_one.insert(num)
    for num in tree2_input:
        tree_two.insert(num)
    for num in tree3_input:
        tree_three.insert(num)

    # print(tree_one.print_tree())
    
    # Test your method is_similar()
    print("Testing is_similar tree_one and tree_two:", tree_one.is_similar(tree_two))
    print("Testing is_similar tree_two and tree_one:", tree_two.is_similar(tree_one))
    print("Testing is_similar tree_one and tree_three:", tree_one.is_similar(tree_three))
    print("Testing is_similar tree_two and tree_three:", tree_two.is_similar(tree_three))
    
    # Print the various levels of two of the trees that are different
    print("Testing get_level(3) of tree_one:", tree_one.get_level(3))
    print("Testing get_level(3) of tree_two:", tree_two.get_level(3))
    print("Testing get_level(0) of tree_one:", tree_one.get_level(0))
    print("Testing get_level(0) of tree_two:", tree_two.get_level(0))
    
    # Get the height of the two trees that are different
    print("Testing get_height of tree_one:", tree_one.get_height())
    print("Testing get_height of tree_two:", tree_two.get_height())
    print("Testing get_height of tree_three:", tree_three.get_height())

    # Get the total number of nodes a binary search tree
    print("Testing num_nodes of tree_one:", tree_one.num_nodes())
    print("Testing num_nodes of tree_two:", tree_two.num_nodes())
    print("Testing num_nodes of tree_three:", tree_three.num_nodes())

if __name__ == "__main__":
     main()