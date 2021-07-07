# Course: CS261 - Data Structures
# Student Name: Melanie Huynh
# Assignment: Assignment 4, BST
# Description: Implementation of a binary search tree using a stack and queue ADT.


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

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
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

    def dequeue(self) -> object:
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
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if not cur:
            return
        # store value of current node
        values.append(str(cur.value))
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        This method adds a new value to the tree, maintaining BST property. 
        Duplicates must be allowed and placed in the right subtree.
        """
        # first make a node to store value
        new_node = TreeNode(value)
        # check if the tree is empty
        if self.root == None: 
            # add the node as the head
            self.root = new_node
            return # exit
        # otherwise, traverse the BST to find the place to add value
        # define the cur node
        cur = self.root
        # create a pointer that trails behind cur as parent node
        p_cur = None
        while cur is not None: # while the cur doesn't reach the bottom of the BST
            p_cur = cur # trailing behind cur
            if value >= cur.value: # compare value to the current value
                cur = cur.right # the cur will be on the right sub tree
            else: 
                cur = cur.left # cur on left sub tree
        # now you are on the place to add the value based on the parent node
        if value >= p_cur.value: # if value is greater than the parent node
            p_cur.right = new_node
        else: # less than parent node
            p_cur.left = new_node

    def contains(self, value: object) -> bool:
        """
        This method returns True if value is in the BST, False otherwise.
        """
        # if BST is empty
        if self.root == None:
            return False
        # undergo traversal
        cur = self.root
        while cur != None: # haven't reached the end
            if cur.value == value: # value  found
                return True
            elif value < cur.value: # comparison
                cur = cur.left # traverse left
            else:
                cur = cur.right # traverse right

        return False # value not found

    def get_first(self) -> object:
        """
        This method returns the value stored at the root node. 
        """
        # empty?
        if self.root == None:
            return None
        # otherwise, return the root node value
        return self.root.value

    def remove_first(self) -> bool:
        """
        This method removes the root node in the BST. Returns True if root is removed.
        """
        # empty?
        if self.root == None:
            return False
        # only root?
        if self.root.right == None and self.root.left == None:
            self.root = None
            return True
        # no left or right sub tree
        if self.root.right == None:
            self.root = self.root.left # move it up
            return True
        if self.root.left == None:
            self.root = self.root.right # move it up
            return True

        # need to find the in order successor
        found = False # tracking if the in order successor is found
        parent = self.root
        successor = self.root.right
        # traversing all the way to the left of the right child

        while successor.left != None: 
            parent = successor
            successor = successor.left
            found = True 

        if found:
            # remove the successor
            parent.left = successor.right
        else:
            parent.right = successor.right
        # then insert the successor as the root and fix pointers
        successor.left = self.root.left
        successor.right = self.root.right
        self.root = successor

        return True


    def remove(self, value) -> bool:
            """
            This method should remove the first instance of the value in the BST. 
            """
            # first, check if the BST is empty
            if self.root == None:
                return False
            # find value using BS
            found_left = False # value found in left subtree
            found = False # value found, cur.value = value
            parent = None
            cur = self.root
            while cur is not None and not found: # until the end is found and value is found
                if value == cur.value: # value you found
                    found = True
                elif value < cur.value: # value is less than cur.value
                    parent = cur
                    cur = cur.left # go down left subtree
                    found_left = True
                else: # value is greater than cur.value
                    parent = cur
                    cur = cur.right # go down right subtree
                    found_left = False
            # HANDLE SPECIAL CASES BEFORE FINDING IN-ORDER SUCCESSOR
            # cur is the root node, use remove_first()
            if cur == self.root:
                self.remove_first()
                return True
            # value not found, cur is None but found is not true
            if not found:
                return False
            # cur is a leaf, has no children
            if cur.left == None and cur.right == None:
                if found_left:
                    parent.left = None
                    return True
                if found_left:
                    parent.right = None
                    return True
            # only left subtree
            if cur.right is None: 
                if found_left:
                    parent.left = cur.left
                    return True
                if not found_left:
                    parent.right = cur.left
                    return True
            # only right subtree
            if cur.left is None:
                if found_left:
                    parent.left = cur.right
                    return True
                if not found_left:
                    parent.right = cur.right
                    return True
            else:
                # two children, need in-order successor
                suc_found_left = False
                succ = cur.right
                succ_parent = cur
                while succ.left is not None:
                    succ_parent = succ
                    succ = succ.left
                    suc_found_left = True
                # remove the successor
                if suc_found_left:
                    succ_parent.left = succ.right
                if not suc_found_left:
                    succ_parent.right = succ.right
                # place successor in removed node's spot
                if found_left:
                    parent.left = succ
                    succ.left = cur.left
                    succ.right = cur.right
                    return True
                if not found_left:
                    parent.right = succ
                    succ.left = cur.left
                    succ.right = cur.right
                    return True

    def pre_order_traversal(self) -> Queue:
        """
        This method will perform pre-order traversal of a tree, 
        return a Queue object containing values of visited nodes in order.
        """
        # empty
        if self.root == None:
            return Queue()
        # recurse to find nodes to visit
        order = Queue()
        self.helper_pre_order(self.root, order)
        return order

    def helper_pre_order(self, cur, queue):
        """
        Helper function for pre_order_traversal
        """
        # take the current node, add to end of queue
        queue.enqueue(cur)
        # then begin movement to the next node to visit
        if cur.left != None:
            self.helper_pre_order(cur.left, queue)
        if cur.right != None:
            self.helper_pre_order(cur.right, queue)

    def in_order_traversal(self) -> Queue:
        """
        This method will perform in-order traversal of a tree, 
        return a Queue object containing values of visited nodes in order.
        """
        # empty
        if self.root == None:
            return Queue()
        # recurse to find nodes to visit
        order = Queue()
        self.helper_in_order(self.root, order)
        return order

    def helper_in_order(self, cur, queue):
        """
        Helper function for in_order_traversal
        """
        # then begin movement to the next node to visit
        if cur.left != None:
            self.helper_in_order(cur.left, queue)
        # take cur node and add to end of queue
        queue.enqueue(cur)
        # check if right child exists
        if cur.right != None:
            self.helper_in_order(cur.right, queue)

    def post_order_traversal(self) -> Queue:
        """
        This method will perform post-order traversal of a tree, 
        return a Queue object containing values of visited nodes in order.
        """
        # empty
        if self.root == None:
            return Queue()
        # recurse to find nodes to visit
        order = Queue()
        self.helper_post_order(self.root, order)
        return order

    def helper_post_order(self, cur, queue):
        """
        Helper function for post_order_traversal
        """
        # then begin movement to the next node to visit
        if cur.left != None:
            self.helper_post_order(cur.left, queue)
        # check if right child exists
        if cur.right != None:
            self.helper_post_order(cur.right, queue)
        # take cur node and add to end of queue
        queue.enqueue(cur)

    def by_level_traversal(self) -> Queue:
        """
        This method will perform a by-level traversal of a tree,
        return a Queue object containing values of visited nodes in order.
        """
        # empty
        if self.root == None:
            return Queue()
        cur_BST = Queue()
        # put root in visited
        cur_BST.enqueue(self.root) # first level
        # make a final order
        order = Queue()
        # break while loop when the cur_BST is empty because we will remove values as we iterate
        while cur_BST.is_empty() != True:
            # remove a node
            cur = cur_BST.dequeue()
            # then check if that node isn't None
            if cur != None:
                order.enqueue(cur)
                cur_BST.enqueue(cur.left)
                cur_BST.enqueue(cur.right)
        return order

    def is_full(self) -> bool:
        """
        This method returns True if the current tree is a full BST. Empty or just root trees are considered full.
        """
        # special cases
        if self.root == None: #empty
            return True
        if self.root.left == None and self.root.right == None:
            #leaf
            return True
        # now check the leaves using recursion
        return self.helper_is_full(self.root)

    def helper_is_full(self, cur):
        """
        Helper function for is_full method
        """
        #BASE CASES
        # check to see if cur is a leaf aka no children
        if cur.left == None and cur.right == None:
            #leaf
            return True
        # otherwise, recurse to the next node
        if cur.left != None and cur.right != None:
            return self.helper_is_full(cur.left) and self.helper_is_full(cur.right)
        return False

    def is_complete(self) -> bool:
        """
        This method returns True if the current tree is a complete BST. 
        """
        #special cases
        if self.root == None: #empty
            return True
        if self.root.left == None and self.root.right == None: #leaf
            return True
        # now check rest
        queue = Queue()
        queue.enqueue(self.root) # use queue to keep track of nodes, begin with root

        # process tree from left to right on one level
        check_leaves = False # checks to see if all leaves are needed
        for i in range(self.size()):
            # pull out a node
            node = queue.dequeue()
            if node == None:
                return False
            queue.enqueue(node.left)
            queue.enqueue(node.right)
        return True

    def is_perfect(self) -> bool:
        """
        This method returns True if the current tree is a perfect BST
        """
        #special cases
        if self.root == None: #empty
            return True
        if self.root.left == None and self.root.right == None: #leaf
            return True
        # recurse through each node
        depth = self.find_depth(self.root)
        return self.helper_is_perfect(self.root, depth, 0)

    def find_depth(self, node):
        """
        Helper function that lets you find the depth of the left most leaf
        """
        d = 0
        while node != None:
            d += 1
            node = node.left
        return d

    def helper_is_perfect(self, cur, depth, level):
        """
        Helper function for is_perfect method
        """
        # leaf nodes must be at same depth as other leaves
        if cur.left == None and cur.right == None:
            return depth == level + 1
        # cur is not perfect, one child/subtree missing
        if cur.right == None or cur.left == None:
            return False
        # check if left and right subtrees are perfect
        return self.helper_is_perfect(cur.left, depth, level + 1) and self.helper_is_perfect(cur.right, depth, level + 1)  

    def size(self) -> int:
        """
        This method returns the total number of nodes in a tree
        """
        if self.root == None: # empty
            return 0
        # use recursion to count nodes
        return self.helper_size(self.root)
    
    def helper_size(self, cur):
        """
        Helper function for size method
        """
        # initialized count 1 bc of self.root counted already
        count = 1
        if cur.left != None: # check left subtree
            count += self.helper_size(cur.left)
        if cur.right != None: # check right subtree
            count += self.helper_size(cur.right)
        # at this point if both cur's children are none, exit
        return count

    def height(self) -> int:
        """
        This method returns the height of the BST
        """
        if self.root == None: #empty
            return -1

        # otherwise, use recursion to find depth
        return self.helper_height(self.root)

    def helper_height(self, node):
        """
        Helper function for height method
        """
        if node == None: # leaf root
            return -1
        # check depth
        left_height = self.helper_height(node.left)
        right_height = self.helper_height(node.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1
                                      

    def count_leaves(self) -> int:
        """
        This method returns the number of leaves in the BST.
        """
        # empty
        if self.root == None:
            return 0
        # then recurse to count leaf nodes 
        return self.helper_count_leaves(self.root)

    def helper_count_leaves(self, node):
        """
        Helper method to count_leaves method
        """
        if node == None: # doesn't count
            return 0
        if node.left == None and node.right == None: # node is a leaf
            return 1 
        else:
            # recurse
            return self.helper_count_leaves(node.left) + self.helper_count_leaves(node.right)

    def count_unique(self) -> int:
        """
        This method returns the count of unique values in the BST.
        """
        # empty
        if self.root == None:
            return 0
        # recurse to find unique
        que = Queue()
        return self.helper_count_unique(self.root, que)
 
    def helper_count_unique(self, node, que):
        """
        Helper function for count_unique method
        """
        # initialize variables
        temp, unique, counter = Queue(), True, 0
        # using que while it is true that there is a unique value, do in-order traversal
        while not que.is_empty() and unique:
            cur = que.dequeue()
            temp.enqueue(cur)
            if node.value == cur.value:
                unique = False
        while not temp.is_empty():
            cur = temp.dequeue()
            que.enqueue(cur)
        if unique: # found a unique element
            que.enqueue(node) # enqueue it in que and add to the counter
            counter += 1
        if node.left != None and node.right == None: # left subtree
            return counter + self.helper_count_unique(node.left, que) # add and recurse moving left
        if node.left == None and node.right==None: # leaf
            return counter # just the counter
        if node.left == None and node.right != None: # right subtree
            return counter + self.helper_count_unique(node.right, que) # add and recurse moving right
        # two children at node, sum them both to get the total and recurse moving both ways
        return self.helper_count_unique(node.left, que) + counter + self.helper_count_unique(node.right, que)

# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    """ add() example #1 """
    print("\nPDF - method add() example 1")
    print("----------------------------")
    tree = BST()
    print(tree)
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree)
    tree.add(15)
    tree.add(15)
    print(tree)
    tree.add(5)
    print(tree)

    """ add() example 2 """
    print("\nPDF - method add() example 2")
    print("----------------------------")
    tree = BST()
    tree.add(10)
    tree.add(10)
    print(tree)
    tree.add(-1)
    print(tree)
    tree.add(5)
    print(tree)
    tree.add(-1)
    print(tree)

    """ contains() example 1 """
    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    """ contains() example 2 """
    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    """ get_first() example 1 """
    print("\nPDF - method get_first() example 1")
    print("----------------------------------")
    tree = BST()
    print(tree.get_first())
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree.get_first())
    print(tree)

    """ remove() example 1 """
    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    tree = BST([10, 5, 15])
    print(tree.remove(7))
    print(tree.remove(15))
    print(tree.remove(15))

    """ remove() example 2 """
    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.remove(20))
    print(tree)

    """ remove() example 3 """
    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    print(tree.remove(20))
    print(tree)
    # comment out the following lines
    # if you have not yet implemented traversal methods
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ remove_first() example 1 """
    print("\nPDF - method remove_first() example 1")
    print("-------------------------------------")
    tree = BST([10, 15, 5])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 2 """
    print("\nPDF - method remove_first() example 2")
    print("-------------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 3 """
    print("\nPDF - method remove_first() example 3")
    print("-------------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)

    """ Traversal methods example 1 """
    print("\nPDF - traversal methods example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Traversal methods example 2 """
    print("\nPDF - traversal methods example 2")
    print("---------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'N/A   {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in 'DATA STRUCTURES':
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
          tree.post_order_traversal(), tree.by_level_traversal(),
          sep='\n')

