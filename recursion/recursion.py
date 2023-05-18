import copy


def sum_array(array):
    # Base case
    if len(array) == 1:
        return array[0]

    return array[0] + sum_array(array[1:])


def sum_array_index(array, idx):
    if len(array) - 1 == idx:
        return array[idx]

    return array[idx] + sum_array_index(array, idx + 1)


def reverse_string(input):
    if len(input) == 0:
        return ""

    else:
        first_char = input[0]
        the_rest = slice(1, None)
        sub_str = input[the_rest]

        # Recursive call
        reversed_substr = reverse_string(sub_str)
        return reversed_substr + first_char


def is_palindrome(input):
    # Termination / Base Condition
    if len(input) <= 1:
        return True
    else:
        first_char = input[0]
        last_char = input[-1]

        # sub_input is input with first and last char removed
        sub_input = input[1:-1]

        # recursive call, if first and last char are identical, else return False
        return (first_char == last_char) and is_palindrome(sub_input)


def add_one(arr):
    # Base case
    if arr == [9]:
        return [1, 0]

    # A simple case, where we just need to increment the last digit
    if arr[-1] < 9:
        arr[-1] += 1

    # Case when the Last digit is 9.
    else:
        # Recursive call
        # We have used arr[:-1] that means all elements of the list except the last one.
        # Example, for original input arr=[1,2,9], we will pass[1,2] in next call
        arr = add_one(arr[:-1]) + [0]
    return arr


def permute(input_list):
    finalCompoundList = []  # compoundList to be returned

    if len(input_list) == 0:
        finalCompoundList.append([])
    else:
        first_element = input_list[0]  # Pick one element to be permuted
        after_first = slice(1, None)
        rest_list = input_list[after_first]

        # Call the recursive function to split the `rest_list` further until it meets the base condition
        # iterating through all lists of the `compoundList` returned from previous recursive call
        sub_compoundList = permute(rest_list)

        for alist in sub_compoundList:
            # permuted the first_element at all positions 0,1,2,... len(alist) in each iteration
            for j in range(0, len(alist) + 1):
                # A normal copy / assignment will change alist[j] element
                blist = copy.deepcopy(alist)

                # A new List with size +1 as compared to alist
                # is created by inserting the `first_element` at position j in blist
                blist.insert(j, first_element)

                # Append the newly created list to the finalCompoundList
                finalCompoundList.append(blist)

    return finalCompoundList


def permutations(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]

    result = []
    for i in range(len(lst)):
        m = lst[i]
        remaining = lst[:i] + lst[i + 1:]
        for p in permutations(remaining):
            result.append([m] + p)
    return result


def string_permutation(string):
    return return_permutations(string, 0)


def return_permutations(string, index):
    # output to be returned
    output = list()

    # Termination / Base condition
    if index >= len(string):
        return [""]

    # recursive function call
    small_output = return_permutations(string, index + 1)

    # pick a character
    current_char = string[index]

    # Iterate over each sub-string available in the list returned from previous call
    for subString in small_output:
        # place the current character at different indices of the sub-string
        for index in range(len(small_output[0]) + 1):
            # Make use of the sub-string of previous output, to create a new sub-string.
            new_subString = subString[0: index] + current_char + subString[index:]
            print(new_subString)
            output.append(new_subString)
            print(output)

    return output


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


# Recursion Solution
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


if __name__ == '__main__':
    print(sum_array([2, 3, 4, 1, 5]))
    print(sum_array_index([1, 2, 3, 4], 0))

    print(is_palindrome("madam"))
    print(add_one([1, 2, 9]))

    # print(permute([0, 1, 2]))
    print(permutations([0, 1, 2]))
    print(keypad(23))
