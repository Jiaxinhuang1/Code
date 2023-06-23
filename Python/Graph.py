#  File: Graph.py

#  Description: Program that creates a graph a cities and allows the user to
# delete a connection or city

#  Student Name: Jiaxin Huang

#  Date Created: 04/27/2021

#  Date Last Modified: 04/28/2021

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
        return False    # vertex not found after searching whole lise

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

    # add weighted undirected edge to graph
    def add_undirected_edge (self, start, finish, weight = 1):
        # in undirected, you can go from start to finish and finish to start
        # change the two 0 to weight value
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

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

def main():
    # create a Graph object
    cities = Graph()
    # read the number of vertices
    line = sys.stdin.readline().strip()
    num_vertices = int(line)
    # add the vertices to the graph
    for i in range (num_vertices):
        city = sys.stdin.readline().strip()
        cities.add_vertex(city)
    # get the number of edges
    line = sys.stdin.readline().strip()
    num_edges = int(line)
    # read the edges and add to the graph
    for i in range (num_edges):
        edge = sys.stdin.readline().strip()
        edge = edge.split()
        start = int(edge[0])
        finish = int(edge[1])
        weight = int(edge[2])
        cities.add_directed_edge(start, finish, weight)
    
    # test depth first search
    start_vertex = sys.stdin.readline().strip()     # read the starting vertex for dfs and bfs
    start_index = cities.get_index (start_vertex)   # get the index of the starting vertex
    print ("Depth First Search")
    cities.dfs(start_index)
    print()
    # test breadth first search
    print ("Breadth First Search")
    cities.bfs(start_index)
    print()
    # test deletion of an edge
    line = sys.stdin.readline().strip()     # read the from and to label of the edge to be deleted
    edges = line.split()        # split it into list
    fromVertex = edges[0]       # set the from and to label
    toVertex = edges[1]
    print("Deletion of an edge")
    cities.delete_edge(fromVertex, toVertex)
    # print the adjacency matrix of the graph with deleted edge
    print("\nAdjacency Matrix")
    for i in range (num_vertices):
        for j in range (num_vertices - 1):
            print(cities.adjMat[i][j], end = " ")
        print(cities.adjMat[i][num_vertices - 1], end = "")
        print()
    print()
    # test deletion of a vertex
    vertex_to_del = sys.stdin.readline().strip()    # read the vertex to be deleted
    print ("Deletion of a vertex")
    cities.delete_vertex(vertex_to_del)
    print()
    # print the list of vertices after the user selected vertex is deleted
    print("List of Vertices")
    for vertex in cities.Vertices:
        print(vertex)
    print()
    # print the adj matrix after the user selected vertex is deleted
    print("Adjacency Matrix")
    for i in range (num_vertices - 1):
        for j in range (num_vertices - 2):
            print(cities.adjMat[i][j], end = " ")
        print(cities.adjMat[i][num_vertices - 2], end = "")
        print()
    print()

if __name__ == "__main__":
    main()