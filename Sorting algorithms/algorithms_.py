import copy
import random


class Algorithm:
    @staticmethod
    def __insertion_sort(tab):
        for j in range(1, len(tab)):
            key = tab[j]
            i = j - 1
            while i >= 0 and tab[i] > key:
                tab[i + 1] = tab[i]
                i -= 1
            tab[i + 1] = key
        return tab

    @staticmethod
    def insertion_sort(a):
        c = copy.deepcopy(a)
        Algorithm.__insertion_sort(c)
        return c

    @staticmethod
    def __swap(a, i, j):
        a[i], a[j] = a[j], a[i]

    @staticmethod
    def __selection_sort(tab):
        j = len(tab) - 1
        while j >= 1:
            maximum = j
            i = j - 1
            while i >= 0:
                if tab[i] > tab[maximum]:
                    maximum = i
                i -= 1
            tab[j], tab[maximum] = tab[maximum], tab[j]
            j -= 1
        return tab

    @staticmethod
    def selection_sort(a):
        c = copy.deepcopy(a)
        Algorithm.__selection_sort(c)
        return c

    @staticmethod
    def __heap_sort(a):
        n = len(a)
        for i in range((n // 2 - 1), -1, -1):
            Algorithm.__heapify(a, n, i)

        for i in range(n - 1, 0, -1):
            a[i], a[0] = a[0], a[i]
            Algorithm.__heapify(a, i, 0)

    @staticmethod
    def __heapify(a, n, heapsize):
        largest = heapsize
        l = 2 * heapsize
        r = 2 * heapsize + 1

        if l < n and a[l] > a[largest]:
            largest = l

        if r < n and a[r] > a[largest]:
            largest = r

        if largest != heapsize:
            a[largest], a[heapsize] = a[heapsize], a[largest]
            Algorithm.__heapify(a, n, largest)

    @staticmethod
    def heap_sort(a):
        c = copy.deepcopy(a)
        Algorithm.__heap_sort(c)
        return c

    @staticmethod
    def __merge_sort_build(x, y):
        c = []
        i = j = 0
        while i < len(x) and j < len(y):
            if x[i] < y[j]:
                c.append(x[i])
                i = i + 1
            else:
                c.append(y[j])
                j = j + 1
        if i < len(x):
            c = c + x[i:]
        if j < len(y):
            c = c + y[j:]
        return c

    @staticmethod
    def __merge_sort(a):
        if len(a) == 1:
            return a
        mid = len(a) // 2
        l = Algorithm.__merge_sort(a[:mid])
        r = Algorithm.__merge_sort(a[mid:])
        return Algorithm.__merge_sort_build(l, r)

    @staticmethod
    def merge_sort(a):
        c = copy.deepcopy(a)
        return Algorithm.__merge_sort(c)

    @staticmethod
    def __quick_sort(a, tp):
        def quick_sort_build(x, y, z):
            if y < z:
                index = Algorithm.__partition(x, y, z, tp)
                quick_sort_build(x, y, index)
                quick_sort_build(x, index + 1, z)
        quick_sort_build(a, 0, len(a) - 1)

    @staticmethod
    def __partition(a, y, z, tp):
        if tp == 'e':
            Algorithm.__swap(a, (y + z) // 2, z)
        if tp == 'r':
            i = random.randrange(y, z)
            Algorithm.__swap(a, (y + z) // 2, i)
        p = a[(y + z) // 2]
        i = y - 1
        j = z + 1
        while True:
            i = i + 1
            while a[i] < p:
                i = i + 1

            j = j - 1
            while a[j] > p:
                j = j - 1

            if i >= j:
                return j
            a[i], a[j] = a[j], a[i]

    @staticmethod
    def quick_sort_extreme(a):
        c = copy.deepcopy(a)
        Algorithm.__quick_sort(c, 'e')
        return c

    @staticmethod
    def quick_sort_random(a):
        c = copy.deepcopy(a)
        Algorithm.__quick_sort(c, 'r')
        return c

    @staticmethod
    def quick_sort(a):
        c = copy.deepcopy(a)
        Algorithm.__quick_sort(c, 'm')
        return c


class Generator:
    @staticmethod
    def increasing(n):
        return [i for i in range(1, n + 1)]

    @staticmethod
    def decreasing(n):
        return Generator.increasing(n)[::-1]

    @staticmethod
    def v_shape(n):
        return [i for i in range(n, 0, -2)] + [j for j in range(abs((n + 1) % 2 - 2), n, 2)]

    @staticmethod
    def constant(n):
        return [1 for _ in range(1, n + 1)]

    @staticmethod
    def rand(n):
        return [random.randint(1, n) for _ in range(1, n + 1)]

    @staticmethod
    def a_shape(n):
        return [j for j in range(abs((n + 1) % 2 - 2), n, 2)] + [i for i in range(n, 0, -2)]
