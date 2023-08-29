def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        # due to a carry-out, we need to add 1 more digit to store the result
        # thus, append 0 at the end of the array and update the first entry to 1
        A[0] = 1
        A.append(0)
    return A


num1 = [1, 2, 9]
num2 = [1, 3, 9]
num3 = [0, 5, 5]
print(plus_one(num1))
print(plus_one(num2))
print(plus_one(num3))
