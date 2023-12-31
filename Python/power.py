def power(x, y):
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x
    while power:
        if power & 1:
            result *= x
        x, power = x*x, power >> 1
    return result


print(power(2, 3))
print(power(2, -4))
print(power(10, 0))
