import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stack import Stack
from decorators.time_decorator import time_decorator

@time_decorator
def generate_next_greater_element_array(arr):
    size = len(arr)
    s = Stack(size)
    
    ret_array = [-1] * size
    for ind, i in enumerate(arr[::-1]):
        top_ele = s.top_element()
        if top_ele == -1:
            ret_array[size-ind-1] = top_ele
            s.push(i)
        else:
            # print(top_ele, i, s)
            while top_ele <= i & top_ele != -1:
                # print("here")
                s.pop()
                # print(a, i)
                top_ele = s.top_element()
                
            ret_array[size-ind-1] = top_ele
            s.push(i)
    
    for ind, x in enumerate(zip(arr, ret_array)):
        print(ind, x[0], x[1])
generate_next_greater_element_array([1,463,46,34,643,6,34,63,46,34,32,5634,26,2,2,456,456,32,4643,45,46,3,463,6,34,64,3,64,3])