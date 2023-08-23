import random


def uniform_random(lower_bound, upper_bound):
    number_of_outcomes = upper_bound - lower_bound + 1
    while True:
        result, i = 0, 0
        while (1 << i) < number_of_outcomes:
            result = (result << 1) | int(random.uniform(0, 2))
            i += 1
        if result < number_of_outcomes:
            break
    return result + lower_bound


print(uniform_random(1, 6))
print(uniform_random(100, 300))
