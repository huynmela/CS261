# Course: CS261 - Data Structures
# Student Name: Melanie Huynh 
# Assignment: Assignment 5, AVL
# Description: Implementation of an AVL tree class.


import random


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self):
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self):
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self):
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    AVL Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL N
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

    def __str__(self):
        return 'AVL Node: {}'.format(self.value)


class AVL:
    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate AVL with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of AVL in human-readable form using pre-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if cur:
            values.append(str(cur.value))
            self._str_helper(cur.left, values)
            self._str_helper(cur.right, values)

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        s = Stack()
        s.push(self.root)
        while not s.is_empty():
            N = s.pop()
            if N:
                # check for correct height (relative to children)
                l = N.left.height if N.left else -1
                r = N.right.height if N.right else -1
                if N.height != 1 + max(l, r):
                    print("height failed")
                    return False

                if N.parent:
                    # parent and child pointers are in sync
                    if N.value < N.parent.value:
                        check_node = N.parent.left
                    else:
                        check_node = N.parent.right
                    if check_node != N:
                        print("pointers of child and parent not in sync")
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if N != self.root:
                        print("none parent only allowed on the root of tree")
                        return False
                s.push(N.right)
                s.push(N.left)
        return True

    # -----------------------------------------------------------------------
    
    def add(self, value: object) -> None:
        """
        This method adds a new value to the tree while maintaining AVL property.
        Duplicates are not allowed, and if the value already exists, the method should do nothing.
        """
        # base case, root is empty
        if self.root == None:
            # make the root the first value, then return
            new_node = TreeNode(value)
            self.root = new_node

        # otherwise
        # first, need to see if the value exists in the tree and otherwise insert it
        N = self.root
        new_node = None
        while new_node == None:
            if value == N.value: # the value is already in the tree
                return # do nothing
            elif value < N.value: # on the left
                if N.left == None: # left subtree DNE
                    N.left = TreeNode(value)
                    new_node = N.left
                    new_node.parent = N # update parent
                else:
                    N = N.left # otherwise, keep moving
            elif value > N.value: # on the right
                if N.right == None: # right subtree DNE
                    N.right = TreeNode(value)
                    new_node = N.right
                    new_node.parent = N # update parent
                else:
                    N = N.right # otherwise, keep moving

        # at this point, N's child is the newly inserted value-- so N is the parent.
        # then perform rebalancing
        P = new_node.parent
        while P is not None:
            self.rebalance(P)
            P = P.parent
            #print(N)

    # REDO THE BALANCE FACTOR TO MAKE IT EASIER TO READ

    def get_height(self, N):
        """
        Helper function to return height fo a given N. Checks if the the
         given N is None to return -1.
        """
        if N == None: # N is none
            return -1
        else: # otherwise, return its height
            return N.height 

    def balance_factor(self, N):
        """
        Returns the balance factor of a given N
        """
        # right - left 
        right = self.get_height(N.right)
        left = self.get_height(N.left)
        return right - left

    def rebalance(self, N):
        """
        Performs rebalancing at each N
        """
        # left, right heavy, requires double rotation
        if self.balance_factor(N) < -1:
            if self.balance_factor(N.left) > 0:
                N.left = self.rotate_left(N.left) # update pointers
                N.left.parent = N
            # now rotate C about N
            save_N_parent = N.parent
            C = self.rotate_right(N)
            C.parent = save_N_parent
            # reconnect pointers
            if save_N_parent == None: # check to see if the saved parent exists
                self.root = C # if not, the root is the new subtree root
            elif save_N_parent.left == N: # check to see if the saved parent's left child is N
                save_N_parent.left = C # change it to the new subtree's root
            else: # check to see if the saved parent's right child is N
                save_N_parent.right = C # change it to the new subtree's root

        # right, left heavy, requires double rotation
        elif self.balance_factor(N) > 1: 
            if self.balance_factor(N.right) < 0: 
                N.right = self.rotate_right(N.right) # update pointers
                N.right.parent = N
            # now rotate C about N
            save_N_parent = N.parent
            C = self.rotate_left(N)
            C.parent = save_N_parent
            # reconnect pointers
            if save_N_parent == None: # check to see if the saved parent exists
                self.root = C # if not, the root is the new subtree root
            elif save_N_parent.left == N: # check to see if the saved parent's left child is N
                save_N_parent.left = C # change it to the new subtree's root
            else: # check to see if the saved parent's right child is N
                save_N_parent.right = C # change it to the new subtree's root

        # otherwise, skip rotation and just update the height          
        self.update_height(N) 

    def rotate_left(self, N):
        """
        Method allowing for left rotation around N.
        """
        # using pseudocode from exploration
        C = N.right
        N.right = C.left
        # using pseudocode from exploration
        if N.right != None:
            N.right.parent = N
        C.left = N
        N.parent = C  
        # update heights
        self.update_height(N)
        self.update_height(C)
        return C
    
    def update_height(self, N):
        """
        Updates the height of a node whose subtrees may have been restructured
        """
        # check to see if they are None
        if N.left == None: 
            left_height = -1
        else:
            left_height = N.left.height

        if N.right == None:
            right_height = -1
        else:
            right_height = N.right.height

        # then redefine the height
        N.height = max(left_height, right_height) + 1

    def rotate_right(self, N):
        """
        Method allowing for right rotation around N.       
        """
        # using pseudocode from exploration
        C = N.left
        N.left = C.right
        # using pseudocode from exploration
        if N.left != None:
            N.left.parent = N
        C.right = N
        N.parent = C   
        # update heights
        self.update_height(N)
        self.update_height(C)
        return C

    def remove(self, value: object) -> bool:
        """
        This method removes the first instance of the value in the AVL tree.
        Returns True if the value is removed, False otherwise.
        """
        # base case, tree is empty
        if self.root == None:
            return False
        # root case
        if self.root.left == None:
            if self.root.right == None:
                self.root = None
                return True
        # remove value using standard BST delete
        # need to see if the value exists in the tree and otherwise remove it
        N = self.root
        while N.value != value:
            if value < N.value: # moving left
                if N.left == None: # value not found
                    return False
                N = N.left # keep moving left
            else: # moving right
                if N.right == None: # value not found
                    return False
                N = N.right # keep moving right

        # Defining all cases of removing a node, depending on subtree presence

        # 1: no right subtree
        if N.right == None:
            P = N.left
            cur = P
            # fix the pointers to connect the new parent and child
            if P != None:
                P.parent = N.parent
            if N.parent != None:
                if N.parent.left == N:
                    N.parent.left = P
                else:
                    N.parent.right = P
        # 2: no left subtree
        elif N.left == None: 
            P = N.right
            cur = P
            # fix the pointers to connect the new parent and child
            P.parent = N.parent
            if N.parent != None:
                if N.parent.left == N:
                    N.parent.left = P
                else:
                    N.parent.right = P
        # 3: no subtrees
        elif N.right.left == None: 
            P = N.right
            cur = P
            # fix the pointers to connect the new parent and child
            if P != None:
                P.parent = N.parent
            if N.parent != None:
                if N.parent.left == N:
                    N.parent.left = P
                else:
                    N.parent.right = P
            P.left = N.left
            if P.left != None:
                P.left.parent = P
        # 4: otherwise, find the in-order successor
        else:
            P= N.right
            while P.left != None:
                P= P.left
            P.parent.left = P.right # replace in order successor
            cur = P.parent   
            if P.right != None:
                P.right.parent = P.parent
                cur = P.right        
            # fix the pointers to connect the new parent and child
            P.parent = N.parent
            if P.parent != None:
                if P.parent.left == N:
                    P.parent.left = P
                else:
                    P.parent.right = P
            P.left = N.left
            P.right = N.right
            if P.left != None:
                P.left.parent = P
            if P.right != None:
                P.right.parent = P
        
        if P != None: # fix the root
            if P.parent == None:
                self.root = P
        if cur == None: # check if cur is None so cur can be the parent of N
            cur = N.parent

        # rebalance the tree
        while cur != None:
            self.rebalance(cur)
            cur = cur.parent
        # if it's reached this point, it should be removed and rebalanced
        return True
# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        avl = AVL(case)
        print(avl)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),   # RR, RR
        (10, 20, 30, 50, 40),   # RR, RL
        (30, 20, 10, 5, 1),     # LL, LL
        (30, 20, 10, 1, 5),     # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        avl = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', avl)

    #print("\nPDF - method add() example 3")
    #print("----------------------------")
    #for _ in range(100):
    #    case = list(set(random.randrange(1, 20000) for _ in range(900)))
    #    avl = AVL()
    #    for value in case:
    #        avl.add(value)

    #    if not avl.is_valid_avl():
    #        raise Exception("PROBLEM WITH ADD OPERATION")
    #print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),  # no AVL rotation
        ((1, 2, 3), 2),  # no AVL rotation
        ((1, 2, 3), 3),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    )
    for tree, del_value in test_cases:
        avl = AVL(tree)
        print('INPUT  :', avl, "DEL:", del_value)
        avl.remove(del_value)
        print('RESULT :', avl)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    )
    for tree, del_value in test_cases:
        avl = AVL(tree)
        print('INPUT  :', avl, "DEL:", del_value)
        avl.remove(del_value)
        print('RESULT :', avl)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    avl = AVL(case)
    for del_value in case:
        print('INPUT  :', avl, del_value)
        avl.remove(del_value)
        print('RESULT :', avl)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    avl = AVL(case)
    for _ in case[:-2]:
        print('INPUT  :', avl, avl.root.value)
        avl.remove(avl.root.value)
        print('RESULT :', avl)

    #print("\nPDF - method remove() example 5")
    #print("-------------------------------")
    #for _ in range(100):
    #    case = list(set(random.randrange(1, 20000) for _ in range(900)))
    #    avl = AVL(case)
    #    for value in case[::2]:
    #        avl.remove(value)
    #    if not avl.is_valid_avl():
    #        raise Exception("PROBLEM WITH REMOVE OPERATION")
    #print('remove() stress test finished')
