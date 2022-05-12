from random import random
import matplotlib.pyplot as plt
import networkx as nx
from time import perf_counter
import sys
from scipy.ndimage import gaussian_filter

# constants

DENSITY = [0.3, 0.6, 0.7]
REPEAT = 1
STEP = 20
SIZE_MAX = 300
SIZE_MAX_2 = 300
STEP_2 = 20
sys.setrecursionlimit(3000)


def generatetask2(size):
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(i + 1, size):
            if i - j == 1:
                matrix[i][j] = round(random() * 1000) + 1
                matrix[j][i] = matrix[i][j]
            elif random() < DENSITY[0]:
                matrix[i][j] = round(random() * 1000)
                matrix[j][i] = matrix[i][j]
    for i in range(size):
        if sum(matrix[i]) == 0:
            index = round(random() * size)
            while index == i:
                index = round(random() * size)
            matrix[i][index] = round(random() * 1000) + 1
            matrix[index][i] = matrix[i][index]
    for i in range(size):
        for j in range(i + 1, size):
            if matrix[i][j] != 0:
                matrix[j][i] = matrix[i][j]
    return matrix


def generatelisttask2(matrix):
    ilist = []
    for ind, val in enumerate(matrix):
        ilist.append([])
        for index, value in enumerate(val):
            if value != 0:
                ilist[ind].append((index, value))
    return ilist


def generateDAG(SIZE):
    matrix = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    for i in range(SIZE):
        for j in range(i + 1, SIZE):
            if random() < DENSITY[1]:
                matrix[i][j] = 1
    return matrix


def generateIncList(matrix):
    ilist = []
    for ind, val in enumerate(matrix):
        ilist.append([])
        for index, value in enumerate(val):
            if value == 1:
                ilist[ind].append(index)
    return ilist


def drawweight(graph, size):
    G = nx.Graph()
    for i in range(size):
        G.add_node(i, pos=(i, round(random() * size * 10)))
    for i in range(size):
        for j in range(i + 1, size):
            if graph[i][j] != 0:
                G.add_edge(i, j, weight=graph[i][j])
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


def draw(graph, SIZE):
    g = nx.DiGraph()
    g.add_nodes_from(range(1, SIZE))
    for i in range(SIZE):
        for j in range(SIZE):
            if graph[i][j] == 1:
                g.add_edge(i + 1, j + 1)
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(g, k=0.8)
    nx.draw(g, pos, with_labels=True, width=0.4, node_color='lightblue', node_size=400)
    plt.show(block=True)


def topological_sort_matrix(matrix, SIZE):
    vertices = []
    visited = set()

    def rekt(v=0):
        visited.add(v)
        for i in range(SIZE):
            if matrix[v][i] == 1 and i not in visited:
                rekt(i)
        vertices.append(v + 1)

    for i in range(SIZE):
        if i not in visited:
            rekt(i)
    vertices.reverse()
    return vertices


def topological_sort_list(lst, SIZE):
    vertices = []
    visited = set()

    def traverse(v=0):
        visited.add(v)
        for i in lst[v]:
            if i not in visited:
                traverse(i)
        if (v + 1) not in vertices:
            vertices.append(v + 1)

    for j in range(SIZE):
        if j not in visited:
            traverse(j)

    traverse()
    vertices.reverse()
    return vertices


def prim(matrix, size):
    selected_node = [0 for _ in range(size)]
    no_edge = 0
    selected_node[0] = True
    # printing for edge and weight
    res = []
    while no_edge < size - 1:

        minimum = 1001
        a = 0
        b = 0
        for m in range(size):
            if selected_node[m]:
                for n in range(m, size):
                    if ((not selected_node[n]) and matrix[m][n]):
                        # not in selected and there is an edge
                        if minimum > matrix[m][n]:
                            minimum = matrix[m][n]
                            a = m
                            b = n
        res.append([a, b, matrix[a][b]])
        selected_node[b] = True
        no_edge += 1
    return res


def primaList(lst):
    edges = []
    edges_visited = []
    vertices = set()
    vertices.add(0)
    for index, line in enumerate(lst):
        for item in line:
            edges.append([index, item[0], item[1]])
    while len(vertices) < len(lst):
        mn = 1001
        mn_ind = -1
        for index, e in enumerate(edges):
            if e[2] < mn and e[0] in vertices and e[1] not in vertices:
                mn = e[2]
                mn_ind = index
        vertices.add(edges[mn_ind][1])
        edges_visited.append(edges[mn_ind])
    return edges_visited


def task1():
    time_for_matrix = 0
    time_for_list = 0
    size = STEP
    n = []
    ilistlist = []
    matrixlist = []
    while size <= SIZE_MAX:

        for _ in range(REPEAT):
            graphmatrix = generateDAG(size)
            graphlist = generateIncList(graphmatrix)
            start = perf_counter()
            topological_sort_matrix(graphmatrix, size)
            time_for_matrix += (perf_counter() - start)
            start = perf_counter()
            topological_sort_list(graphlist, size)
            time_for_list += (perf_counter() - start)
        n.append(size)
        ilistlist.append(time_for_list / REPEAT)
        matrixlist.append(time_for_matrix / REPEAT)
        size += STEP
        time_for_list = 0
        time_for_matrix = 0
    plt.gca()
    plt.title("Topological Sort")
    plt.xlabel("Elements")
    plt.ylabel("Time")
    plt.plot(n, gaussian_filter(ilistlist, sigma=2), label="list", color="cyan")
    plt.plot(n, gaussian_filter(matrixlist, sigma=2), label="matrix", color="green")
    plt.legend(loc="lower right")
    plt.show()


def task2():
    size = STEP_2
    n = []
    ilistlist = []
    matrixlist = []
    time_for_matrix = 0
    time_for_list = 0
    while size <= SIZE_MAX_2:
        for _ in range(REPEAT):
            graphmatrix = generatetask2(size)
            graphlist = generatelisttask2(graphmatrix)
            start = perf_counter()
            primaList(graphlist)
            time_for_list += perf_counter() - start
            start1 = perf_counter()
            prim(graphmatrix, size)
            time_for_matrix += perf_counter() - start1
        n.append(size)
        ilistlist.append(time_for_list / REPEAT)
        matrixlist.append(time_for_matrix / REPEAT)
        size += STEP_2
        time_for_list = 0
        time_for_matrix = 0
    plt.gca()
    plt.title("Minimum Spanning Tree 30%")
    plt.xlabel("Elements")
    plt.ylabel("Time")
    plt.plot(n, gaussian_filter(ilistlist, sigma=2), label='list', color="cyan")
    plt.plot(n, gaussian_filter(matrixlist, sigma=2), label='matrix', color="green")
    plt.legend(loc='lower right')
    plt.show()


def main():
    # task1()
    task2()


if __name__ == "__main__":
    main()