def reverse(x):
    result, x_rem = 0, abs(x)
    while x_rem:
        result = result*10 + x_rem % 10
        x_rem //= 10
    return -result if x < 0 else result


print(reverse(1234))
print(reverse(17))
print(reverse(0b1111))
