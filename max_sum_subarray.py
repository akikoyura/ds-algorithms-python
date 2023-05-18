import math


def max_sum_subarray(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    for element in arr[1:]:
        current_sum = max(element, current_sum + element)
        max_sum = max(max_sum, current_sum)
    return max_sum


if __name__ == '__main__':
    arr = [1, 2, 3, -4, 6]
    arr1 = [1, 2, -5, -4, 1, 6]
    print(max_sum_subarray(arr))
    print(max_sum_subarray(arr1))
