def right_shift(str1, shift_by):
    if shift_by >= len(str1):
        return '0'
    elif shift_by == 0:
        return str1
    return str1[:-shift_by]


print(f"11010 after right shift is {right_shift('11010', 6)}")
print(f"11010 after right shift is {right_shift('11010', 5)}")
print(f"11010 after right shift is {right_shift('11010', 4)}")
print(f"11010 after right shift is {right_shift('11010', 3)}")
print(f"11010 after right shift is {right_shift('11010', 2)}")
print(f"11010 after right shift is {right_shift('11010', 1)}")
print(f"11010 after right shift is {right_shift('11010', 0)}")