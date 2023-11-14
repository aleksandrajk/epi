# Given n, return all primes up to and including n.
def generate_primes(n):
    primes = []
    # is_prime[p] represents if p is prime or not
    is_prime = [False, False] + [True] * (n-1)
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            # Sieve p's multiples
            for i in range(p, n + 1, p):
                is_prime[i] = False
    return primes


result11 = generate_primes(11)
result64 = generate_primes(64)
print(result11)  # will print [2, 3, 5, 7, 11]
print(result64)  # will print [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
