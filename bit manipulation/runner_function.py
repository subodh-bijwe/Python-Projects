from int2binary import convert2binary
from binary2int import convert2int
for i in range(5, -1, -1):
    j = convert2binary(i)
    k = convert2int(j)
    print(f"Binary of {i} is {j} and number of {j} is {k}")
    assert i == k