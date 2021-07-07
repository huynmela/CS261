# Course: CS261 - Data Structures
# Author: Melanie Huynh
# Assignment: Assignment 6, Directed graph
# Description: A directed graph implementation. Uses a adjacency matrix.

import heapq
from collections import deque

class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        This method adds a new vertex to the graph. Name does not need to be provided.
        """
        # Need to modify the adj_matrix list of list to include an extra vertex
        self.adj_matrix = [[0] * (self.v_count + 1) for i in range(self.v_count + 1)] # initialized with no weight, list comprehension
        self.v_count += 1
        return self.v_count #+= 1 # returns the number of vertices plus the added
        

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        This method adds a new edge to the graph, connecting two vertices with provided indices.
        """
        # if either or both vertices DNE as in outside of matrix rows and columns, do nothing
        if src < 0 or dst < 0 or src == dst: # src or dst is negative or if they equal eachother
            return
        if src >= len(self.adj_matrix): # src is greater than number of rows
            return
        if src >= len(self.adj_matrix[0]): # src is greater than number of columns
            return
        if dst >= len(self.adj_matrix): # dst is greater than number of rows
            return
        if dst >= len(self.adj_matrix[0]): # dst is greater than number of columns
            return
        # check the weight if negative
        if weight < 0:
            return
        # otherwise, add the weight at the src and dst
        self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        This method removes an edge between two vertices with provided indices.
        """
        # if either or both vertices DNE or if no edge between them, do nothing
        if src < 0 or dst < 0: # src or dst negative
            return
        if src >= len(self.adj_matrix): # src is greater than number of rows
            return
        if src >= len(self.adj_matrix[0]): # src is greater than number of columns
            return
        if dst >= len(self.adj_matrix): # dst is greater than number of rows
            return
        if dst >= len(self.adj_matrix[0]): # dst is greater than number of columns
            return
        if self.adj_matrix[src][dst] is 0: # no edge between them aka no weight
            return
        # otherwise, remove the weight at src and dst
        self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """
        This method returns a list of vertices of the graph. Order does not matter.
        """
        # vertices are simply the indices of the rows in the matrix
        list = []
        for row in range(len(self.adj_matrix)):
            list.append(row)
        return list

    def get_edges(self) -> []:
        """
        This method returns a list of edges in the graph. Each edge is returned as 
        tuple of two incident vertex indices and weight.
        """
        # edges are simply the weights stored in the adj_matrix
        list = []
        for row in range(len(self.adj_matrix)): # rows
            for column in range(len(self.adj_matrix[row])): # columns
                if self.adj_matrix[row][column] != 0: # 0 means no edge between two vertices
                    list.append((row, column, self.adj_matrix[row][column]))
        return list

    def is_valid_path(self, path: []) -> bool:
        """
        This method takes a list of vertex indices and returns True if the 
        sequence of vertices represents a valid path in the graph.
        """
        # check if path is empty
        if not path: 
            return True # empty paths are True
        # collect the vertex/edge pairs in the graph
        list = []
        for edge in self.get_edges():
            list.append((edge[0], edge[1]))
        # perform search
        for i in range(len(path) - 1): # indices for the path, subtract 1 because starts at 0
            # look at tuples holding the path's value currently and the next vertex
            tuple = (path[i], path[i + 1])
            # now check if the tuple exists in the list of 
            if tuple not in list:
                return False
        # if not caught in the for loop
        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        This method performs a depth-first search in the graph and returns a list of 
        vertices visited during the search, in the order they were visited.
        """
        # check v_start
        if v_start < 0: # if negative
            return []
        if v_start >= len(self.adj_matrix) or v_start >= len(self.adj_matrix[0]): # greater than rows or columns
            return []
        # otherwise, follow pseudocode
        visited = []
        stack = [v_start]
        while stack: # while the stack isn't empty
            v = stack.pop() # pop the vertex
            if v not in visited: # if not already visited 
                visited.append(v) # add it
                # break if you reach v_end
                if v == v_end:
                    break
            # pick vertices in ascending order
            list = []
            for i in range(len(self.adj_matrix[v])): # indices of the row aka vertices
                if self.adj_matrix[v][i] != 0: # if edge is weighted
                    if i not in visited:
                        list.append(i)
            # add the vertices in the row to the stack in reverse alphabetical order
            reverse = sorted(list, reverse=True)
            for v in reverse:
                stack.append(v)
        return visited

    def bfs(self, v_start, v_end=None) -> []:
        """
        This method performs a breadth-first search in the graph and returns a list of 
        vertices visited during the search, in the order they were visited.
        """
        # check v_start
        if v_start < 0: # if negative
            return []
        if v_start >= len(self.adj_matrix) or v_start >= len(self.adj_matrix[0]): # greater than rows or columns
            return []
        # otherwise, follow pseudocode
        visited = [] # list of visited vertices
        queue = deque() # iniialized queue
        queue.append(v_start)
        while queue: # while the queue isn't empty
            v = queue.pop()
            if v not in visited: # if not already visited
                visited.append(v)
                # break if reached v_end
                if v == v_end:
                    break
            # pick vertices in ascending order
            list = []
            for i in range(len(self.adj_matrix[v])): # indices of the row aka vertices
                if self.adj_matrix[v][i] != 0: # if edge is weighted
                    if i not in visited: 
                        list.append(i)
            # order the queue to extend to the left to order it
            for vertex in list:
                if vertex not in visited:
                    queue.appendleft(vertex)
        return visited


    def has_cycle(self):
        """
        This method returns True if there is at least one cycle in the graph, False if acyclic.
        """
        # using DFS to find cycle b/c DFS for a connected graph produces a tree
        for v in range(len(self.get_vertices())): # for all vertices in the graph
            for edge in range(len(self.get_vertices())): # see if there is a connection/edge existing
                if self.adj_matrix[v][edge]:
                    # use the dfs to get the list of vertices connected
                    if v in self.dfs(edge):
                        return True # the vertex exists in the list of dfs tree
        # otherwise, not found
        return False


    def dijkstra(self, src: int) -> []:
        """
        This method implements Dijkstra's algorithm to compute the length of the 
        shortest path from a given vertex to all other vertices in the graph.
        """
        # check the src to see if valid
        if src < 0 or src >= len(self.get_vertices()):
            # return infinity
            return [float('inf')]
        # initialize priority queue and visited to track
        priority = []
        visited = {}
        # append tuple in priority queue to initialize algorithm
        distance = 0
        heapq.heappush(priority, (distance, src))
        # do algorithm -- pseudocode in module
        while priority: # while priority not empty
            tuple = heapq.heappop(priority)
            cur = tuple[1] # the src
            distance = tuple[0] # the distance for the src
            if cur not in visited: # if the src not visited
                visited[cur] = distance # add it
                # add successors into the priority queue for each vertex
                for successor in range(len(self.get_vertices())):
                    if self.adj_matrix[cur][successor]: # if there is a successor
                        # push it to the priority queue
                        total_dist = distance + self.adj_matrix[cur][successor]
                        heapq.heappush(priority, (total_dist, successor))
        # initialize infinity list the length of the number of vertices
        list = [float('inf')] * len(self.get_vertices())
        # return the visited values, ensure that certain vertices that are not reachable from src are float('inf')
        for vertex in visited.keys():
            list[vertex] = visited[vertex]
        return list


if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = DirectedGraph()
    print(g)
    for _ in range(5):
        g.add_vertex()
    print(g)

    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    for src, dst, weight in edges:
        g.add_edge(src, dst, weight)
    print(g)


    print("\nPDF - method get_edges() example 1")
    print("----------------------------------")
    g = DirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    for path in test_cases:
        print(path, g.is_valid_path(path))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for start in range(5):
        print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)


    print("\nPDF - dijkstra() example 1")
    print("--------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    g.remove_edge(4, 3)
    print('\n', g)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
