def even_odd(arrs):
    next_even, next_odd = 0, len(arrs) - 1
    while next_even < next_odd:
        if arrs[next_even] % 2 == 0:
            next_even += 1
        else:
            arrs[next_even], arrs[next_odd] = arrs[next_odd], arrs[next_even]
            next_odd -= 1
    return arrs     


arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_odd(arr1))
# [0, 10, 2, 8, 4, 6, 7, 5, 9, 3, 1]

arr2 = [0, 2, 9, 4, 6, 5, 7, 8, 3, 10, 1]
print(even_odd(arr2))
# [0, 2, 10, 4, 6, 8, 7, 3, 5, 1, 9]
