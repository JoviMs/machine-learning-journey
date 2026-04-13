import numpy as np

# Multidimensional Arrays

'''my_list = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']], [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '']]])

print(my_list.shape)
print(my_list.ndim)

mama = my_list[0, 0, 0] + my_list[0, 2, 0] + my_list[0, 1, 1]
print(mama) '''

# Slicing

bogey = np.array([
    [2,   4,   6,    8],
    [10, 12, 14, 16],
    [18, 20, 22, 24],
    [26, 28, 30, 32]])
# start:end:step
# print(bogey[2])
# print(bogey[0:4:3])
# print(bogey[:, 1])
# print(bogey[:, 0:3])
print(bogey[:, ::-3])
