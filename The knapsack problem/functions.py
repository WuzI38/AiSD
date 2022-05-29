import numpy as np  # cuz performance reasons -> GOTTA GO FAST!!!
from random import randint


# weights -> values -> worth
# generate n items with values: 1 - max_value, size 1 - max_value
def generate_items(n, max_weight, max_value):
    # create np array with weights, values and 3rd row for values/weight
    arr = np.zeros((3, n))

    # generate smaller and bigger elements separately to increase response diversity (more smaller elements)
    half_n = n // 2
    for x in range(half_n):
        arr[0, x] = randint(1, max_weight // 2)
        arr[1, x] = randint(1, int(max_value * 0.6))
    for x in range(half_n, n):
        arr[0, x] = randint(max_weight // 2 + 1, max_weight)
        arr[1, x] = randint(1, max_value)

    # calculate 3rd row
    arr[2, :] = arr[1, :] / arr[0, :]

    return arr


# load array from a text file (size, weights, values)
def items_from_file(file):
    f = open(file, 'r')
    lines = f.readlines()

    arr = np.empty([3, int(lines[0])])
    for index, line in enumerate(lines[1:]):
        arr[index, :] = list(map(int, line.rstrip().split()))

    arr[2, :] = arr[1, :] / arr[0, :]

    return arr


# calculate max value using 3rd row of generated array for backpack with given size (greedy algorithm)
def greed(array, size):
    # it looks awful, but sorts the array by 3rd row
    sorted_items = array[:, array[2, :].argsort()[::-1]]

    items_value = 0
    for index, value in enumerate(sorted_items[1]):
        if sorted_items[0, index] <= size:
            size -= sorted_items[0, index]
            items_value += value

    return int(items_value)


# solve problem using dynamic algorithm - return cost matrix
def dp(array, size, return_max=False):
    # generating cost matrix
    cost_matrix = np.zeros((array[0].size + 1, size + 1))
    for x in range(1, array[0].size + 1):
        for y in range(1, size + 1):
            if int(array[0, x - 1]) > y:
                cost_matrix[x, y] = cost_matrix[x - 1, y]
            else:
                cost_matrix[x, y] = max(cost_matrix[x - 1, y], cost_matrix[x - 1, y - int(array[0, x - 1])] + array[1, x - 1])

    # if you want to see the max value, just add true as the last parameter
    if return_max:
        return int(cost_matrix[-1, -1])

    return cost_matrix


# return set of items for optimal shipping using cost matrix
def optimal_shipping(array, cost_matrix):
    x = array[0].size
    y = cost_matrix[0].size - 1
    items = []

    while y > 0 and x > 0:
        if cost_matrix[x, y] > cost_matrix[x - 1, y]:
            items.append((array[0, x - 1], array[1, x - 1]))
            y -= int(array[0, x - 1])
            x -= 1
        else:
            x -= 1

    return items
