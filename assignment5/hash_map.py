# Course: CS261 - Data Structures
# Student Name: Melanie Huynh
# Assignment: Assignment 5, Hash maps
# Description: Implementation of a HashMap class, using a dynamic array to store the hash table.
# Will be using chaning for collision resolution using a singly linked list.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        This method clears the content of the hash map. 
        It does not change underlying hash table capacity.
        """
        for i in range(0, self.capacity): # Loop over all buckets
            # set an empty SLL in every index
            self.buckets.set_at_index(i, LinkedList())
        # then changed the size to 0
        self.size = 0

    def get(self, key: str) -> object:
        """
        This method returns the value associated with the given key.
        If the key is not in the hash map, the method returns None
        """
        # search for the given key
        SLL = self.buckets.get_at_index(self.hash_function(key) % self.capacity) # gives the SLL at the index

        if SLL.contains(key) == None: 
            return None
        else:
            return SLL.contains(key).value

    def put(self, key: str, value: object) -> None:
        """
        This method updates the key/value pair in the hash map. 
        If a given key already exists in the hash map, its associated value should be replaced
         with the new value. Otherwise, the key/value pair should be added.
        """
        # define node value at index
        SLL = self.buckets.get_at_index(self.hash_function(key) % self.capacity) # gives the SLL at the index
        if SLL.length() == 0: # if the SLL is empty
            # just insert at that index
            SLL.insert(key, value)
        elif SLL.contains(key) != None: # if the key exists in the SLL
            # the value will be replaced with the new value
            SLL.remove(key) # remove the first node with they key
            SLL.insert(key, value) # insert the key/value pair 
            # to keep the size of the hash map
            self.size -= 1
        else:
            # otherwise, insert the key/value pair
            SLL.insert(key, value)
        # increase the size of the hash map
        self.size += 1

    def remove(self, key: str) -> None:
        """
        This method removes the given key and its assosciated value from the hash map.
        If given key is not in the hash map, method does nothing.
        """
        # find the key in the hash map using the hash function
        # define the SLL at the index
        SLL = self.buckets[self.hash_function(key) % self.capacity].contains(key)
        # find value to remove
        if SLL == None: # empty SLL
            return
        else:
            self.buckets[self.hash_function(key) % self.capacity].remove(key)
            self.size -= 1

    def contains_key(self, key: str) -> bool:
        """
        This method returns True if the given key is in the hash map, otherwise it returns False.
        """
        if self.buckets.get_at_index(self.hash_function(key) % self.capacity).contains(key) != None:
           # gives the SLL at the index
           return True
        return False

    def empty_buckets(self) -> int:
        """
        This method returns a number of empty nuckets in the hash table.
        """
        counter = 0 # initialize number of empty buckets found
        # loop through the entire hash map array
        for i in range(0, self.capacity): 
            # count if the length of the SLL in the DA is 0
            if self.buckets[i].head == None:
                counter += 1
        return counter

    def table_load(self) -> float:
        """
        This method returns the current hash table load factor.
        """
        # number of elements
        n = self.size
        # number of buckets
        m = self.capacity
        return n / m

    def resize_table(self, new_capacity: int) -> None:
        """
        This method changes the capacity of the internal hash table.
        If new_capacity is less than 1, the method does nothing.
        """
        # new capacity is 0
        if new_capacity < 1:
            return # do nothing

        # initialize a new empty DA with the specified new_capacity
        new_table = DynamicArray()
        for i in range(new_capacity):
            new_table.append(LinkedList())

        # then take SLL in the original table and insert it into an empty SLL to parsing later
        temp_SLL = LinkedList()
        for i in range(0, self.capacity): # loop over original hash table
            cur = self.buckets.get_at_index(i) # get the SLL at index
            if cur.length() == 0: # an empty bucket
                continue # skip it!
            else: 
                # if there is something in that bucket, insert it into the temp SLL
                for node in cur: # for each node in the SLL
                    temp_SLL.insert(node.key, node.value) # add it into the temp

        # need to flip temp_SLL
        temp_flip = LinkedList()
        for node in temp_SLL:
            temp_flip.insert(node.key, node.value)

        # now that the values are saved, you can resent everything on the original hash table
        self.size, self.capacity, self.buckets = 0, new_capacity, new_table
        # then insert each key/value pair into current hash table
        for node in temp_flip:
            self.put(node.key, node.value)

    def get_keys(self) -> DynamicArray:
        """
        This method returns a DynamicArray that contains all keys stored in the hash map.
        """
        keys = DynamicArray()
        # populate keys with node keys
        for i in range(self.buckets.length()): # over the range of the DA Map
            for j in self.buckets.get_at_index(i):
                keys.append(j.key)
        return keys


# BASIC TESTING
if __name__ == "__main__":

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())


    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))


    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)


    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))


    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)


    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')


    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))


    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))


    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())
