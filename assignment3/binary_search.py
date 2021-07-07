# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:

import random
import time
from static_array import *


# ------------------- PROBLEM 1 - -------------------------------------------


def binary_search(arr: StaticArray, target: int) -> int:
    """
    This function takes a StaticArray and an integer target and returns the 
    index of the target element if it is present in the array or returns -1 if it 
    is not.
    """
    # begin with the entire array 
    lo = 0 # first index
    hi = arr.size() - 1 # last index
    # the return values
    found = -1 
    index = 0
    # check and see if it is strictly ascending or descending
    # ascending
    if arr[0] < arr[arr.size()-1]:
        # Reduce the array size by half in a loop
        while lo <= hi:
            mid = (lo + hi) // 2;     
            # check if mid is target
            if arr[mid] == target:
                found = mid 
                index = mid
                return index 
  
            # check if target is less than the value at the midpoint
            elif target < arr[mid]:
                hi = mid - 1
            
            # or greater than
            else: 
                lo = mid + 1
  
        # exit if target is not in the array
        index = lo  
        return  found
    else: # descending
        # Reduce the array size by half in a loop
        while lo <= hi:
            mid = (lo + hi) // 2;     
            # check if mid is target
            if arr[mid] == target:
                found = mid 
                index = mid
                return index 
  
            # check if target is less than the value at the midpoint
            elif target > arr[mid]:
                hi = mid - 1
            
            # or greater than
            else: 
                lo = mid + 1
  
        # exit if target is not in the array
        index = lo  
        return  found
  


# ------------------- PROBLEM 2 - -------------------------------------------


def binary_search_rotated(arr: StaticArray, target: int) -> int:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":
    pass

    print('\n# problem 1 example 1')
    src = (-10, -5, 0, 5, 7, 9, 11)
    targets = (7, -10, 11, 0, 8, 1, -100, 100)
    arr = StaticArray(len(src))
    for i, value in enumerate(src):
        arr[i] = value
    print([binary_search(arr, target) for target in targets])
    arr._data.reverse()
    print([binary_search(arr, target) for target in targets])


    print('\n# problem 1 example 2')
    """
    src = [random.randint(-10 ** 7, 10 ** 7) for _ in range(5_000_000)]
    src = sorted(set(src))
    arr = StaticArray(len(src))
    arr._data = src[:]

    # add 20 valid and 20 (likely) invalid targets
    targets = [-10 ** 8, 10 ** 8]
    targets += [arr[random.randint(0, len(src) - 1)] for _ in range(20)]
    targets += [random.randint(-10 ** 7, 10 ** 7) for _ in range(18)]

    result, total_time = True, 0
    for target in targets:
        total_time -= time.time()
        answer = binary_search(arr, target)
        total_time += time.time()
        result &= arr[answer] == target if target in src else answer == -1
    print(result, total_time < 0.5)

    arr._data.reverse()
    for target in targets:
        total_time -= time.time()
        answer = binary_search(arr, target)
        total_time += time.time()
        result &= arr[answer] == target if target in src else answer == -1
    print(result, total_time < 0.5)
    """


    print('\n# problem 2 example 1')
    test_cases = (
        ((6, 8, 12, 20, 0, 2, 5), 0),
        ((6, 8, 12, 20, 0, 2, 5), -1),
        ((1,), 1),
        ((1,), 0),
    )
    result = []
    for src, target in test_cases:
        arr = StaticArray(len(src))
        for i, value in enumerate(src):
            arr[i] = value
        result.append((binary_search_rotated(arr, target)))
    print(*result)


    print('\n# problem 2 example 2')
    """
    src = [random.randint(-10 ** 7, 10 ** 7) for _ in range(5_000_000)]
    src = sorted(set(src))
    arr = StaticArray(len(src))
    arr._data = src[:]

    # add 20 valid and 20 (likely) invalid targets
    targets = [-10 ** 8, 10 ** 8]
    targets += [arr[random.randint(0, len(src) - 1)] for _ in range(20)]
    targets += [random.randint(-10 ** 7, 10 ** 7) for _ in range(18)]

    result, total_time = True, 0
    for target in targets:
        # rotate arr random number of steps
        pivot = random.randint(0, len(src) - 1)
        arr._data = src[pivot:] + src[:pivot]

        total_time -= time.time()
        answer = binary_search_rotated(arr, target)
        total_time += time.time()
        result &= arr[answer] == target if target in src else answer == -1
    print(result, total_time < 0.5)
    """

