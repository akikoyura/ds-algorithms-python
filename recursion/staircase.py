def staircase(n):
    # Base Case - What holds true for minimum steps possible i.e., n == 0, 1, 2 or 3?
    # Return the number of ways the child can climb n steps.
    # Recursive Step - Split the solution into base case if n > 3.

    if n <= 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)


def test_function(test_cases):
    n = test_cases[0]
    solution = test_cases[1]
    output = staircase(n)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    n = 3
    sol = 4
    test_case = [n, sol]
    test_function(test_case)
