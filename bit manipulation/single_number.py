def find_single_number(arr):
    ret = 0
    for i in arr:
        ret ^= i
    return ret

print(find_single_number([4,1,2,2,1]))
