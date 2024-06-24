from int2binary import convert2binary
def remove_last_set_bit(n):
    return n & (n-1)

for num in range(10, 33):
    print(f"before {convert2binary(num)} after: {convert2binary(remove_last_set_bit(num))}")