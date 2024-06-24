def set_ith_bit_to_1(n, i):
    return n | 1 << i

print(set_ith_bit_to_1(set_ith_bit_to_1(set_ith_bit_to_1(0, 5), 2), 3))