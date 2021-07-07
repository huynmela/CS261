# Course: CS261 - Data Structures
# Student Name: Melanie T. Huynh
# Assignment: Assignment 1, Python Fundamentals Review
# Description: The purpose of this assignment is to practice programming in Python 
# and learn how to use arrays.

import random
import string
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------


def min_max(arr: StaticArray) -> ():
    """
    This function returns the minimum and maximum value in an array.
    """
    # initialize min and max variables to replace in for-loop
    min = arr.get(0) # begin at the start of the array
    max = arr.get(0) 

    for i in range(arr.size()): # for every index in the array
        if min < arr.get(i): # if the current index is less than the saved index
            min = arr.get(i) # set the saved index to the current index
        # repeat for max but greater than
        if max > arr.get(i):
            max = arr.get(i)
    # thus minimum and maximum are redefined and should return the value
    return (max, min)


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    This function modifies a StaticArray by replacing integers divisible by 3 with 
    'fizz', integers divisible by 5 with 'buzz', and integers divisible by both 3 
    and 5 with 'fizzbuzz'.
    """
    # define a new StaticArray with the same size as arr
    new_arr = StaticArray(arr.size()) 

    for i in range(arr.size()): # iterate through arr
        # go through all the criteria
        if arr.get(i) % 3 == 0 and arr.get(i) % 5 == 0: # both divisible by 3 and 5
            new_arr.set(i, 'fizzbuzz') # set to 'fizzbuzz' at same index as arr
        elif arr.get(i) % 3 == 0: # divisible by 3
            new_arr.set(i, 'fizz') # set to 'fizz' at the same index as arr
        elif arr.get(i) % 5 == 0: # divisible by 5
            new_arr.set(i, 'buzz') # set to 'buzz' at the same index as arr
        else: # otherwise
            new_arr.set(i, arr.get(i)) # set to original element as arr at same index
    # thus new_arr is redefined by modified arr
    return new_arr



# ------------------- PROBLEM 3 - REVERSE -----------------------------------


def reverse(arr: StaticArray) -> None:
    """
    The function reverses in place a StaticArray.
    """
    # define the first and last indices of the array
    front = 0
    back = arr.size() - 1
    
    while front < back: # moving towards the middle of the array
        # swap positions
        temp_front = arr.get(front) # holding the front value
        arr.set(front, arr.get(back))
        arr.set(back, temp_front)
        # increment inwards
        front += 1
        back -= 1
    # thus arr is reversed in place


# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    This function rotates a StaticArray by certain number of steps, shifting each 
    element left or right.
    """
    # define a new StaticArray with the same size as arr
    new_arr = StaticArray(arr.size()) 
    # check to see if the number of steps will shift back to the original array
    if steps % arr.size() == 0:
        for i in range(arr.size()): # return a copy of the original array
            new_arr.set(i, arr.get(i))
        return new_arr
    else: # otherwise, do the shift
        if steps > 0: # if positive, move right 
            for i in range(arr.size()):
                new_arr.set(i, arr.get((i - steps) % arr.size())) # recognize pattern, steps can be simplified
            return new_arr

        else: # if negative, move left
            for i in range(arr.size()):
                new_arr.set((i + steps) % arr.size(), arr.get(i)) # change the signs and flip
            return new_arr
    # thus new_arr is rotated


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------


def sa_range(start: int, end: int) -> StaticArray:
    """
    This function takes two integers and returns an array with all integers in between the two
    """
    size = abs(end-start) + 1
    arr = StaticArray(size)

    for i in range(0, size):
        if start <= end: # increasing range
            arr.set(i, start + i) # adds to the start by 1 for every step
        if start > end: # decreasing range
            arr.set(i, start - i)
    # thus arr is created with a range of integers from start to end
    return arr


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------


def is_sorted(arr: StaticArray) -> int:
    """
    This function checks if a given StaticArray is strictly ascending or descending in order.
    Returns 1 if ascending, 2 if descending, 0 otherwise.
    """
    a_counter = 1 # initialize ascending counter
    d_counter = 1 # initialize descending counter

    if arr.size() == 1: # if there is only one element in the array
        return 1

    for i in range(arr.size() - 1): # going through the entire array
        # descending
        if arr.get(i) < arr.get(i + 1): # current index is less than the next index
            a_counter += 1 # add to the counter
            if a_counter == arr.size(): # all are ascending
                return 1
        elif arr.get(i) > arr.get(i + 1): # current index is greater than the next index
            d_counter += 1 # add to the counter
            if d_counter == arr.size(): # all are descending 
                return 2
    return 0 # otherwise, it is not strictly ordered for either
# thus the array has been evaluated


# ------------------- PROBLEM 7 - SA_SORT -----------------------------------


def sa_sort(arr: StaticArray) -> None:
    """
    This function sorts using insertion sort a StaticArray in non-descending order.
    """
    for i in range(1, arr.size()): # go through the array
        val = arr.get(i) # define current element
        pos = i - 1 # define index before current
        while pos >= 0 and arr.get(pos) > val: # loop and sort by insertion
            arr.set(pos + 1, arr.get(pos))
            pos -= 1
        arr.set(pos + 1, val)
    # thus the array has been sorted


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    This function takes a pre-sorted StaticArray and returns a new StaticArray with 
    all duplicate values removed.
    """
    # initialize counters
    unique = 1 # inherently, the first one will be included
    if arr.size() == 1:
        new_arr = StaticArray(1)
        new_arr.set(0, arr.get(0))
        return new_arr
    # determine new_arr size
    for i in range(1, arr.size()):
        # count uniques
        if arr.get(i - 1) != arr.get(i): # pre-sorted, thus you can count uniques linearly
            unique += 1
    # define new_arr
    new_arr = StaticArray(unique)
    unique_index = 0
    # populate the uniques into new_arr
    for i in range(1, arr.size()):
        if arr.get(i-1) != arr.get(i):
            new_arr.set(unique_index, arr.get(i - 1))
            unique_index += 1
    new_arr.set(new_arr.size() - 1, arr.get(arr.size() - 1))
    return new_arr


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    # The output array that will have sorted arr
    new_arr = StaticArray(arr.size())
    
    # identify the minimum number in the array
    min_element = arr[0]
    max_element = arr[0]
    ind = 1
    while ind <= arr.size() - 1:
        if arr[ind] < min_element:
            min_element = arr[ind]
        if arr[ind] > max_element:
            max_element = arr[ind]
        ind += 1
    # The count array that will store count of individual characters
    counts = StaticArray(max_element - min_element + 1)
    for zero in range(counts.size()):
        counts.set(zero, 0)
    
    for i in range(0, arr.size()):
        counts[arr[i] - min_element] += 1
   
    pos = arr.size() - 1
    
    for i in range(max_element - min_element + 1):
        count = counts[i]
        value = i + min_element
        for j in range(count):
            new_arr[pos] = value
            pos -= 1
      
    return new_arr
# ------------------- PROBLEM 10 - SA_INTERSECTION --------------------------


def sa_intersection(arr1: StaticArray, arr2: StaticArray, arr3: StaticArray) \
        -> StaticArray:
    """
    This function takes three sorted StaticArrays and returns their common elements
    """
    # starting indices 
    i, j, k = 0, 0, 0
    x, y, z = arr1.size(), arr2.size(), arr3.size()
    size = 0

    #first run finds size
    while (i < x and j < y and k < z):
        if (arr1.get(i) == arr2.get(j) and arr2.get(j) == arr3.get(k)):
            size += 1
            i += 1
            j += 1
            k += 1
        elif arr1.get(i) < arr2.get(j):
            i += 1
        elif arr2.get(j) < arr3.get(k):
            j += 1
        else:
            k += 1
    
    if size == 0: # if nothing common was found, set it to none
        new_arr = StaticArray(1)
        new_arr.set(0, None)
        return new_arr
    # otherwise initialize the new_arr
    new_arr = StaticArray(size)
    new_index = 0
    i, j, k = 0, 0, 0 # reset counter
    # populate new_arr with common elements
    while (i < x and j < y and k < z):
        if (arr1.get(i) == arr2.get(j) and arr2.get(j) == arr3.get(k)):
            new_arr.set(new_index, arr3.get(k))
            new_index += 1
            i += 1
            j += 1
            k += 1
        elif arr1.get(i) < arr2.get(j):
            i += 1
        elif arr2.get(j) < arr3.get(k):
            j += 1
        else:
            k += 1
    return new_arr # thus the common elements are found

# ------------------- PROBLEM 11 - SORTED SQUARES ---------------------------


def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    This function uses a two pointer technique to give the squares of each element 
    in a given array in an ascending order.
    """
    # initialize square element array
    new_arr = StaticArray(arr.size())

    # populate new_arr with squares 
    i = arr.size() - 1
    start = 0
    end = arr.size() - 1

    for num in range(arr.size()):
        if abs(arr[start]) > abs(arr[end]):
            new_arr[i] = arr[start] ** 2
            start += 1
        else: # abs(arr[start]) < abs(arr[end]):
            new_arr[i] = arr[end] ** 2
            end -= 1
        i -= 1

    return new_arr # thus the array is squared and sorted
    

# ------------------- PROBLEM 12 - ADD_NUMBERS ------------------------------


def add_numbers(arr1: StaticArray, arr2: StaticArray) -> StaticArray:
    """
    This function takes two StaticArrays and sums each element with the same index. 
    Returns a new array with resulting sums of elements.
    """
    # finding array size based on magnitude of array
    arr1_index = 0
    # multiplied by 10 ^ i for each element in array 
    for i in range(arr1.size()):
        arr1_index += (arr1[arr1.size() - i - 1] * (10 ** (i)) )
    
    arr2_index =0
    for i in range(arr2.size()):
        arr2_index += (arr2[arr2.size() - i - 1] * (10 ** (i)) )

    val = arr1_index + arr2_index

    # intialize array size
    # if the size ends up being zero, this is a unique case
    if val == 0:
        arr = StaticArray(1)
        arr.set(0,0)
        return arr

    # otherwise, build array
    size = 0

    while(val > 0):
        # look and divide integers by flooring to get nearest whole number
        val = val // 10
        size += 1

    new_array = StaticArray(size)
    val = arr1_index + arr2_index
    # iteration again to fill
    i = 0

    while(val!=0):
      # take reminder
      remainder = val % 10
      # append val
      new_array.set(size - (i + 1), remainder)
      
      val = val // 10;
      i += 1
      
    # return the static  array
    return new_array


# ------------------- PROBLEM 13 - SPIRAL MATRIX -------------------------


def spiral_matrix(rows: int, cols: int, start: int) -> StaticArray:
    """
    TODO: Write this implementation
    """
    # first, construct the big staticarray
    big_array = StaticArray(rows)
    # then add the columns into the big_array by using StaticArrays with size columns
    for row in range(rows):
        big_array.set(row, StaticArray(cols))
    
    num = start
    top = 0
    bottom = rows
    left = 0
    right = cols

    if rows == 1 and cols == 1: # for a column row
        big_array[0][0] = start
        return big_array
    if cols == 1:
        if start < 0:
            for i in rows:
                big_array[i][0] = num
                num -= 1
            return big_array
        else:
            for i in rows:
                big_array[i][0] = num
                num += 1
            return big_array


    while (top < bottom and left < right):
        if start >= 0: # if start val is non-negative, top right downwards first
            for i in range(top, bottom):
                big_array[i][right - 1] = num
                num += 1 # down works
            right -= 1

            for i in range(right, left, -1):
                big_array[bottom - 1][i - 1] = num
                num += 1 # left works
            bottom -= 1

            if not (left < right and top < bottom):
                break

            for i in range(bottom - 1, top, -1): # up works
                big_array[i][left] = num
                num += 1
            left += 1

            for i in range(left - 1, right): # right??
                big_array[top][i] = num
                num += 1
            top += 1

        elif start < 0: # start val is negative, bottom left right first
            for i in range(left, right): # left to right
                big_array[bottom - 1][i] = num
                print(num)
                num -= 1
                print("right")
            bottom -= 1

            for i in range(bottom - 1, top, -1): # bottom to top
                big_array[i][right - 1] = num
                print(num)
                num -= 1
                print("up")
            right -= 1

            if not (left < right and top < bottom):
                break

            for i in range(right, left - 1, -1): # right to left
                big_array[top][i] = num
                print(num)
                num -= 1
                print("left")
            top += 1

            for i in range(top, bottom):
                big_array[i][left] = num
                print(num)
                num -= 1
                print("down")
            left += 1

    return big_array


# ------------------- PROBLEM 14 - TRANSFORM_STRING -------------------------


def transform_string(source: str, s1: str, s2: str) -> str:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(min_max(arr))


    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(min_max(arr))


    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(min_max(arr))


    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)


    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)


    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2**28, -2**31]:
        print(rotate(arr, steps), steps)
    print(arr)


    #print('\n# rotate example 2')
    #array_size = 1_000_000
    #source = [random.randint(-10**9, 10**9) for _ in range(array_size)]
    #arr = StaticArray(len(source))
    #for i, value in enumerate(source):
    #    arr[i] = value
    #print(f'Started rotating large array of {array_size} elements')
    #rotate(arr, 3**14)
    #rotate(arr, -3**15)
    #print(f'Finished rotating large array of {array_size} elements')


    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-105, -99), (-99, -105)]
    for start, end in cases:
        print(start, end, sa_range(start, end))


    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)


    print('\n# sa_sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)],
        [random.randint(-10**7, 10**7) for _ in range(5_000)]
    )
#    for case in test_cases:
#        arr = StaticArray(len(case))
#        for i, value in enumerate(case):
#            arr[i] = value
#        print(arr if len(case) < 50 else 'Started sorting large array')
#        sa_sort(arr)
#        print(arr if len(case) < 50 else 'Finished sorting large array')


    print('\n# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)


    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        result = count_sort(arr)
        print(result if len(case) < 50 else 'Finished sorting large array')


    #print('\n# count_sort example 2')
    #array_size = 5_000_000
    #min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    #max_val = min_val + 998
    #case = [random.randint(min_val, max_val) for _ in range(array_size)]
    #arr = StaticArray(len(case))
    #for i, value in enumerate(case):
    #    arr[i] = value
    #print(f'Started sorting large array of {array_size} elements')
    #result = count_sort(arr)
    #print(f'Finished sorting large array of {array_size} elements')


    print('\n# sa_intersection example 1')
    test_cases = (
        ([1, 2, 3], [3, 4, 5], [2, 3, 4]),
        ([1, 2], [2, 4], [3, 4]),
        ([1, 1, 2, 2, 5, 75], [1, 2, 2, 12, 75, 90], [-5, 2, 2, 2, 20, 75, 95])
    )
    for case in test_cases:
        arr = []
        for i, lst in enumerate(case):
            arr.append(StaticArray(len(lst)))
            for j, value in enumerate(sorted(lst)):
                arr[i][j] = value
        print(sa_intersection(arr[0], arr[1], arr[2]))


    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)


    #print('\n# sorted_squares example 2')
    #array_size = 5_000_000
    #case = [random.randint(-10**9, 10**9) for _ in range(array_size)]
    #arr = StaticArray(len(case))
    #for i, value in enumerate(sorted(case)):
    #    arr[i] = value
    #print(f'Started sorting large array of {array_size} elements')
    #result = sorted_squares(arr)
    #print(f'Finished sorting large array of {array_size} elements')


    print('\n# add_numbers example 1')
    test_cases = (
        ([1, 2, 3], [4, 5, 6]),
        ([0], [2, 5]), ([0], [0]),
        ([2, 0, 9, 0, 7], [1, 0, 8]),
        ([9, 9, 9], [9, 9, 9, 9])
    )
    for num1, num2 in test_cases:
        n1 = StaticArray(len(num1))
        n2 = StaticArray(len(num2))
        for i, value in enumerate(num1):
            n1[i] = value
        for i, value in enumerate(num2):
            n2[i] = value
        print('Original nums:', n1, n2)
        print('Sum: ', add_numbers(n1, n2))


    print('\n# spiral matrix example 1')
    matrix = spiral_matrix(1, 1, 7)
    print(matrix)
    if matrix: print(matrix[0])
    matrix = spiral_matrix(3, 2, 12)
    if matrix: print(matrix[0], matrix[1], matrix[2])


    print('\n# spiral matrix example 2')
    def print_matrix(matrix: StaticArray) -> None:
        rows, cols = matrix.size(), matrix[0].size()
        for row in range(rows):
            for col in range(cols):
                print('{:4d}'.format(matrix[row][col]), end=' ')
            print()
        print()

    test_cases = (
        (4, 4, 1), (3, 4, 0), (2, 3, 10), (1, 2, 1), (1, 1, 42),
        (4, 4, -1), (3, 4, -3), (1, 3, -12), (1, 2, -42),
    )
    for rows, cols, start in test_cases:
        matrix = spiral_matrix(rows, cols, start)
        if matrix: print_matrix(matrix)


    #print('\n# transform_strings example 1')
    #test_cases = ('eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
    #              'dGAqJLcNC0YFJQEB5JJKETQ0QOODKF8EYX7BGdzAACmrSL0PVKC',
    #              'aLiAnVhSV9}_+QOD3YSIYPR4MCKYUF9QUV9TVvNdFuGqVU4$/%D',
    #              'zmRJWfoKC5RDKVYO3PWMATC7BEIIVX9LJR7FKtDXxXLpFG7PESX',
    #              'hFKGVErCS$**!<OS<_/.>NR*)<<+IR!,=%?OAiPQJILzMI_#[+}',
    #              'EOQUQJLBQLDLAVQSWERAGGAOKUUKOPUWLQSKJNECCPRRXGAUABN',
    #              'WGBKTQSGVHHHHHTZZZZZMQKBLC66666NNR11111OKUN2KTGYUIB',
    #              'YFOWAOYLWGQHJQXZAUPZPNUCEJABRR6MYR1JASNOTF22MAAGTVA',
    #              'GNLXFPEPMYGHQQGZGEPZXGJVEYE666UKNE11111WGNW2NVLCIOK',
    #              'VTABNCKEFTJHXATZTYGZVLXLAB6JVGRATY1GEY1PGCO2QFPRUAP',
    #              'UTCKYKGJBWMHPYGZZZZZWOKQTM66666GLA11111CPF222RUPCJT')
    #for case in test_cases:
    #    print(transform_string(case, '612HZ', '261TO'))
