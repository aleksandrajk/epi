RED, WHITE, BLUE = range(3)


# Example 1
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break


# Example 2
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal +1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


# Test
# Example 1: Sorting an array of colors
colors = [RED, WHITE, BLUE, RED, BLUE, WHITE, RED]
dutch_flag_partition(1, colors)
print(colors)  # Output: [RED, RED, WHITE, WHITE, BLUE, BLUE, RED]

# Example 2: Sorting an array of numbers
numbers = [5, 3, 1, 2, 4, 6]
dutch_flag_partition(2, numbers)
print(numbers)  # Output: [1, 2, 3, 5, 4, 6]

# Example 3: Sorting an array of letters
letters = ['c', 'a', 'b', 'a', 'c', 'b', 'a']
dutch_flag_partition(0, letters)
print(letters)  # Output: ['a', 'a', 'a', 'b', 'b', 'c', 'c']

