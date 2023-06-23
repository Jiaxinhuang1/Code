import sys

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # insert data into the tree
  def insert (self, data):
    new_node = Node (data)

    if (self.root == None):
      self.root = new_node
      return
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (data < current.data):
          current = current.lchild
        else:
          current = current.rchild

      # found location now insert node
      if (data < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # ***There is no reason to change anything above this line***

  # Returns an integer representing the sum of the leaf nodes
  def get_leaf_sum(self):
    height = self.get_height()
    nodes = []
    clean_nodes = []
    leaf_sum = 0
    for i in range(height):
      nodes.append(self.get_level(i))
    #print(nodes)
    for i in nodes:
      for node in i:
        clean_nodes.append(node)
    #print(clean_nodes)
    for node in clean_nodes:
      if (node.lchild == None and node.rchild == None):
        leaf_sum += node.data  
    return leaf_sum

  # Helper functions made for TestBinaryTree Assignment 
  # Returns a list of nodes data at a given level from left to right
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
# ***There is no reason to change anything below this line***

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree_input = list (map (int, line))    # converts elements into ints

    tree = Tree()
    for i in tree_input:
      tree.insert(i)

    print(tree.get_leaf_sum())

if __name__ == "__main__":
  main()