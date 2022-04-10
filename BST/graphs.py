import json
from matplotlib import pyplot as plt
from scipy.ndimage import gaussian_filter1d

INITIAL = 100
MEASURE_POINTS = 30
STEP = 300

colors = {
    "list": 'b',
    "tree_AVL": 'y',
    "tree": 'r'
}


def getData(file):  # json file -> data
    with open(file) as json_file:
        d = json.load(json_file)
        return d


def structuresComparePlot(dictionary_data, data_type, initial=1000, step=300, mp=30, log_scale=False):
    if data_type not in ["creation", "search", "deletion"]:
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
    plt.ylabel("Time (microseconds)")
    plt.title("BST vs List: " + data_type + " time")
    plt.legend()

    plt.show()


def addLabels(x, y, offset):
    for i in range(len(x)):
        plt.text(INITIAL + i * STEP + offset / 2, y[i] + 0.5, y[i], ha='center', fontweight="bold")


def heightComparePlot(dictionary_data, initial=1000, step=300, mp=30, labels=False):
    data_x = [initial + x * step for x in range(mp)]

    for key, value in dictionary_data.items():
        plt.bar(data_x, value, label=key, color=colors[key], width=mp * 3, align="edge")
        if labels:
            addLabels(data_x, value, mp * 3)
        mp = -mp

    plt.xlabel("Data size")
    plt.ylabel("Height")
    plt.title("BST vs AVL: height")
    plt.legend()

    plt.show()


data = getData("data.json")
dataAVL = getData("dataAVL.json")

# structuresComparePlot(data, "deletion", INITIAL, STEP, MEASURE_POINTS, True)
# heightComparePlot(dataAVL, INITIAL, STEP, MEASURE_POINTS, False)
