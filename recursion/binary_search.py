"""
    Binary Search
    Overview
    Given a sorted list (say arr), and a key (say target). The binary search algorithm returns the index of the target element if it is present in the given arr list, else returns -1. Here is an overview of how the the recursive version of binary search algorithm works:

    Given a list with the lower bound (start_index) and the upper bound (end_index).
    Find the center (say mid_index) of the list.
    Check if the element at the center is your target? If yes, return the mid_index.

    Check if the target is greater than that element at mid_index? If yes, call the same function with right sub-array w.r.t center i.e., updated indexes as mid_index + 1 to end_index

    Check if the target is less than that element at mid_index? If yes, call the same function with left sub-array w.r.t center i.e., updated indexes as start_index to mid_index - 1

    Repeat the step above until you find the target or until the bounds are the same or cross (the upper bound is less than the lower bound).
    Complexity Analysis
    Let's look at the time complexity of the recursive version of binary search algorithm.

    Note: The binary search function can also be written iteratively. But for the sake of understanding recurrence relations, we will have a look at the recursive algorithm.

    Here's the binary search algorithm, coded using recursion:
"""


def binary_search(array, target):
    return binary_search_func(array, 0, len(array) - 1, target)


def binary_search_func(array, start_index, end_index, target):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2

    if array[mid_index] == target:
        return mid_index
    elif array[mid_index] > target:
        return binary_search_func(array, start_index, mid_index - 1, target)
    else:
        return binary_search_func(array, mid_index + 1, end_index, target)


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(binary_search(arr, 5))
