from stl_tools import numpy2stl
import numpy as np


def monkey_function(x, y):
    output = (x ** 3 - 3 * x * (y ** 2))
    if output < -4500:
        return -4500
    else:
        return output


z_array = np.zeros((300, 260))

for y in range(-130, 130, 1):
    line_of_z_values = []
    for x in range(-150, 150, 1):
        z_array[x + 150][y + 130] = monkey_function(x / 10, y / 10)

numpy2stl(z_array, "monkey_saddle.stl", scale=0.05, mask_val=5., solid=True)
