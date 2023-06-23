import sys

class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))

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

  # Helper functions made in TestBinaryTree assignment
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


  # Returns a list containing the left view of the BST
  def get_left_view(self):
    #self.print_tree()
    left_list = []
    height = self.get_height()
    for i in range (height):
      left_list.append(self.get_level(i)[0].data)
    return left_list


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

    print(tree.get_left_view())

if __name__ == "__main__":
  main()