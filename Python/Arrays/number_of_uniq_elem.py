def number_of_uniq_elem(arr):
    if not arr:
        return 0

    write_index = 1
    for i in range(1, len(arr)):
        if arr[write_index - 1] != arr[i]:
            arr[write_index] = arr[i]
            write_index += 1
    return write_index


arr1 = [0, 44, 2, 2, 8, 50, 17, 18, 1, 1, 1]
arr2 = [3, 3, 1, 0, 2, 1]
print(number_of_uniq_elem(arr1))
print(number_of_uniq_elem(arr2))
