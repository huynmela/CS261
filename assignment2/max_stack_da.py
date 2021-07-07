# Course: CS261 - Data Structures
# Student Name: Melanie Huynh
# Assignment: Assignment 2, Max and Stacks
# Description: Implementation of a Stack data type

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class MaxStack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da_val = DynamicArray()
        self.da_max = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "MAX STACK: " + str(self.da_val.length()) + " elements. ["
        out += ', '.join([str(self.da_val[i]) for i in range(self.da_val.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da_val.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da_val.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        This method adds a new element to the top of the stack. 
        Implemented with O(1) amortized runtime complexity.
        """
        # keep track of the max value in the stack
        if self.size() > 0: # if the stack isn't empty
            if self.da_max[self.size() - 1] < value: # value is bigger, append value to top
                self.da_max.append(value)
            else:
                self.da_max.append(self.da_max[self.size() - 1]) # repeat
            
        else: # Stack is empty, first push is inherently max
            self.da_max.append(value)

        self.da_val.append(value) # add to the stack

    def pop(self) -> object:
        """
        This method removes the top element from the stack and returns its value.
        Implemented with O(1) amortized runtime complexity.
        """
        if self.size() == 0: #empty, nothing to pop
            raise StackException 

        a = self.da_val[self.size() - 1] # keep the top value
        
        self.da_val.remove_at_index(self.size() - 1) # remove it from the array
        self.da_max.remove_at_index(self.size()) # keep track of the removal of the top
        
        return a #return the top value you removed

    def top(self) -> object:
        """
        This method returns the value of the top element of the stack without removing it.
        Implemented with O(1) runtime complexity.
        """
        if self.size() == 0: # empty stack
            raise StackException
        return self.da_val[self.size() - 1] # return the top element in the stack

    def get_max(self) -> object:
        """
        This method returns the maximum value currently stored in the stack.
        Implemented with O(1) runtime complexity.
        """
        if self.size() == 0: #empty stack
            raise StackException
        return self.da_max[self.size() - 1] # return the top element in the stack


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = MaxStack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)


    print("\n# pop example 1")
    s = MaxStack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))


    print("\n# top example 1")
    s = MaxStack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)


    print('\n# get_max example 1')
    s = MaxStack()
    for value in [1, -20, 15, 21, 21, 40, 50]:
        print(s, ' ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
        s.push(value)
    while not s.is_empty():
        print(s.size(), end='')
        print(' Pop value:', s.pop(), ' get_max after: ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
