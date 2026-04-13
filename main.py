import numpy as np

# Multidimensional Arrays
my_list = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']], [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '']]])

# print(my_list.shape)
# print(my_list.ndim)

mama = my_list[0, 0, 0] + my_list[0, 2, 0] + my_list[0, 1, 1]
print(mama)
