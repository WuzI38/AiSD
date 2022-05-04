#include <stdio.h>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

int get(const int &n, int *&subtree) {
    if (subtree[n] == n) return n;
    return subtree[n] = get(subtree[n], subtree);
}

void merge(const int &a, const int &b, int *&subtree, int *&vertex_rank) {
    int ra = get(a, subtree), rb = get(b, subtree);
    if (vertex_rank[ra] < vertex_rank[rb]) subtree[ra] = rb;
    else if (vertex_rank[rb] < vertex_rank[ra]) subtree[rb] = ra;
    else {
        subtree[ra] = rb;
        vertex_rank[rb]++;
    }
}

int main()
{
    int vertices, edges;
    scanf("%i%i", &vertices, &edges);
    vector <pair<int, pair<int, int>>> v(edges);
    for (int i = 0; i < edges; ++i) {
        scanf("%i%i%i", &v[i].second.first, &v[i].second.second, &v[i].first);
    }
    sort(v.begin(), v.end());
    int *subtree = new int[vertices];
    int *vertex_rank = new int[vertices];
    for (int i = 0; i < vertices; i++) {
        subtree[i] = i;
        vertex_rank[i] = 1;
    }
    int spanning_tree_weight = 0;
    for (int i = 0; i < edges; ++i) {
        if (get(v[i].second.first - 1, subtree) != get(v[i].second.second - 1, subtree)) {
            spanning_tree_weight += v[i].first;
            merge(v[i].second.first - 1, v[i].second.second - 1, subtree, vertex_rank);
        }
    }
    printf("%i", spanning_tree_weight);
    delete[] subtree;
    delete[] vertex_rank;
    return 0;
}

/*
10-(wierzchołki) 10-(krawędzi)
1-(początek) 3-(koniec) 1-(waga)
1 4 5
1 2 6
2 3 5
2 5 3
3 4 5
3 5 6
3 6 4
6 4 2
6 5 6


odp. tego = 15
 */

