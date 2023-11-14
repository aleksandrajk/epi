# Given n, return all primes up to and including n.
def generate_primes_improved(n):
    if n < 2:
        return []
    # Calculates the size of the boolean list 'is_prime'. This list will represent odd numbers starting from 3 up to n,
    # as even numbers greater than 2 are not prime.
    size = (n - 3) // 2 + 1
    primes = [2]
    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3
            primes.append(p)
            # j (long) as p^2 can overflow
            # This loop iterates over multiples of the prime number p starting from p^2
            # and marks them as non-prime in the is_prime list.
            for j in range(2 * i**2 + 6 * i + 3, size, p):
                is_prime[j] = False
    return primes


result11 = generate_primes_improved(12)
result64 = generate_primes_improved(63)
print(result11)
print(result64)


# The improvement in this version is that it only stores information for odd numbers, reducing memory usage compared 
# to the 'generate_primes.py'. Additionally, it avoids potential overflow issues by using a 64-bit integer type (long), 
# ensuring that calculations involving squares of primes do not exceed the maximum representable value.
