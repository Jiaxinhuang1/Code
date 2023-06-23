#  File: FullTree.py

#  Description: Program that checks whether the binary tree is full or not

#  Student Name:  Jiaxin Huang

#  Date Created: 05/07/2021

#  Date Last Modified:  05/07/2021


class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  # the only parameter for the Tree class is self.root, which is a Node object
  # a printlevelorder method has been provided to help with debugging

  # complete the isFull method below and return a boolean
  def isFull(self):
    #self.printlevelorder()
    #print(self.get_height())
    height = self.get_height()
    lst_node = self.get_level(height - 2)
    if (height == 1):
      return True
    #print(lst_node)
    for aNode in lst_node:
      if (aNode.lchild == None and aNode.rchild != None) or (aNode.lchild != None and aNode.rchild == None):
        return False
      else:
        return True
      
  
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


  # **there is no reason to change anything below this line**
    
  # prints each level in the tree separately
  # a _ character indicates that there is no node there
  def printlevelorder(self):
    def get_height_helper (aNode):
      if aNode == None:
        return 0
      else:
        return max(get_height_helper(aNode.lchild), get_height_helper(aNode.rchild)) + 1

    def printGivenLevel(root, level):
      if level == 1:
        if root is None:
          print('_', end = ' ')
        else:
          print(root.data, end = ' ')
      elif root is None:
        return root
      elif level > 1:
        printGivenLevel(root.lchild, level - 1)
        printGivenLevel(root.rchild, level - 1)

    h = get_height_helper(self.root)
    for i in range(1, h + 1):
        printGivenLevel(self.root, i)
        print()

  # creates a tree from a list input
  def __init__ (self, tree_list):
    if len(tree_list) == 0 or tree_list[0] == None:
      self.root = None
      return
    self.root = Node(tree_list[0])
    node_objs = [None]
    tree_list.insert(0, None)
    node_objs.append(self.root)
    for i in range(2, len(tree_list)):
      if tree_list[i] != None:
        parent_ind = i // 2
        parent_node = node_objs[parent_ind]
        new_node = Node(tree_list[i])
        # for error checking
        if parent_node != None:
          if i == parent_ind * 2:
            parent_node.lchild = new_node
          else:
            parent_node.rchild = new_node
          node_objs.append(new_node)
        else:
          node_objs.append(None)
      else:
        node_objs.append(None)

import sys
def main():
  # create the tree
  tree_list = sys.stdin.readlines()
  for i in range(len(tree_list)):
    tree_list[i] = tree_list[i].strip()
    if tree_list[i] == "None":
      tree_list[i] = None
    
  tree = Tree(tree_list)

  print (tree.isFull())

if __name__ == "__main__":
  main()
