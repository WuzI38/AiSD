import numpy as np
from math import log
import json
from matplotlib import pyplot as plt
from scipy.ndimage import gaussian_filter1d

INITIAL = 400
STEP = 100
MEASURE_POINTS = 30
LEARNING_RATE = 0.1
ITERATIONS = 250


def saveData(dictionary_data, file_name):  # data -> json file
    with open(file_name, "w") as outfile:
        json.dump(dictionary_data, outfile)


def getData(file):  # json file -> data
    with open(file) as json_file:
        d = json.load(json_file)
        return d


def hypothesis_log(x, t0, t1):
    return t0 + t1 * log(x, 2)


def hypothesis_poly(x, t0, t1):
    return t0 + t1 * x ** 2


def cost_function(y, t0, t1, hypothesis):
    sm = 0
    for x in range(MEASURE_POINTS):
        # print((INITIAL + x * STEP) / (INITIAL + (MEASURE_POINTS - 1) * STEP), y[x], t0, t1)
        sm += (hypothesis((INITIAL + x * STEP) / (INITIAL + (MEASURE_POINTS - 1) * STEP), t0, t1) - y[x]) ** 2
        # print(sm)
    return sm / (2 * MEASURE_POINTS)


data = getData("data.json")
# data_fixed = {}

"""for alg in data:
    for d_type, measures in data[alg].items():"""


def gd(measures, iters, learning_rate, hypothesis, cost_func_history=False):
    theta0 = np.random.random()
    theta1 = np.random.random()
    cost_history = []
    for i in range(iters):
        sigma0 = 0
        sigma1 = 0
        for x in range(MEASURE_POINTS):
            x_ = (INITIAL + x * STEP) / (INITIAL + (MEASURE_POINTS - 1) * STEP)
            sigma0 += hypothesis(x_, theta0, theta1) - measures[x]
            sigma1 += (hypothesis(x_, theta0, theta1) - measures[x]) * x_
        theta0 -= (learning_rate * sigma0) / MEASURE_POINTS
        theta1 -= (learning_rate * sigma1) / MEASURE_POINTS
        if cost_func_history:
            cost_history.append(cost_function(measures, theta0, theta1, hypothesis))
    if cost_func_history:
        return theta0, theta1, cost_history
    return theta0, theta1


data_merge = data["heap"]["decreasing"]
[th0, th1] = [-1, -1]

while th0 < 0:
    [th0, th1] = gd(data_merge, ITERATIONS, LEARNING_RATE, hypothesis_log)
points = [(INITIAL + x * STEP) for x in range(MEASURE_POINTS)]
fixed_data = [hypothesis_log(points[x] / (INITIAL + (MEASURE_POINTS - 1) * STEP), th0, th1) for x in range(MEASURE_POINTS)]

# Fix the data
mean_square_error = cost_function(data_merge, th0, th1, hypothesis_log) * 2


fxd_2 = []
for x in range(MEASURE_POINTS):
    if ((data_merge[x] - fixed_data[x]) ** 2 <= mean_square_error and data_merge[x] != 0) or fixed_data[x] <= 0:
        fxd_2.append(data_merge[x])
    else:
        fxd_2.append(fixed_data[x])


data_y_normal = data_merge
data_y_fixed = fixed_data
# data_y_fixed = fxd_2
# data_y_fixed = gaussian_filter1d(data_y_fixed, sigma=2)
# data_y_normal = gaussian_filter1d(data_y_normal, sigma=2)
data_x = points

# plt.yscale("log")
plt.plot(data_x, data_y_normal, label="Normal", color='r')
plt.plot(data_x, data_y_fixed, label="Fixed", color='g')

plt.xlabel("Data size")
plt.ylabel("Time")
plt.title("Machine learning is fun")
plt.legend()

plt.show()


"""data_y = gd(data["merge"]["increasing"], ITERATIONS, LEARNING_RATE, True)[2]
data_x = [x for x in range(ITERATIONS)]

plt.plot(data_x, data_y, label="cost_func_value", color='r')
plt.xlabel("Iterations")
plt.ylabel("Value")
plt.title("Machine learning is fun")
plt.legend()

plt.show()"""
