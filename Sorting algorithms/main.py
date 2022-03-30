import algorithms_
import time
import json
from matplotlib import pyplot as plt
from scipy.ndimage import gaussian_filter1d
import sys

algorithms = algorithms_.Algorithm
generate = algorithms_.Generator

sys.setrecursionlimit(3000)

INITIAL = 1000
STEP = 300
MEASURE_POINTS = 30
colors = {
    "insertion": 'b',
    "selection": 'g',
    "heap": 'r',
    "merge": 'y',
    "random": 'b',
    "increasing": 'g',
    "decreasing": 'r',
    "constant": 'y',
    "v_shape": 'c',
    "middle": 'g',
    "extreme": 'r'
}


# 1.insertion 2.selection 3.heap 4.merge

def measure(initial_data, data_step, measure_points, iterations=1):  # return data as dictionary
    # Initialize exec_time dictionary
    exec_time = dict()
    exec_time["insertion"] = {"random": [0 for _ in range(measure_points)], "increasing": [0 for _ in range(measure_points)],
                              "decreasing": [0 for _ in range(measure_points)], "constant": [0 for _ in range(measure_points)],
                              "v_shape": [0 for _ in range(measure_points)]}
    exec_time["selection"] = {"random": [0 for _ in range(measure_points)], "increasing": [0 for _ in range(measure_points)],
                              "decreasing": [0 for _ in range(measure_points)], "constant": [0 for _ in range(measure_points)],
                              "v_shape": [0 for _ in range(measure_points)]}
    exec_time["heap"] = {"random": [0 for _ in range(measure_points)], "increasing": [0 for _ in range(measure_points)],
                         "decreasing": [0 for _ in range(measure_points)], "constant": [0 for _ in range(measure_points)],
                         "v_shape": [0 for _ in range(measure_points)]}
    exec_time["merge"] = {"random": [0 for _ in range(measure_points)], "increasing": [0 for _ in range(measure_points)],
                          "decreasing": [0 for _ in range(measure_points)], "constant": [0 for _ in range(measure_points)],
                          "v_shape": [0 for _ in range(measure_points)]}

    data_size = initial_data

    for point in range(measure_points):
        for _ in range(iterations):
            # Generate data
            random_data = generate.rand(data_size)
            increasing_data = generate.increasing(data_size)
            decreasing_data = generate.decreasing(data_size)
            constant_data = generate.constant(data_size)
            v_shape_data = generate.v_shape(data_size)

            # Measure time for each algorithm and add average value to exec_time

            # 1 insertion sort
            start_time = time.process_time()
            algorithms.insertion_sort(random_data)
            exec_time["insertion"]["random"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.insertion_sort(increasing_data)
            exec_time["insertion"]["increasing"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.insertion_sort(decreasing_data)
            exec_time["insertion"]["decreasing"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.insertion_sort(constant_data)
            exec_time["insertion"]["constant"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.insertion_sort(v_shape_data)
            exec_time["insertion"]["v_shape"][point] += (time.process_time() - start_time) / iterations

            # 2 selection sort
            start_time = time.process_time()
            algorithms.selection_sort(random_data)
            exec_time["selection"]["random"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.selection_sort(increasing_data)
            exec_time["selection"]["increasing"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.selection_sort(decreasing_data)
            exec_time["selection"]["decreasing"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.selection_sort(constant_data)
            exec_time["selection"]["constant"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.selection_sort(v_shape_data)
            exec_time["selection"]["v_shape"][point] += (time.process_time() - start_time) / iterations

            # 3 heap sort
            start_time = time.process_time()
            algorithms.heap_sort(random_data)
            exec_time["heap"]["random"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.heap_sort(increasing_data)
            exec_time["heap"]["increasing"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.heap_sort(decreasing_data)
            exec_time["heap"]["decreasing"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.heap_sort(constant_data)
            exec_time["heap"]["constant"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.heap_sort(v_shape_data)
            exec_time["heap"]["v_shape"][point] += (time.process_time() - start_time) / iterations

            # 4 merge sort
            start_time = time.process_time()
            algorithms.merge_sort(random_data)
            exec_time["merge"]["random"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.merge_sort(increasing_data)
            exec_time["merge"]["increasing"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.merge_sort(decreasing_data)
            exec_time["merge"]["decreasing"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.merge_sort(constant_data)
            exec_time["merge"]["constant"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.merge_sort(v_shape_data)
            exec_time["merge"]["v_shape"][point] += (time.process_time() - start_time) / iterations

        # Increase data size
        data_size += data_step
    return exec_time


def saveData(dictionary_data, file_name):  # data -> json file
    with open(file_name, "w") as outfile:
        json.dump(dictionary_data, outfile)


def getData(file):  # json file -> data
    with open(file) as json_file:
        d = json.load(json_file)
        return d


def measure_heap_merge(initial_data, data_step, measure_points, iterations=1):  # return data as dictionary
    # Initialize exec_time dictionary
    exec_time = dict()
    exec_time["heap"] = {"random": [0 for _ in range(measure_points)], "increasing": [0 for _ in range(measure_points)],
                         "decreasing": [0 for _ in range(measure_points)], "constant": [0 for _ in range(measure_points)],
                         "v_shape": [0 for _ in range(measure_points)]}
    exec_time["merge"] = {"random": [0 for _ in range(measure_points)], "increasing": [0 for _ in range(measure_points)],
                          "decreasing": [0 for _ in range(measure_points)], "constant": [0 for _ in range(measure_points)],
                          "v_shape": [0 for _ in range(measure_points)]}

    data_size = initial_data

    for point in range(measure_points):
        for _ in range(iterations):
            # Generate data
            random_data = generate.rand(data_size)
            increasing_data = generate.increasing(data_size)
            decreasing_data = generate.decreasing(data_size)
            constant_data = generate.constant(data_size)
            v_shape_data = generate.v_shape(data_size)

            # 3 heap sort
            start_time = time.process_time()
            algorithms.heap_sort(random_data)
            exec_time["heap"]["random"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.heap_sort(increasing_data)
            exec_time["heap"]["increasing"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.heap_sort(decreasing_data)
            exec_time["heap"]["decreasing"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.heap_sort(constant_data)
            exec_time["heap"]["constant"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.heap_sort(v_shape_data)
            exec_time["heap"]["v_shape"][point] += (time.process_time() - start_time) / iterations

            # 4 merge sort
            start_time = time.process_time()
            algorithms.merge_sort(random_data)
            exec_time["merge"]["random"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.merge_sort(increasing_data)
            exec_time["merge"]["increasing"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.merge_sort(decreasing_data)
            exec_time["merge"]["decreasing"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.merge_sort(constant_data)
            exec_time["merge"]["constant"][point] += (time.process_time() - start_time) / iterations

            start_time = time.process_time()
            algorithms.merge_sort(v_shape_data)
            exec_time["merge"]["v_shape"][point] += (time.process_time() - start_time) / iterations

            # Increase data size
        data_size += data_step
    return exec_time


def algorithms_compare_plot(dictionary_data, data_type, initial=1000, step=100, mp=15, log_scale=False):
    if data_type not in ["random", "increasing", "decreasing", "constant", "v_shape"]:
        print("Wrong algorithm name")
        return 0

    data_x = [initial + x * step for x in range(mp)]
    X_ = data_x

    for key, value in dictionary_data.items():
        dt = dictionary_data[key][data_type]

        # Smooth values
        Y_ = gaussian_filter1d(dt, sigma=2)

        if log_scale:
            plt.yscale("log")
        plt.plot(X_, Y_, label=key, color=colors[key])

    plt.xlabel("Data size")
    plt.ylabel("Time")
    plt.title("comparison: " + data_type + " values")
    plt.legend()

    plt.show()


def data_types_compare_plot(dictionary_data, algorithm_name, initial=1000, step=100, mp=15, log_scale=False):
    if algorithm_name not in ["insertion", "selection", "heap", "merge"]:
        print("Wrong algorithm name")
        return 0

    data_x = [initial + x * step for x in range(mp)]
    dt = dictionary_data[algorithm_name]

    for key, value in dt.items():
        # Smooth values
        Y_ = gaussian_filter1d(value, sigma=2)

        if log_scale:
            plt.yscale("log")
        plt.plot(data_x, Y_, label=key, color=colors[key])

    plt.xlabel("Data size")
    plt.ylabel("Time")
    plt.title(algorithm_name + " sort")
    plt.legend()

    plt.show()


def quicksort_measure(initial_data, data_step, measure_points, iterations=1):
    exec_time = dict()
    exec_time["middle"] = [0 for _ in range(measure_points)]
    exec_time["extreme"] = [0 for _ in range(measure_points)]
    exec_time["random"] = [0 for _ in range(measure_points)]

    data_size = initial_data

    for point in range(measure_points):
        for _ in range(iterations):
            # Generate data
            a_shape_data = generate.a_shape(data_size)

            # Measure time for each pivot

            # Middle
            start_time = time.process_time()
            algorithms.quick_sort(a_shape_data)
            exec_time["middle"][point] += (time.process_time() - start_time) / iterations

            # Random
            start_time = time.process_time()
            algorithms.quick_sort_random(a_shape_data)
            exec_time["random"][point] += (time.process_time() - start_time) / iterations

            # Extreme
            start_time = time.process_time()
            algorithms.quick_sort_extreme(a_shape_data)
            exec_time["extreme"][point] += (time.process_time() - start_time) / iterations

        # Increase data size
        data_size += data_step
    return exec_time


def quicksort_compare_plot(dictionary_data, initial=1000, step=100, mp=15, log_scale=False):
    data_x = [initial + x * step for x in range(mp)]

    for key, value in dictionary_data.items():
        # Smooth values
        Y_ = gaussian_filter1d(value, sigma=2)

        if log_scale:
            plt.yscale("log")
        plt.plot(data_x, Y_, label=key, color=colors[key])

    plt.xlabel("Data size")
    plt.ylabel("Time")
    plt.title("comparison: pivot location")
    plt.legend()

    plt.show()


# saveData(measure(INITIAL, STEP, MEASURE_POINTS, 5), "data_new.json")
# saveData(measure_heap_merge(INITIAL, STEP, MEASURE_POINTS, 5), "data_hm.json")

# data = getData("data_new.json")

# algorithms_compare_plot(data, "v_shape", INITIAL, STEP, MEASURE_POINTS)
# data_types_compare_plot(data, "merge", INITIAL, STEP, MEASURE_POINTS)

# saveData(quicksort_measure(INITIAL, STEP, MEASURE_POINTS), "data_quicksort.json")

# data_quicksort = getData("data_quicksort.json")

# quicksort_compare_plot(data_quicksort)

print(generate.v_shape(20))
