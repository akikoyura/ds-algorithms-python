def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num):
    # Base Case
    if num <= 1:
        return [""]

    # If `num` is single digit, get the LIST having one element - the associated string
    elif 1 < num <= 9:
        return list(get_characters(num))

    # Otherwise `num` >= 10. Find the unit's (last) digits of `num`
    last_digit = num % 10
    ''' Step 1 '''
    # Recursive call to the same function with "floor" of the `num/10`
    small_output = keypad(num // 10)

    ''' Step 2 '''
    # Get the associated string for the `last_digit`
    keypad_string = get_characters(last_digit)  # returns a string

    ''' Permute the characters of results obtained from Step 1 and Step 2 '''
    output = list()

    ''' 
    The Idea
    Each character of keypad_string must be appended to the
    end of each string available in the small_output
    '''
    for character in keypad_string:
        for item in small_output:
            new_item = item + character
            output.append(new_item)

    return output


def test_keypad(input, expected_output):
    if sorted(keypad(input)) == expected_output:
        print("Yay. We got it right.")
    else:
        print("Oops! That was incorrect.")


if __name__ == '__main__':
    # Base case: list with empty string
    input = 0
    expected_output = [""]
    test_keypad(input, expected_output)

    # Example case
    input = 23
    expected_output = sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    test_keypad(input, expected_output)