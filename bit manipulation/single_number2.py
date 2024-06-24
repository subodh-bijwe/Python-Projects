def find_single_number2(arr):
    ret = 0
    for i in arr:
        ret ^= i
    return ret

print(find_single_number2([5,3,2,2,4,5,5,3,2,3]))
