import numpy as np

# Multidimensional Arrays

'''my_list = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']], [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '']]])

print(my_list.shape)
print(my_list.ndim)

mama = my_list[0, 0, 0] + my_list[0, 2, 0] + my_list[0, 1, 1]
print(mama) 

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

# Scalar Arithmetic Operations

# radii = np.array([2, 4, 6])
# Area = np.pi * radii ** 2
# print((Area))

# print([number * 2])
# print([number - 1])
# print([number ** 3])
# print(np.round(number))
# print(np.sqrt(number))

leaders = np.array([12, 87, 55, 90, 76, 43, 33, 9])
# print(leaders >= 15)
leaders[leaders >= 50] = 100
print(leaders) 

# Broadcasting
list1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])  # 2d array
list2 = np.array([[2], [4], [6], [8], [10], [12], [14], [16], [18], [20]])

print(list1.shape)
print(list2.shape)
print(list1 * list2)

# Aggregrate Function

values = np.array([[0, 1, 3, 5, 7],
                   [2, 4, 6, 8, 10]])

print(np.sum(values))
print(np.min(values))
print(np.max(values))
print(np.argmin(values))
print(np.argmax(values))
print(np.sum(values, axis=0))
print(np.sum(values, axis=1)) 

# filtering

temperature = np.array([[22, 43, 75, 21, 98, 45, 14],
                        [-2, -77, 6, -23, 51, 87, -15]])

winter = temperature[temperature <= 6]
sunny = temperature[(temperature >= 20) & (temperature <= 22)]
killer = np.where(temperature >= 43, temperature, 0)
print(winter)
print(sunny)
print(killer) '''

# Random Number
# random = np.random.default_rng()
# print(random.integers(low=1, high=237, size=(5, 3)))

# random = np.random.uniform()
# print(np.random.uniform(low=1, high=237, size=(2, 1)))

random = np.random.default_rng()
cars = np.array(["Mercedes", "BMW", "Tesla", "Audi", "BYD"])
car = random.choice(cars, size=(2, 1))
print(car)
