# Course: CS261 - Data Structures
# Student Name: Melanie Huynh
# Assignment: Assignment 2, Bag ADT
# Description: Implementation of a Bag ADT using dynamic arrays

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        This method adds a new element to the bag. 
        Done in O(1)
        """
        # order doesn't matter, just append to the end
        self.da.append(value)

    def remove(self, value: object) -> bool:
        """
        This method removes one lement from the bag that matches the provided value.
        Returns True if some object was actually removed and False otherwise.
        Done in O(n).
        """
        # must find the index associated with the value
        # single for-loop (linear search) is O(n)
        for i in range(0, self.size()):
            if value == self.da[i]:
                # found --> remove and return True
                self.da.remove_at_index(i)
                return True
        else:
            # not found --> return False
            return False

    def count(self, value: object) -> int:
        """
        This method counts the number of elements in the bag that match value.
        Runs in O(n).
        """
        # must find the index associated with the value
        # single for-loop (linear search) is O(n)
        counter = 0

        for i in range(0, self.size()):
            if value == self.da[i]:
                counter += 1 # Count each instance value appears
        
        return counter

    def clear(self) -> None:
        """
        This method clears the contents of the bag
        """
        self.da = DynamicArray()

    def equal(self, second_bag: object) -> bool:
        """
        This method compares the contents of a big with the content of a second bag.
        Returns True if the bags are equal, False otherwise. 
        """
        # First, check if the bag lengths are equal
        if self.size() != second_bag.size():
            return False
        # bags are equal if and only if for every element in the first bag, count of 
            # such element is equal to count of same element in the second bag
        else: 
            for i in range(0, self.size()):
                if self.count(self.da[i]) != second_bag.count(self.da[i]):
                    return False # loop will break if it catches just one mismatch
        return True
               


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)


    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)


    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))


    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)


    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))
