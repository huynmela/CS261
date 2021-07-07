# Course: Data Structures 261
# Author: Melanie Huynh
# Assignment: Assignment 6
# Description: Implementation of an undirected graph. Usies an adjacency list.

import heapq
from collections import deque

class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        This method adds a new vertex to the graph. If vertex with the same name 
        is already present in the graph, the method does nothing.
        """
        if v in self.adj_list: # already in list
            return # do nothing
        # otherwise, add v into the list as a new key with no 
        self.adj_list[v] = []
        
    def add_edge(self, u: str, v: str) -> None:
        """
        This method adds a new edge to the graph, connecting two vertices with 
        provided names. If either/both vertex names do not exist, this method creates 
        them and then creates an edge between them.
        If an edge exists in the graph, or if u and v refer to the same vertex, do nothing.
        """
        # check if u and v refer to the same vertex
        if u == v:
            return # do nothing
        # check if u and v are in adj_list
        if u not in self.adj_list:
            self.add_vertex(u) # add the vertex
        if v not in self.adj_list:
            self.add_vertex(v) # add the vertex
        # check to see if u and v are connected
        if (u in self.adj_list[v]) and (v in self.adj_list[u]):
            return # do nothing
        # else, add them in self.adj_list
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def remove_edge(self, v: str, u: str) -> None:
        """
        This method removes an edge between two vertices with provided names. 
        If either/both vertex names do not exist in the graph, or if there is no edge 
        between them, do nothing.
        """
        # check if u and v arent in adj_list
        if u not in self.adj_list:
            return # do nothing
        if v not in self.adj_list:
            return # do nothing
        # check if u and v have an edge between them
        if (u not in self.adj_list[v]) and (v not in self.adj_list[u]):
            return # do nothing
        # otherwise, remove the edge
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)
        

    def remove_vertex(self, v: str) -> None:
        """
        This method removes a vertex with a given name and all edges incident 
        to it from the graph. If the given vertex does not exist, do nothing.
        """
        # check if v isnt in adj_list
        if v not in self.adj_list:
            return # do nothing
        # otherwise, remove the vertex
        self.adj_list.pop(v, None) # pop from the dict
        # then look through the entire list to remove 
        for each_vertex in self.adj_list:
            if v in self.adj_list[each_vertex]:
                self.adj_list[each_vertex].remove(v)


    def get_vertices(self) -> []:
        """
        This method returns a list of vertices of the graph.
        Order of the vertices in the list does not matter.
        """
        list = [] # initialize list to return
        for vertex in self.adj_list: # get each vertex in the dict
            list.append(vertex) # append the vertex into the list
        return list
        

    def get_edges(self) -> []:
        """
        This method returns a list of edges in the graph.
        Each edge is returned as a tuple of two incident vertex names.
        Order of the edges in the list or order of the vertices incident to 
        each edge does not matter.
        """
        list = [] # initialized list to return
        for vertex in self.adj_list: # get each vertex in the dict
            for edge in self.adj_list[vertex]: # get edges for each vertex
                # ensure there are no repeats of tuples 
                if (edge, vertex) not in list: # add otherwise
                    list.append((vertex, edge))
        return list
        

    def is_valid_path(self, path: []) -> bool:
        """
        This method takes a list of vertex names and returns True if the 
        sequence of vertices represents a valid path in the graph 
        (so one can travel from the first vertex in the list to the last 
        vertex in the list, at each step traversing over an edge in the graph).
        """
        # check if empty 
        if not path:
            return True # empty path is True
        # create a path looking at the vertices before and currently
        cur = None
        prev = None
        # collect the edges in the graph in a list
        edges = self.get_edges()
        for i in range(len(path)):
            cur = path[i]
            # special case, if the first vertex DNE
            if i is 0:
                if path[0] not in self.adj_list:
                    return False
            # check the rest of the vertices
            else:
                if (cur, prev) not in edges:
                    if (prev, cur) not in edges:
                        return False
            prev = cur # move on and track prev
        # otherwise, it hasn't been caught by the loop
        return True
 

    def dfs(self, v_start, v_end=None) -> []:
        """
        This method performs a depth-first search in the graph 
        and returns a list of vertices visited durng the search, 
        in the order they were visited.
        """
        # empty list if v_start not in list
        if v_start not in self.adj_list:
            return []
        # otherwise, follow pseudocode
        visited = [] # list of visited vertices
        stack = [v_start] # initialized stack
        while stack: # while the stack isn't empty
            v = stack.pop() # pop the vertex
            if v not in visited: # if not already visited
                visited.append(v) # add it 
                # break if you reach v_end
                if v == v_end:
                    break
            # pick vertices in ascending lexicographical order
            reverse = sorted(self.adj_list[v], reverse=True) # dealing with stacks, must reverse the traversal to access the bottom
            for vertex in reverse:
                if vertex not in visited:
                    stack.append(vertex)
        return visited

       

    def bfs(self, v_start, v_end=None) -> []:
        """
        This method performs a breadth-first search in the graph 
        and returns a list of vertices visited durng the search, 
        in the order they were visited.
        """
        # empty list if v_start not in list
        if v_start not in self.adj_list:
            return []
        # otherwise, follow pseudocode
        visited = [] # list of visited vertices
        queue = deque() # initialized queue
        queue.append(v_start)
        while queue: # while the queue isn't empty
            v = queue.pop()
            if v not in visited: # if not already visited
                visited.append(v) # append it
                # break if reached v_end
                if v == v_end:
                    break
            # pick vertices in ascending lexicographical order
            for vertex in sorted(self.adj_list[v]):
                if vertex not in visited:
                    queue.extendleft(vertex)
        return visited


    def count_connected_components(self):
        """
        This method returns the number of connected componets in the graph
        """
        # use a search algo BFS or DFS to find and count the connected components
        counter = 0 # initialize counter
        # track the vertices you've visited in a list
        visited = []
        for v in self.adj_list: # check each vertex in adj_list
            if v not in visited: # havent visited v
                visited.append(v) # now you have
                counter += 1 # add to counter
                for i in self.dfs(v): # dfs gives all connected elements
                    visited.extend(i) # extend the list
        return counter

    def has_cycle(self):
        """
        This method returns True if the graph contains at least one cycle, 
        False if acyclic.
        """
        # Cycle only if there is a back edge present in the graph
        # Find back edge by using visited and check if back edge exists any visited node
        # use DFS on each edge
        edges = self.get_edges() # all edges
        num_edges = range(len(edges)) # total number of edges
        # follow the same strategy for is_valid
        cur = None 
        prev = None
        # loop over each vertex for all edges
        for i in num_edges:
            vertex = edges[i][0] # the first vertex of an edge
            # then begin DFS
            visited = [] # initialize list of visited vertices
            stack = [(None, vertex)] # initialize stack with the first edge
            # loop until stack is empty
            #print("stuck in first for loop")
            while stack:
                #print("stuck in while loop")
                edge = stack.pop() # pop edge of stack
                # then redefine the cur and prev
                cur, prev = edge[1], edge[0]
                # now check each v in the adj_list
                for v in self.adj_list[cur]:
                    #print("stuck in second for loop")
                    if v is prev: # skip over the vertex that has already been visited
                        pass
                    elif v in visited:
                        return True # v in visited, there's a cycle
                    elif v not in visited: # haven't visited v
                        visited.append(cur)
                        stack.append((cur, v))
                        #print("stuck appending")
                        #print(cur, v)
                    
        # if not caught in the loop
        return False

   


if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = UndirectedGraph()
    print(g)

    for v in 'ABCDE':
        g.add_vertex(v)
    print(g)

    g.add_vertex('A')
    print(g)

    for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
        g.add_edge(u, v)
    print(g)


    print("\nPDF - method remove_edge() / remove_vertex example 1")
    print("----------------------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    g.remove_vertex('DOES NOT EXIST')
    g.remove_edge('A', 'B')
    g.remove_edge('X', 'B')
    print(g)
    g.remove_vertex('D')
    print(g)


    print("\nPDF - method get_vertices() / get_edges() example 1")
    print("---------------------------------------------------")
    g = UndirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    for path in test_cases:
        print(list(path), g.is_valid_path(list(path)))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')


    print("\nPDF - method count_connected_components() example 1")
    print("---------------------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print(g.count_connected_components(), end=' ')
    print()


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
        'add FG', 'remove GE')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print('{:<10}'.format(case), g.has_cycle())
