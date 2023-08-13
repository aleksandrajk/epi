def closest_int_same_bit_count(x):
    NUM_UNSIGNED_BITS = 64
    for i in range(NUM_UNSIGNED_BITS -1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            x ^= (1 << i) | (1 << (i +1))
            return x
    # Raise error if all bits of x are 0 or 1
    raise ValueError('All bits are 0 or 1')


print(closest_int_same_bit_count(7))
print(0b111)
print(0b1011)
print(closest_int_same_bit_count(92))
print(0b1011100)
print(0b1011010)
