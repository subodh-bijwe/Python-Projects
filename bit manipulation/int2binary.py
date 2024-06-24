def convert2binary(num):
    if num == 0:
        return "0"
    res = ""
    while num >= 1:
        res += str(num%2)
        num = num//2
    return res[::-1]

