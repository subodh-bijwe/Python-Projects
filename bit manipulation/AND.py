from bitsize_converter import convert_to_bitsize, remove_zeroes
def and_function(str1, str2):
    str1 = convert_to_bitsize(str1)
    str2 = convert_to_bitsize(str2)
    fin = ""
    for i, j in zip(str1, str2):
        if i == "1" and j == "1":
            fin += "1"
        else:
            fin += "0"
    return fin

print(remove_zeroes(and_function("1111", "0010")))