from int2binary import convert2binary
def check_if_kth_bit_is_set(num, k, right=False):
    if right:
        return True if (num >> k) & 1 else False
    else:
        return True if num & (1 << k) else False

    
for i in range(16):
    print(f"right:   {convert2binary(i)} {check_if_kth_bit_is_set(i, 10, True)}")
    print(f"left :   {convert2binary(i)} {check_if_kth_bit_is_set(i, 10)}")