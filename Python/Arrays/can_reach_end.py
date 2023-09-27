def can_reach_end(arr):
    furthest_reach_so_far, last_index = 0, len(arr) - 1
    i = 0
    while i <= furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, arr[i] + i)
        i += 1
    return furthest_reach_so_far >= last_index


arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [3, 3, 1, 0, 2, 1]
print(can_reach_end(arr1))  # False
print(can_reach_end(arr2))  # True
