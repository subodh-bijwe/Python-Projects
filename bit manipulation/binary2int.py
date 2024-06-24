def convert2int(binary_string):
    num = 0
    for index, i in enumerate(binary_string[::-1]):
        num += 2**index * eval(i)
    return num

print(convert2int("111"))