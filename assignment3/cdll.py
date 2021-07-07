# Course: CS261 - Data Structures
# Student Name: Melanie T. Huynh
# Assignment: Assignment 3, CLL
# Description: Implmentation of a circular linked list and its operations


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list

        This can also be used as troubleshooting method. This method works
        by independently measuring length during forward and backward
        traverse of the list and return the length if results agree or error
        code of -1 or -2 if thr measurements are different.

        Return values:
        >= 0 - length of the list
        -1 - list likely has an infinite loop (forward or backward)
        -2 - list has some other kind of problem

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # length of the list measured traversing forward
        count_forward = 0
        cur = self.sentinel.next
        while cur != self.sentinel and count_forward < 101_000:
            count_forward += 1
            cur = cur.next

        # length of the list measured traversing backwards
        count_backward = 0
        cur = self.sentinel.prev
        while cur != self.sentinel and count_backward < 101_000:
            count_backward += 1
            cur = cur.prev

        # if any of the result is > 100,000 -> list has a loop
        if count_forward > 100_000 or count_backward > 100_000:
            return -1

        # if counters have different values -> there is some other problem
        return count_forward if count_forward == count_backward else -2

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sentinel.next == self.sentinel

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        This method adds a new node at the beginning of the list right after the
         front sentinel
        """
        # make new node to hold value
        new_node = DLNode(value)
        # point the links to integrate new_node in
        temp = self.sentinel.next

        temp.prev = new_node
        self.sentinel.next = new_node
        new_node.prev = self.sentinel
        new_node.next = temp

    def add_back(self, value: object) -> None:
        """
        This method adds a new node at the end of the list right before the sentinel
        """
        # make new node to hold value
        new_node = DLNode(value)
        # point the links to integrate new_node in
        temp = self.sentinel.prev

        temp.next = new_node
        self.sentinel.prev = new_node
        new_node.next = self.sentinel
        new_node.prev = temp

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method adds a new value at index in the circular linked list. 
        Index 0 refers to the beginning of the list (right after the sentinel)
        """
        # raise exceptions
        if index < 0 or index > self.length() or self.length == 0:
            raise CDLLException
        # make new node
        new_node = DLNode(value)
        cur = self.sentinel
        i = 0 # iterator
        while i < index: 
            cur = cur.next
            i += 1
        # point linkers
        new_node.next = cur.next
        cur.next.prev = new_node
        cur.next = new_node
        new_node.prev = cur

    def remove_front(self) -> None:
        """
        This method removes the first node from the list
        """
        # deal with exceptions
        if self.length() == 0: #empty?
            raise CDLLException
        # define the node you want to remove
        remove_node = self.sentinel.next
        # set the head to the next
        self.sentinel.next = self.sentinel.next.next
        self.sentinel.next.prev = self.sentinel
        # then remove the node
        remove_node = None

    def remove_back(self) -> None:
        """
        This method removes the last node from the list
        """
        # deal with exceptions
        if self.length() == 0: #empty?
            raise CDLLException
        # define the node you want to remove
        remove_node = self.sentinel.prev
        # set the head to the prev 
        self.sentinel.prev = self.sentinel.prev.prev
        self.sentinel.prev.next = self.sentinel
        # the remove the node
        remove_node = None

    def remove_at_index(self, index: int) -> None:
        """
        This method removes a node from the list given its index
        """
        # check exceptions
        if index < 0 or index > self.length() - 1 or self.length == 0:
            raise CDLLException
        
        cur = self.sentinel.next

        for i in range(index):
            cur = cur.next
        
        # point linkers to remove
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        cur = None

    def get_front(self) -> object:
        """
        This method returns the value from the first node in the list without removing it
        """
        # check exceptions
        if self.length() == 0:
            raise CDLLException
        else:
            return self.sentinel.next.value

    def get_back(self) -> object:
        """
        This method returns the value from the back node in the list without removing it
        """
        # check exceptions
        if self.length() == 0:
            raise CDLLException
        else:
            return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """
        This method removes a node if it contains value. 
        Returns True if node is removed, False otherwise.
        """
        cur = self.sentinel.next
        while cur.value != None:
            if cur.value == value:
                # point linkers to remove
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return True
            else:
                cur = cur.next
        return False

    def count(self, value: object) -> int:
        """
        This method counts the number of elements in the list that match value
        """
        cur = self.sentinel.next
        count = 0
        i = 0
        while i < self.length(): # exit when end is reached
            if cur.value == value: # values match
                count += 1
            cur = cur.next
            i += 1
        return count

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        This method swaps two nodes given their indices.
        """
        # check exceptions
        if index1 < 0 or index2 < 0 or index1 > (self.length() - 1) or index2 > (self.length() - 1):
            raise CDLLException

        if index1 == index2:
            return

        # identify the nodes you need to swap, start at head
        cur = self.sentinel.next
        node_1 = self.sentinel.next
        node_2 = self.sentinel.next
        # begin traversal
        bigger = 0
        if index1 > index2:
            bigger = index1
        else:
            bigger = index2
        counter = 0

        # traverse
        while counter < bigger + 1:
            if counter == index1:
                node_1 = cur
            elif counter == index2:
                node_2 = cur
            cur = cur.next
            counter += 1

        # now swap the pointers
        if index1-index2 == -1:
            temp1 = node_1.prev
            temp2 = node_2.next

            node_1.next = temp2
            node_1.prev = node_2
            node_2.prev = temp1
            node_2.next = node_1

            temp1.next = node_2
            temp2.prev = node_1
            
        elif index1-index2 == 1:
            temp1 = node_2.prev
            temp2 = node_1.next

            node_2.next = temp2
            node_2.prev = node_1
            node_1.prev = temp1
            node_1.next = node_2

            temp1.next = node_1
            temp2.prev = node_2
        else:
            temp1_next = node_2.next
            temp1_prev = node_2.prev

            node_2.next = node_1.next
            node_2.prev = node_1.prev
            node_2.next.prev = node_2
            node_2.prev.next = node_2

            node_1.next = temp1_next
            node_1.prev = temp1_prev
            node_1.next.prev = node_1
            node_1.prev.next = node_1

    def reverse(self) -> None:
        """
        This method reverses the order of the nodes in the list.
        """
        # check exceptions:
        if self.length() == 0: #empty list
            return # exit

        cur = self.sentinel.next # set current pointer to node next to head

        # swap the next and prev for each node
        while cur != self.sentinel:
            cur.prev, cur.next = cur.next, cur.prev
            cur = cur.prev
        cur.prev, cur.next = cur.next, cur.prev

    def sort(self) -> None:
        """
        This method sorts the content of the list in non-descending order.
        """
        # empty list
        if self.length() == 0:
            return
        sorted = False
        done = None
        while sorted == False:
            sorted = True
            temp = self.sentinel.next
            while temp.next.value != None:

                if temp.value > temp.next.value:
                    before = temp.prev
                    after = temp.next
                    if before != None:
                        before.next = after
                    else: 
                        self.sentinel = after
                    temp.next = after.next
                    if after.next != None:
                        after.next.prev = temp
                    temp.prev = after
                    after.next = temp
                    after.prev = before

                    sorted = False
                else:
                    temp = temp.next
                done = temp
        
    def rotate(self, steps: int) -> None:
        """
        This method rotates the linked list by shifting the position of its elements 
        right or left steps number of times.
        """
        if self.length() == 0:
            return # don't do anything
        # otherwise, shift
        # define steps
        steps = -steps % self.length()
        if steps == 0:
            return

        cur = self.sentinel.next

        while steps != 0:
            cur = cur.next
            steps -= 1
        # remove sentinel from list
        self.sentinel.prev.next = self.sentinel.next
        self.sentinel.next.prev = self.sentinel.prev

        # put it back where cur is
        self.sentinel.prev, self.sentinel.next = cur.prev, cur
        cur.prev.next = self.sentinel
        cur.prev = self.sentinel
        

    def remove_duplicates(self) -> None:
        """
        This method deletes all nodes that have duplicate values from aa sorted linked list, 
        leaving only nodes with distinct values.
        """
        iter = self.sentinel.next
        next = self.sentinel.next
        prev_duplicate = self.sentinel
        while iter.next != self.sentinel: # loop through the list
            next = iter.next
            if iter.value != next.value: # duplicate not found
                prev_duplicate = iter # leave behind a pointer, will close the gap
                iter = iter.next # move a pointer on to find where the gap ends
            else:
                while iter.value == next.value: # found the end duplicate
                    iter = iter.next
                    next = iter.next
                # close the gap
                iter = next
            # remove the duplicates to close the gap
            prev_duplicate.next = next
            next.prev = prev_duplicate

    def odd_even(self) -> None:
        """
        This method regroups list nodes by first grouping all ODD nodes together, 
        then grouping EVEN nodes together. Odd and even refer to node position in the list.
        """
        odd = self.sentinel.next
        even = self.sentinel.next.next

        even_head = even

        while even.value != None and even.next.value != None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head

    def add_integer(self, num: int) -> None:
        """
        This method takes a non-negative integer and adds it to the number 
        already stored in the linked list. Then it will store the 
        result of the addition back into the list nodes, 
        one digit per node. 
        """
        # check for an empty list
        if self.is_empty() is True:
            # you need to add a new node to initialize the rest of the method
            new_node = DLNode(0)
            # then connect it back in
            self.sentinel.next = new_node
            self.sentinel.prev = new_node
            
            new_node.next = self.sentinel
            new_node.prev = self.sentinel
        
        cur = self.sentinel.prev
        while num and cur != self.sentinel:
            num += cur.value
            cur.value = num % 10
            num = num // 10
            if cur.prev == self.sentinel and num > 0:
                new_node = DLNode(0)
                self.sentinel.next = new_node
                cur.prev = new_node
                new_node.prev = self.sentinel
                new_node.next = cur
            # move on
            cur = cur.prev

#if __name__ == '__main__':
#    pass

#    print('\n# add_front example 1')
#    lst = CircularList()
#    print(lst)
#    lst.add_front('a')
#    lst.add_front('b')
#    lst.add_front('c')
#    print(lst)

#    print('\n# add_back example 1')
#    lst = CircularList()
#    print(lst)
#    lst.add_back('C')
#    lst.add_back('B')
#    lst.add_back('A')
#    print(lst)
    
#    print('\n# insert_at_index example 1')
#    lst = CircularList()
#    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
#    for index, value in test_cases:
#        print('Insert of', value, 'at', index, ': ', end='')
#        try:
#            lst.insert_at_index(index, value)
#            print(lst)
#        except Exception as e:
#            print(type(e))
    
#    print('\n# remove_front example 1')
#    lst = CircularList([1, 2])
#    print(lst)
#    for i in range(3):
#        try:
#            lst.remove_front()
#            print('Successful removal', lst)
#        except Exception as e:
#            print(type(e))
    
#    print('\n# remove_back example 1')
#    lst = CircularList()
#    try:
#        lst.remove_back()
#    except Exception as e:
#        print(type(e))
#    lst.add_front('Z')
#    lst.remove_back()
#    print(lst)
#    lst.add_front('Y')
#    lst.add_back('Z')
#    lst.add_front('X')
#    print(lst)
#    lst.remove_back()
#    print(lst)
    
#    print('\n# remove_at_index example 1')
#    lst = CircularList([1, 2, 3, 4, 5, 6])
#    print(lst)
#    for index in [0, 0, 0, 2, 2, -2]:
#        print('Removed at index:', index, ': ', end='')
#        try:
#            lst.remove_at_index(index)
#            print(lst)
#        except Exception as e:
#            print(type(e))
#    print(lst)
    
#    print('\n# get_front example 1')
#    lst = CircularList(['A', 'B'])
#    print(lst.get_front())
#    print(lst.get_front())
#    lst.remove_front()
#    print(lst.get_front())
#    lst.remove_back()
#    try:
#        print(lst.get_front())
#    except Exception as e:
#        print(type(e))
    
#    print('\n# get_back example 1')
#    lst = CircularList([1, 2, 3])
#    lst.add_back(4)
#    print(lst.get_back())
#    lst.remove_back()
#    print(lst)
#    print(lst.get_back())
    
#    print('\n# remove example 1')
#    lst = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
#    print(lst)
#    for value in [7, 3, 3, 3, 3]:
#        print(lst.remove(value), lst.length(), lst)
    
#    print('\n# count example 1')
#    lst = CircularList([1, 2, 3, 1, 2, 2])
#    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))
    
#    print('\n# swap_pairs example 1')
#    lst = CircularList([0, 1, 2, 3, 4, 5, 6])
#    test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5),
#                (4, 2), (3, 3), (1, 2), (2, 1))
    
#    for i, j in test_cases:
#        print('Swap nodes ', i, j, ' ', end='')
#        try:
#            lst.swap_pairs(i, j)
#            print(lst)
#        except Exception as e:
#            print(type(e))
    
#    print('\n# reverse example 1')
#    test_cases = (
#        [1, 2, 3, 3, 4, 5],
#        [1, 2, 3, 4, 5],
#        ['A', 'B', 'C', 'D']
#    )
#    for case in test_cases:
#        lst = CircularList(case)
#        lst.reverse()
#        print(lst)
    
#    print('\n# reverse example 2')
#    lst = CircularList()
#    print(lst)
#    lst.reverse()
#    print(lst)
#    lst.add_back(2)
#    lst.add_back(3)
#    lst.add_front(1)
#    lst.reverse()
#    print(lst)
    
#    print('\n# reverse example 3')
    
    
#    class Student:
#        def __init__(self, name, age):
#            self.name, self.age = name, age
    
#        def __eq__(self, other):
#            return self.age == other.age
    
#        def __str__(self):
#            return str(self.name) + ' ' + str(self.age)
    
    
#    s1, s2 = Student('John', 20), Student('Andy', 20)
#    lst = CircularList([s1, s2])
#    print(lst)
#    lst.reverse()
#    print(lst)
#    print(s1 == s2)
    
#    print('\n# reverse example 4')
#    lst = CircularList([1, 'A'])
#    lst.reverse()
#    print(lst)
    
#    print('\n# sort example 1')
#    test_cases = (
#        [1, 10, 2, 20, 3, 30, 4, 40, 5],
#        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
#        [(1, 1), (20, 1), (1, 20), (2, 20)]
#    )
#    for case in test_cases:
#        lst = CircularList(case)
#        print(lst)
#        lst.sort()
#        print(lst)
    
#    print('\n# rotate example 1')
#    source = [_ for _ in range(-20, 20, 7)]
#    for steps in [1, 2, 0, -1, -2, 28, -100]:
#        lst = CircularList(source)
#        lst.rotate(steps)
#        print(lst, steps)
    
#    print('\n# rotate example 2')
#    lst = CircularList([10, 20, 30, 40])
#    for j in range(-1, 2, 2):
#        for _ in range(3):
#            lst.rotate(j)
#            print(lst)
    
#    print('\n# rotate example 3')
#    lst = CircularList()
#    lst.rotate(10)
#    print(lst)
    
#    print('\n# remove_duplicates example 1')
#    test_cases = (
#        [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
#        [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
#        [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],
#        list("abccd"),
#        list("005BCDDEEFI")
#    )
    
#    for case in test_cases:
#        lst = CircularList(case)
#        print('INPUT :', lst)
#        lst.remove_duplicates()
#        print('OUTPUT:', lst)
    
#    print('\n# odd_even example 1')
#    test_cases = (
#        [1, 2, 3, 4, 5], list('ABCDE'),
#        [], [100], [100, 200], [100, 200, 300],
#        [100, 200, 300, 400],
#        [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E']
#    )
    
#    for case in test_cases:
#        lst = CircularList(case)
#        print('INPUT :', lst)
#        lst.odd_even()
#        print('OUTPUT:', lst)

#    print('\n# add_integer example 1')
#    test_cases = (
#      ([1, 2, 3], 10456),
#      ([], 25),
#      ([2, 0, 9, 0, 7], 108),
#       ([9, 9, 9], 9_999_999),
#    )
#    for list_content, integer in test_cases:
#       lst = CircularList(list_content)
#    print('INPUT :', lst, 'INTEGER', integer)
#    lst.add_integer(integer)
#    print('OUTPUT:', lst)
