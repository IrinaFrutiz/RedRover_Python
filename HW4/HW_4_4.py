from functools import reduce
from HW4.HW_4_3 import my_list


new_list = reduce(lambda x, y: x * y, my_list)

print(new_list)
