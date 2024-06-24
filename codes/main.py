def convert(s: str, numRows: int) -> str:
    # print(len(s))
    to_sum = 2*numRows - 2
    ret = ""
    for i in range(to_sum):
        m = i
        while m < len(s):
            print(m, s[m])
            ret += s[m]
            m += to_sum
    return ret

# a = convert("PAYPALISHIRING", 3)
# print(a, len(a))
# a = convert("PAYPALISHIRING", 4)
# print(a, len(a))
# a = convert("PAYPALISHIRING", 6)
# print(a, len(a))

# a = convert("abcdefghijklmnopqrstuvwxyz", 3)
# print(a, len(a))
a = convert("abcdefghijklmnopqrstuvwxyz", 4)
print(a, len(a))
# a = convert("abcdefghijklmnopqrstuvwxyz", 6)
# print(a, len(a))














