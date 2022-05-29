# import numpy as np  # cuz performance reasons
import functions as fnc
import graphs as grp
from time import perf_counter
import json

# const values
MEASURE_POINTS = 15
ITERATIONS = 3

# size of possible items list
INIT_ITEMS = 10
STEP_ITEMS = 4

# size of backpack / ship
INIT_SIZE = 20
STEP_SIZE = 10

# max size of backpack and item list
MAX_ITEMS = INIT_ITEMS + STEP_ITEMS * MEASURE_POINTS
MAX_SIZE = INIT_SIZE + STEP_SIZE * MEASURE_POINTS

# max item weight (1 / 3 of max backpack / ship size) and max item value
MAX_WEIGHT = MAX_SIZE // 3
MAX_VALUE = MAX_WEIGHT * 4


# Why is that here? No eye deer
def saveData(dictionary_data, file_name):  # data -> json file
    with open(file_name, "w") as outfile:
        json.dump(dictionary_data, outfile)


# average c++ enjoyer here
def main():
    # generate dataset + initialize dictionary storing measurements
    exec_time = dict()
    error = dict()
    exec_time["greed_size"] = [0 for _ in range(MEASURE_POINTS)]
    exec_time["greed_items"] = [0 for _ in range(MEASURE_POINTS)]
    exec_time["dp_size"] = [0 for _ in range(MEASURE_POINTS)]
    exec_time["dp_items"] = [0 for _ in range(MEASURE_POINTS)]
    error["size"] = [0 for _ in range(MEASURE_POINTS)]
    error["items"] = [0 for _ in range(MEASURE_POINTS)]

    for x in range(ITERATIONS):
        # generate item list
        items = fnc.generate_items(MAX_ITEMS, MAX_WEIGHT, MAX_VALUE)
        # time in microseconds!!!

        # part one: only backpack / ship size changes
        for i in range(MEASURE_POINTS):
            # make measurement for dp algorithm
            start = perf_counter()
            dp_value = fnc.dp(items, INIT_SIZE + i * STEP_SIZE, True)
            end = perf_counter()
            exec_time["dp_size"][i] += round(((end - start) / ITERATIONS) * 1000, 3)

            # make measurement for greedy algorithm
            start = perf_counter()
            greed_value = fnc.greed(items, INIT_SIZE + i * STEP_SIZE)
            end = perf_counter()
            exec_time["greed_size"][i] += round(((end - start) / ITERATIONS) * 1000, 3)

            # calculate error
            error["size"][i] += abs((dp_value - greed_value) / (ITERATIONS * greed_value))

        # part two: only size of item array changes
        for i in range(MEASURE_POINTS):
            # make measurement for dp algorithm
            start = perf_counter()
            dp_value = fnc.dp(items[:, 0:INIT_ITEMS + i * STEP_ITEMS], MAX_ITEMS, True)
            end = perf_counter()
            exec_time["dp_items"][i] += round(((end - start) / ITERATIONS) * 1000, 3)

            # make measurement for greedy algorithm
            start = perf_counter()
            greed_value = fnc.greed(items[:, 0:INIT_ITEMS + i * STEP_ITEMS], MAX_ITEMS)
            end = perf_counter()
            exec_time["greed_items"][i] += round(((end - start) / ITERATIONS) * 1000, 3)

            # calculate error
            error["items"][i] += abs((dp_value - greed_value) / (ITERATIONS * greed_value))

    # some random code like creating graphs goes here

    # save data to json format cause why not (stolen from my past self)

    # saveData(exec_time, "answers.json")
    # saveData(error, "error.json")

    # draw graphs: 1st for increasing number of items, 2nd for increasing backpack size, 3rd for error sizes

    # grp.items_compare_plot(exec_time["dp_items"], exec_time["greed_items"], True)
    # grp.size_compare_plot(exec_time["dp_size"], exec_time["greed_size"], True)
    grp.error_compare_plot(error["size"], error["items"])


if __name__ == "__main__":
    main()

# Everything in this entire universe is either a duck or not a duck
