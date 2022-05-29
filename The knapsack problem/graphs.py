from matplotlib import pyplot as plt
from scipy.ndimage import gaussian_filter1d
from main import INIT_SIZE, STEP_SIZE, MEASURE_POINTS, STEP_ITEMS, INIT_ITEMS


# nothing really revelatory here, just graphs
def size_compare_plot(data_dp, data_greed, log_scale=False):
    data_x = [INIT_SIZE + x * STEP_SIZE for x in range(MEASURE_POINTS)]

    # Smooth values
    y1 = gaussian_filter1d(data_dp, sigma=2)
    y2 = gaussian_filter1d(data_greed, sigma=2)

    plt.plot(data_x, y1, label="Dynamic algorithm", color="red")
    plt.plot(data_x, y2, label="Greedy algorithm", color="green")

    if log_scale:
        plt.yscale("log")
    plt.xlabel("Backpack size")
    plt.ylabel("Time")
    plt.title("Comparison: backpack size not const")
    plt.legend()

    plt.show()


def items_compare_plot(data_dp, data_greed, log_scale=False):
    data_x = [INIT_ITEMS + x * STEP_ITEMS for x in range(MEASURE_POINTS)]

    # Smooth values
    y1 = gaussian_filter1d(data_dp, sigma=2)
    y2 = gaussian_filter1d(data_greed, sigma=2)

    plt.plot(data_x, y1, label="Dynamic algorithm", color="red")
    plt.plot(data_x, y2, label="Greedy algorithm", color="green")

    if log_scale:
        plt.yscale("log")
    plt.xlabel("Item list size")
    plt.ylabel("Time")
    plt.title("Comparison: item list size not const")
    plt.legend()

    plt.show()


def error_compare_plot(data_error_size, data_error_item, log_scale=False):
    data_x = [x + 1 for x in range(MEASURE_POINTS)]

    # Smooth values
    y1 = gaussian_filter1d(data_error_size, sigma=2)
    y2 = gaussian_filter1d(data_error_item, sigma=2)

    plt.plot(data_x, y1, label="Backpack error", color="red")
    plt.plot(data_x, y2, label="Item list error", color="green")

    if log_scale:
        plt.yscale("log")
    plt.xlabel("Measure point id")
    plt.ylabel("Error size")
    plt.title("Comparison: error size")
    plt.legend()

    plt.show()
