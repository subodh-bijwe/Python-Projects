from int2binary import convert2binary
def clear_ith_bit(n, i):
    return n & ~(1 << i)

print(convert2binary(clear_ith_bit(127, 2)))