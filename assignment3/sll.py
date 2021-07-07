# Course: CS261 - Data Structures
# Student Name: Melanie T. Huynh
# Assignment: Assignment 3, SLL
# Description: Implmentation of a singly linked list and its operations



class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head.next == self.tail

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        This method adds a new node at the beginning of the list right after the
         front sentinel
        """
        # make a new node to hold value
        new_node = SLNode(value)
        # point the new_node's link to the head's next
        new_node.next = self.head.next
        # then point the head's link to the new_node
        self.head.next = new_node

    def add_back(self, value: object) -> None:
        """
        This method adds a new node at the end of the list (right before the back sentinel)
        """
        self.helper_add_back(self.head, self.head.next, value) # recurse

    def helper_add_back(self, prev, cur, value):
        """
        Helper function for add_back method
        """
        # base case
        if cur == self.tail: # if you land on the tail
            # make the new node with value
            new_node = SLNode(value)
            # then link it in
            prev.next = new_node
            new_node.next = cur
            return #exit the function
        else: 
            # otherwise, recurse with movement
            self.helper_add_back(cur, cur.next, value)

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method adds a new value at the specified index position in the linked list.
        Index 0 refers to the beginning of the list (right after the sentinel)
        """
        if index < 0 or index > self.length(): 
            raise SLLException

        self.helper_insert_at_index(self.head, self.head.next, index, value, 0)

    def helper_insert_at_index(self, prev, cur, index, value, counter):
        """
        Helper function of the insert_at_index method
        """
        #base case, exit when the counter == index aka reached the location
        if counter == index:
            # check exceptions
            if prev == self.tail or prev == None:
                raise SLLException
            # make new node with value
            new_node = SLNode(value)
            # then link it in
            prev.next = new_node
            new_node.next = cur
            return # exit the function
        else:
            # otherwise, recurse with movement
            self.helper_insert_at_index(cur, cur.next, index, value, counter + 1)

    def remove_front(self) -> None:
        """
        This method removes the first node from the list.
        """
        if self.length() == 0:
            raise SLLException
        # define the node you want to remove
        remove_node = self.head
        # set the head to the next
        self.head = self.head.next
        # then remove the node
        remove_node = None

    def remove_back(self) -> None:
        """
        This method removes the last node from the list. 
        """
        if self.length() == 0: #check if empty
            raise SLLException

        self.helper_remove_back(self.head, self.head.next)

    def helper_remove_back(self, prev, cur):
        """
        Helper function for the remove_back method
        """
        # base case
        if cur.next == self.tail: # land on tail
            temp = prev.next
            prev.next = self.tail
            temp = None
            return # exit
        else:
            self.helper_remove_back(cur, cur.next) # recurse

    def remove_at_index(self, index: int) -> None:
        """
        This method removes a node from the list given its index
        """
        # check to see if the index is at the end 
        if index == self.length() - 1:
            # then this is simply removing from the back
            self.remove_back()
            return # exit
        # check exceptions
        if index < 0 or index > self.length() - 1 or self.length == 0:
            raise SLLException
        # recurse
        self.helper_remove_at_index(self.head, self.head.next, index, 0)

    def helper_remove_at_index(self, prev, cur, index, counter):
        """
        Helper function for the remove_at_index method
        """        
        # base case, exit when the counter == index aka reached the location
        if counter == index:
            # check exceptions
            if prev == self.tail:
                raise SLLException
            # remove
            prev.next = cur.next
            return # exit
        else:
            # otherwise, recurse with movement
            self.helper_remove_at_index(cur, cur.next, index, counter + 1)

    def get_front(self) -> object:
        """
        This method returns the value from the first node in the list without removing it
        """
        if self.length() == 0: # empty list?
            raise SLLException
        else:
            return self.head.next.value

    def get_back(self) -> object:
        """
        This method returns the value from the last node in the list without removing it
        """
        if self.length() == 0: # empty list?
            raise SLLException
        else:
            return self.helper_get_back(self.head, self.head.next)

    def helper_get_back(self, prev, cur):
        """
        Helper function for the get_back method
        """
        if cur == self.tail: # Reached end sentinel
            return prev.value
        else: # otherwise, recurse
            return self.helper_get_back(cur, cur.next)

    def remove(self, value: object) -> bool:
        """
        This method traverses the list from the beginning to the end and removes the 
        first node that matches value.
        Returns True if node is removed, False otherwise.
        """
        return self.helper_remove(self.head, self.head.next, value, False)

    def helper_remove(self, prev, cur, value, found):
        """
        Helper function for the remove method
        """
        if cur.value == value: # if the value matches
            prev.next = cur.next
            found = True
            if found == True:
                return found
        if cur.next != None: # otherwise, recurse
            return self.helper_remove(cur, cur.next, value, found)
        return found

    def count(self, value: object) -> int:
        """
        This method counts the number of elements in the list that match value
        """
        return self.helper_count(self.head, value, 0)

    def helper_count(self, cur, value, count):
        """
        Helper function for count method
        """
        if cur.value == value: # if the value matches
            return self.helper_count(cur.next, value, count + 1)
        if cur.next != None:
            return self.helper_count(cur.next, value, count)
        return count

    def slice(self, start_index: int, size: int) -> object:
        """
        This method returns a new LinkedList object that contains the requested number of 
        nodes from the original list starting with the node located at start_index.
        """
        # check exceptions on start_index and size
        if start_index < 0 or start_index >= self.length():
            raise SLLException
        if size < 0 or (start_index + size) > self.length():
            raise SLLException
        # move to the start_index
        cur = self.head
        return self.helper_slice(start_index, size, cur, 0, 0, LinkedList())

    def helper_slice(self, start_index, size, cur, cur_counter, add_counter, new_LL):
        """
        Helper movement function for the slice method
        """
        if cur_counter == start_index: # return cur
            if add_counter != size: # now begin populating, check if the cur reached the end
                # if not, add to the new_LL
                new_LL.add_back(cur.next.value)
                # then recurse to the next node
                return self.helper_slice(start_index, size, cur.next, cur_counter, add_counter + 1, new_LL)
            else: 
                return new_LL
        else:# move until counter reaches start_index
            return self.helper_slice(start_index, size, cur.next, cur_counter + 1, add_counter, new_LL)


if __name__ == '__main__':
    pass

    print('\n# add_front example 1')
    list = LinkedList()
    print(list)
    list.add_front('A')
    list.add_front('B')
    list.add_front('C')
    print(list)
    
    
    print('\n# add_back example 1')
    list = LinkedList()
    print(list)
    list.add_back('C')
    list.add_back('B')
    list.add_back('A')
    print(list)
    
    
    print('\n# insert_at_index example 1')
    list = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            list.insert_at_index(index, value)
            print(list)
        except Exception as e:
            print(type(e))
    
    
    print('\n# remove_front example 1')
    list = LinkedList([1, 2])
    print(list)
    for i in range(3):
        try:
            list.remove_front()
            print('Successful removal', list)
        except Exception as e:
            print(type(e))
    
    
    print('\n# remove_back example 1')
    list = LinkedList()
    try:
        list.remove_back()
    except Exception as e:
        print(type(e))
    list.add_front('Z')
    list.remove_back()
    print(list)
    list.add_front('Y')
    list.add_back('Z')
    list.add_front('X')
    print(list)
    list.remove_back()
    print(list)
    
    
    print('\n# remove_at_index example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6])
    print(list)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            list.remove_at_index(index)
            print(list)
        except Exception as e:
            print(type(e))
    print(list)
    
    
    print('\n# get_front example 1')
    list = LinkedList(['A', 'B'])
    print(list.get_front())
    print(list.get_front())
    list.remove_front()
    print(list.get_front())
    list.remove_back()
    try:
        print(list.get_front())
    except Exception as e:
        print(type(e))
    
    
    print('\n# get_back example 1')
    list = LinkedList([1, 2, 3])
    list.add_back(4)
    print(list.get_back())
    list.remove_back()
    print(list)
    print(list.get_back())
    
    
    print('\n# remove example 1')
    list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(list)
    for value in [7, 3, 3, 3, 3]:
        print(list.remove(value), list.length(), list)
    
    
    print('\n# count example 1')
    list = LinkedList([1, 2, 3, 1, 2, 2])
    print(list, list.count(1), list.count(2), list.count(3), list.count(4))
    
    
    print('\n# slice example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")
    
    
    print('\n# slice example 2')
    list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", list)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", list.slice(index, size))
        except:
            print(" --- exception occurred.")

