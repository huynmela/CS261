# Course: CS261 - Data Structures
# Student Name: Melanie Huynh
# Assignment: Assignment 5, Min heaps
# Description: Implementation of a MinHeap class, using a dynamic array to store the hash table.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        This method adds a new object to the MinHeap maintaining heap property.
        Runtime complexity must be O(logN).
        """
        # begin by adding the node object at the end of the heap array
        self.heap.append(node)
        # then define the index of the node
        index = self.heap.length() - 1
        # finally, percolate the node up until it finds it proper spot
        self.percolate_up(index)

    def get_min(self) -> object:
        """
        This method returns an object with a minimum key without removing it from the heap.
        If heap is empty, raise exception
        """
        if self.is_empty() == True:
            raise MinHeapException()
        return self.heap.get_at_index(0) # return the root, which should be the minimum

    def remove_min(self) -> object:
        """
        This method returns an object with a minimum key and removes it from the heap.
        If heap is empty, raise exception
        """
        if self.heap.length() < 0:
            raise MinHeapException()
        # define the first val in the heap
        cur_val = self.get_min()
        # swap the first and last element
        self.heap.swap(0, self.heap.length() - 1)
        # then remove the last element
        self.heap.pop()
        # finally, percolate down the root node
        self.percolate_down(0)

        return cur_val

    def build_heap(self, da: DynamicArray) -> None:
        """
        This method receives a dynamic array with objects in any order and builds a proper 
        MinHeap from there. Current content of the MinHeap is lost.

        Runtime complexity must be O(N).
        """
        # must clear current content of minheap
        new_heap = DynamicArray()

        for i in range(da.length()): # taking the overall length of the array
            new_heap.append(da.get_at_index(i)) # adds the value into the array, using add method to ensure it is a proper heap

        # then set new_heap as the current heap, clearing current content
        self.heap = new_heap

        # begin percolation through all non-parent node
        # define the parent node
        parent_node = (da.length()) // 2 - 1
        while (parent_node != -1): #begin at parent and stop at root
            self.percolate_down(parent_node)
            # increment parent
            parent_node -= 1


    def percolate_up(self, index):
        """
        Helper function that allows for percolation up the min-heap until it reaches the root.
        """
        parent_index = (index - 1) // 2
        while index != 0:
            if (self.heap.get_at_index(parent_index) > self.heap.get_at_index(index)):
                # swap the nodes
                self.heap.swap(parent_index, index)
                # redefine the indices
                index = parent_index
                parent_index = (index - 1) // 2
            else:
                index = parent_index
                parent_index = (index - 1) // 2

    def percolate_down(self, index):
        """
        Helper function that allows for percolation down the min-heap until it reaches a leaf.
        """
        # define the children
        left = 2 * index + 1
        right = 2 * index + 2
        less = index # define the lesser value node

        if left <= self.heap.length() -1 and self.heap.get_at_index(index) > self.heap.get_at_index(left):
            less = left
        if right <= self.heap.length() - 1 and self.heap.get_at_index(less) > self.heap.get_at_index(right):
            less = right
        # otherwise, swap with parent to percolate down
        if less != index:
            self.heap.swap(index, less)
            # recurse the percolation using the lesser value
            self.percolate_down(less)


# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)