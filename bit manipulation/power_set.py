from int2binary import convert2binary
def print_all_subsets(arr):
    n = 2**len(arr)
    print(arr)
    ret_list = []
    for i in range(n):
        m = convert2binary(i)
        temp_list = []
        m = m[::-1]
        for ind, x in enumerate(m):
            
            if eval(x) == 1:
                temp_list.append(arr[ind])
        ret_list.append(temp_list)
    return ret_list

print(print_all_subsets([1,2,3,4,5,6,7,8,9,0]))