from int2binary import convert2binary
def toggle_ith_bit(n, i):
    return n ^ (1 << i)

for num in range(10, 33):
    print(f"before {convert2binary(num)} after: {convert2binary(toggle_ith_bit(num, 3))}")