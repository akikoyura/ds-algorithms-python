def add(num_one, num_two):
    output = num_one + num_two
    custom_print(output, num_one, num_two)
    return output


def custom_print(output, num_one, num_two):
    print("The sum of {} and {} is: {}".format(num_one, num_two, output))


if __name__ == '__main__':
    result = add(5, 7)
    print(result)
