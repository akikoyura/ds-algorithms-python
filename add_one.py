def add_one(arr):
    if arr[-1] < 9:
        arr[len(arr) - 1] = arr[-1] + 1


# A helper function for Test Cases
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")


if __name__ == '__main__':
    # Test Case 2
    arr = [1, 2, 3]
    solution = [1, 2, 4]
    test_case = [arr, solution]
    test_function(test_case)
