def duplicate_number(arr):
    total = 0
    val = 0
    for index in range(len(arr)):
        total = total + arr[index]
        val = val + index
    return val - total


if __name__ == '__main__':
    arr = [0, 2, 3, 1, 4, 5, 3]
    print(duplicate_number(arr))
