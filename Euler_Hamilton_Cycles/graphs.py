from matplotlib import pyplot as plt

data30 = {}
data70 = {}
data_hamilton = {}

colors = {
    "Euler": 'b',
    "Hamilton": 'g',
    "Cycles": 'r',
}

for x in ["Vertices", "Euler", "Hamilton"]:
    data30[x] = []
    data70[x] = []

data_hamilton["Vertices"] = []
data_hamilton["Cycles"] = []

with open("g30.txt") as file:
    for line in file:
        text = line.rstrip().split()
        if text[0] == 'n':
            continue
        data30["Vertices"].append(int(text[0]))
        data30["Euler"].append(int(text[1]))
        data30["Hamilton"].append(int(text[2]))

file.close()

with open("g70.txt") as file:
    for line in file:
        text = line.rstrip().split()
        if text[0] == 'n':
            continue
        data70["Vertices"].append(int(text[0]))
        data70["Euler"].append(int(text[1]))
        data70["Hamilton"].append(int(text[2]))

file.close()

with open("ham2.txt") as file:
    for line in file:
        text = line.rstrip().split()
        if text[0] == 'n':
            continue
        data_hamilton["Vertices"].append(int(text[0]))
        data_hamilton["Cycles"].append(int(text[1]))

file.close()


def task1_plot(args, density):
    data_x = args["Vertices"]

    for key, value in args.items():
        if key == "Vertices":
            continue

        data_y = value
        plt.scatter(data_x, data_y, label=key, color=colors[key], marker='o')

    plt.yscale("log")
    plt.xlabel("Vertices")
    plt.ylabel("Time")
    plt.title("Density: {}%".format(density))
    plt.xticks(range(5, data_x[-1] - (data_x[-1] % 5) + 6, 5))  # Put x axis ticks every 5 units.
    plt.legend()
    plt.show()


def task2_plot(args):
    data_x = args["Vertices"]
    data_y = args["Cycles"]
    plt.scatter(data_x, data_y, label="HC", color=colors["Cycles"], marker='o')

    plt.yscale("log")
    plt.xlabel("Vertices")
    plt.ylabel("Time")
    plt.title("Finding all Hamiltonian cycles")
    plt.legend()

    plt.show()

task1_plot(data70, 70)
# task2_plot(data_hamilton)
