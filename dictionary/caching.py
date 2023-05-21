def stair_case(n):
    # Base case - What holds true for minimum steps possible i.e., n == 1 ?
    # Return the number of ways the child can climb one step.
    # Inductive Hypothesis - What holds true for n == 2 and n == 3 ? Return the number of ways to climb them.
    # Inductive Step ( n > 3 ) - use Inductive Hypothesis to formulate a solution
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return stair_case(n - 1) + stair_case(n - 2) + stair_case(n - 3)


def test_function(test_case):
    answer = stair_case(test_case[0])
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")

