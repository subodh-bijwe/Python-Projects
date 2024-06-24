# given start and goal as two positive integers
# return number of bit flips to convert start to goal
from count_set_bits import count_set_bits
from int2binary import convert2binary
def flip_bits(start, goal):
    diff = start ^ goal
    return count_set_bits(diff)

for num in range(33):
    print(f"{convert2binary(num), convert2binary(128)} -> {flip_bits(num, 128)}")