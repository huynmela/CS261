
class DynamicArrayException(Exception):

    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass
class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array   
        DO NOT CHANGE THIS METHOD IN ANY WAY    
        """    
        self.size = 0    
        self.capacity = 4    
        self.first = 0  # do not use / change this value    
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)    
        # before using this feature, implement append() method    
        if start_array is not None:    
            for value in start_array:    
                self.append(value)

    def dynArrayAddAt(self, index: int, value: object) -> None:    
        """    
        This method adds an element at a particular index in the dynamic array.
        """   
        # check any exceptions: index is greater than the size or if its negative
        if index > self.size or index < 0:
            raise DynamicArrayException

        # check if size == capacity,
        if self.size == self.capacity:
            # change the capacity of the dynamic array
            self.capacity = 2 * self.capacity # double it
        # begin shifting elements to the right of the index
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        # then place the value at index
        self.data[index] = value
        # thus the size has increased by 1
        self.size += 1
        return