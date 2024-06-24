def convert_to_bitsize(str1, bitsize):
    return "0"*(bitsize-len(str1)) + str1

def remove_zeroes(str1):
    str2 = ""
    append = False
    for i in str1:
        if eval(i) and append == False:
            append = True
        if append:
            str2 += i
    return str2

# print(convert_to_bitsize("111"))
# print(remove_zeroes(convert_to_bitsize("111")))