def swap_bits(x, i, j):
    # Extract the i-th and j-th bits, and see if they differ.
    if (x >> i) & 1 != (x >> j) & 1:
        # i-th and j-th bits differ. We will swap them by flipping the values.
        # Select the bits to flip with bit_mask. Since x^1 = 0 when x=1 and
        # 1 when x = 0, we can perform the flip XOR. This XOR operation flips the bits at positions i and j, effectively swapping them.
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


print(swap_bits(18, 2, 4))  # get 6
print(swap_bits(73, 1, 6))  # get 11
print(swap_bits(10, 1, 3))  # get 10
print(swap_bits(73, 1, 4))  # get 73
