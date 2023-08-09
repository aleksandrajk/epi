# Computing parity of a word


def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


print(count_bits(0b1100))


def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


print(parity(0b1101))


def parity_drop_lowest_bit(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1  # Drops the lowest set bit of x
    return result


print(parity_drop_lowest_bit(0b00101100))


def parity2(x, PRECOMPUTED_PARITY=None):
    MASK_SIZE = 16
    BIT_MASK  = 0xFFFF
    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
            PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^ PRECOMPUTED_PARITY[x & BIT_MASK])


def parity3(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1

