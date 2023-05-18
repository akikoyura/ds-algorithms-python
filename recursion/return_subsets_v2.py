def subsets(nums):
    result = []
    generate_subsets(nums, 0, [], result)
    return result


def generate_subsets(nums, index, current, result):
    result.append(list(current))
    for i in range(index, len(nums)):
        current.append(nums[i])
        generate_subsets(nums, i + 1, current, result)
        current.pop()


if __name__ == '__main__':
    nums = [1, 2, 3]
    result = subsets(nums)
    print(result)
