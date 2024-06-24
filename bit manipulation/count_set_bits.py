from int2binary import convert2binary
def count_set_bits(n):
    c = 0
    # while n > 0:
    #     c += n & 1
    #     n = n >> 1
    
    while n != 0:
        n = n & (n-1)
        c += 1
    return c

# for num in range(33):
#     print(f"{num} : {convert2binary(num)} -> {count_set_bits(num)}")