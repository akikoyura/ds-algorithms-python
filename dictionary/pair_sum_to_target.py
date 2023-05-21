"""
    Given an input_list and a target, return the pair of indices in the list that holds the values which sum to the target.
    for example,
    input_list = [1,5,7,9] and target = 8, and the answer would be [0,3]

"""


def pair_sum_to_target(input_list, target):
    # TODO: Write pair sum to target function
    sum = {}
    for index, value in enumerate(input_list):
        remain = target - value
        if sum.get(remain) is not None:
            return [index, sum.get(remain)]
        else:
            sum[value] = index

    return -1


def test_function(test_case):
    output = pair_sum_to_target(test_case[0], test_case[1])
    print(output)
    if sorted(output) == test_case[2]:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_case_1 = [[1, 5, 9, 7], 8, [0, 3]]
    test_function(test_case_1)

    test_case_2 = [[10, 5, 9, 8, 12, 1, 16, 6], 16, [0, 7]]
    test_function(test_case_2)

    test_case_3 = [[0, 1, 2, 3, -4], -4, [0, 4]]
    test_function(test_case_3)
