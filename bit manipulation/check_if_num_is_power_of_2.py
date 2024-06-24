def check_if_power_of_2(num):
    return True if num & (num-1) == 0 else False

for num in range(33):
    print(f"{num} : {check_if_power_of_2(num)}")