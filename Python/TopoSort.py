#  File: TopoSort.py

#  Description: Program that checks if there is a cycle in the graph
# and topologically sorts it alphabetically.

#  Student Name: Jiaxin Huang

#  Date Created: 04/29/2021

#  Date Last Modified: 04/30/2021

import sys

class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        #if not Stack.is_empty(self):
        return self.stack.pop()

    # check the item on the top of the stack without removing
    def peek(self):
        return self.stack[-1]

    # check if the stack is empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))

class Queue (object):
    def __init__ (self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        if (not self.is_empty()):
            return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty (self):
        return (len (self.queue) == 0)

    # return the size of the queue
    def size (self):
        return (len (self.queue))

    # check the item at the top of the queue without removing it
    def peek (self):
        return self.queue[0]

# graphs have vertices
class Vertex (object):
    def __init__ (self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited (self):
        return self.visited
    
    # determine what the label is
    def get_label (self):
        return self.label

    # string representation of vertex 
    def __str__ (self):
        return str(self.label)

class Graph (object):
    def __init__ (self):
        self.Vertices = []      # list of Vertex objects
        self.adjMat = []        # adjacency matrix that defins all the edges
    
    # check if a vertex is already in the graph
    def has_vertex (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):     # sequencial search to check if vertex in graph
            if (label == self.Vertices[i].get_label()):
                return True
        return False    # vertex not found after searching whole list

    # get the index from the vertex label
    def get_index (self, label):
        nVert = len(self.Vertices)
        for i in range (nVert):       # sequencial search to return index of label
            if (label == self.Vertices[i].get_label()):
                return i
        return -1       # not found

    # add a Vertex object with a given label to the graph
    def add_vertex (self, label):
        self.Vertices.append (Vertex(label))    # add a new label to the list
        # add a new column in the adjacency matrix
        nVert = len (self.Vertices)
        for i in range (nVert - 1):
            self.adjMat[i].append(0)    # adds a zero in the end of each row
        # add a new row for the new vertex
        new_row = []
        for i in range (nVert):
            new_row.append(0)       # adds nVert number of zeros on the new_row
        self.adjMat.append(new_row)     # add the new_row to the adjacency matrix
    
    # add weighted directed edge to graph
    def add_directed_edge (self, start, finish, weight = 1):
        # change the 0 to weight value at the position connecting the start and finish
        self.adjMat[start][finish] = weight   

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight (self, fromVertexLabel, toVertexLabel):
        # set weight equal to the position based on the index of the labels
        weight = self.adjMat[self.get_index(fromVertexLabel)][self.get_index(toVertexLabel)]
        if (weight != 0):    # if weight is not 0 then there is a edge
            return weight
        else:
            return -1

    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none
    def get_neighbors (self, vertexLabel):
        neighbors = []      # create a new list
        nVert = len (self.Vertices)
        # find idx of the given vertexLabel
        idx = self.get_index(vertexLabel)
        # add the vertex to the list for all the vertices in this row
        # if the weight at that connection is not 0 (theres an edge)
        for i in range (nVert):
            if (self.adjMat[idx][i] != 0):
                neighbors.append(self.Vertices[i])
        # add the vertex to the list for all vertices in this column
        # if the weight is not 0 and vertex is not in the list already
        for i in range (nVert):
            if (self.adjMat[i][idx] != 0) and (self.adjMat[i][idx] not in neighbors):
                neighbors.append(self.Vertices[i])
        return neighbors

    # return an index to an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex (self, v):
        nVert = len (self.Vertices)
        # return index of the vertex that contains an edge from v and is not visited
        for i in range (nVert):
            if (self.adjMat[v][i] > 0) and (not self.Vertices[i].was_visited()):
                return i
        return -1

    # return an index to an visited vertex adjacent to vertex v (index)
    def get_adj_visited_vertex (self, v):
        nVert = len (self.Vertices)
        # return index of the vertex that contains an edge from v and is not visited
        for i in range (nVert):
            if (self.adjMat[v][i] > 0) and (self.Vertices[i].was_visited()):
                return i
        return -1

    # get a copy of the list of Vertex objects
    def get_vertices (self):
        vertices_copy = []
        # add all the vertices in the Vertices list to the new list
        for vertex in self.Vertices:
            vertices_copy.append(vertex)
        return vertices_copy

    # do a depth first search in a graph starting at vertex v (index)
    def dfs (self, v):
        # create the Stack object
        theStack = Stack()
        # mark the vertex v as visited and push it on the stack
        self.Vertices[v].visited = True
        print(self.Vertices[v])
        theStack.push(v)
        # visit the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex (theStack.peek())
            if (u == -1):       # there is no adjacent vertex that I have not visited
                u = theStack.pop()      # backtracking happens when you are popping the stack
            else:
                self.Vertices[u].visited = True     # make it visited to keep track
                print (self.Vertices[u])
                theStack.push(u)
        # clean up to make the stacks unvisited again for use next time
        # the stack is empty let us reset the flags
        nVert = len(self.Vertices)
        for i in range (nVert):
            self.Vertices[i].visited = False

    # do a breadth first search in a graph starting at vertex v (index)
    def bfs (self, v):  # used pseudocode from Apr 21st class lecture similar to dfs
        # create a queue object
        theQueue = Queue()
        # Select a starting vertex. Make it the current vertex. Mark it visited
        self.Vertices[v].visited = True
        print (self.Vertices[v])
        theQueue.enqueue(v) # only prints Houston if not enqueued
        # Visit and adjacent unvisited vertex (if there is one) in order from the current vertex.
        # Mark it visited and insert it into the queue.
        while (not theQueue.is_empty()):
            u = self.get_adj_unvisited_vertex (theQueue.peek())
            if (u == -1):       # there is no adjacent vertex that i have not visited
                u = theQueue.dequeue()
            else:
                self.Vertices[u].visited = True
                print(self.Vertices[u])
                theQueue.enqueue(u)
                
        # the queue is empty let us reset the flags
        nVert = len(self.Vertices)
        for i in range (nVert):
            self.Vertices[i].visited = False

    # delete an edge from the adjacency matrix
    # delete a single edge if the graph is directed
    # delete two edges if the graph is undirected
    def delete_edge (self, fromVertexLabel, toVertexLabel):
        # go to the position and make the adjMat 0 for 2 areas different start and end
        self.adjMat[self.get_index(fromVertexLabel)][self.get_index(toVertexLabel)] = 0
        self.adjMat[self.get_index(toVertexLabel)][self.get_index(fromVertexLabel)] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex (self, vertexLabel):
        # delete the column and row of that index
        idx = self.get_index(vertexLabel)   # find index of the label
        nVert = len(self.Vertices)
        # delete the row of the vertex
        del self.adjMat[idx]
        # delete every edge that is in the idx column
        for i in range (nVert - 1):
            del self.adjMat[i][idx]
        # delete the vertex in the Vertices list
        for vertex in self.Vertices:
            if (vertex.get_label() == vertexLabel):
                del self.Vertices[idx]

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def has_cycle (self):
        # create the Stack object
        result = []
        # used the code from dfs but append result to list rather than print
        theStack = Stack()
        # mark the vertex v as visited and push it on the stack
        self.Vertices[0].visited = True
        result.append(self.Vertices[0].label)
        theStack.push(0)
        # visit the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex (theStack.peek())
            if (u == -1):       # there is no adjacent vertex that I have not visited
                u = theStack.pop()      # backtracking happens when you are popping the stack
            else:
                self.Vertices[u].visited = True     # make it visited to keep track
                result.append(self.Vertices[u].label)
                theStack.push(u)
        # clean up to make the stacks unvisited again for use next time
        # the stack is empty let us reset the flags
        nVert = len(self.Vertices)
        for i in range (nVert):
            self.Vertices[i].visited = False
        sorted_res = sorted(result)     # has cycle if the list does not change
        return sorted_res == result
    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort (self):
        sort_list = []  # created new list for final result
        # fin_round = False
        nVert = len (self.Vertices)
        # continue to loop if all the letters is not in the sort_list
        while len(sort_list) < nVert:
            # print ("new round")
            num_deg_list = []
            # count the number of in degrees each vertex contains by checking
            # if the edge weight at that position is greater than 0
            for idx in range (len (self.Vertices)):
                deg_count = 0
                for j in self.adjMat:
                    if j[idx] > 0:
                        deg_count += 1
                num_deg_list.append(deg_count)
                deg_count = 0
            #print (num_deg_list)
            num_zero = num_deg_list.count(0)    # stores how many vertex has in degree of 0
            #print(num_zero)
            part_list = []  # created new list for partial result
            # loop through all the degree in the list
            for deg in range (len(num_deg_list)):
                # add to part list if the in degree is 0
                if num_deg_list[deg] == 0:
                    part_list.append(self.Vertices[deg].label)
                # break from the loop if the num of vertex in part_list is equal to the num of vertex with 0 as in degree
                elif num_zero == len(part_list):
                    break
            # delete all the vertex in the part_list from the graph
            for label in part_list:
                self.delete_vertex(label)
            # sort the partial list 
            #print(part_list)    
            part_list.sort()    # sort each deleted small list (each round) alphabetically
            #print(part_list)
            # add the results in the partial list to the final list
            for let in part_list:
                sort_list.append(let)
            part_list = []  # empty out the partial list for reuse
        return sort_list 
                    
def main():
    # create a Graph object
    theGraph = Graph()
    # read the number of vertices
    line = sys.stdin.readline().strip()
    num_vertices = int (line)
    # add the vertices to the graph
    for i in range (num_vertices):
        letter = sys.stdin.readline().strip()
        theGraph.add_vertex(letter)
    # get the number of edges
    line = sys.stdin.readline().strip()
    num_edges = int(line)
    # read the edges and add to the graph
    for i in range (num_edges):
        edge = sys.stdin.readline().strip()
        edge = edge.split()
        fromVertex = theGraph.get_index(edge[0])
        toVertex = theGraph.get_index(edge[1])
        theGraph.add_directed_edge(fromVertex, toVertex)

    # test if a directed graph has a cycle
    if (theGraph.has_cycle()):
        print ("The Graph has a cycle.")
    else:
        print ("The Graph does not have a cycle.")

    # test topological sort
    if (not theGraph.has_cycle()):
        vertex_list = theGraph.toposort()
        print ("\nList of vertices after toposort")
        print (vertex_list)

main()