#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <string>
#include <fstream>

using namespace std;

int nr = 0, CH = 0, found = 0;
double timeUsed;
clock_t timeStart, timeEnd;


void nullify(int **AM, int n);
void dfs(int n, int v, bool* visited, int **AM);
int Check_deg(int **AM, int n, int x);

class Graph {
    public:
        int **matrix;
        int vertices;
        int edges;

        void print();
        void generate(float);
        void fromFile(string);

    Graph(int size) {
        this->vertices = size;
        this->edges = 0;

        this->matrix = (int**) malloc(size * size * sizeof(int));
        for(int i = 0; i < size; i++) {
            this->matrix[i] = new int[size];
            for(int j = 0; j < size; j++) {
                this->matrix[i][j] = 0;
            }
        }
    }
    ~Graph() {
        for(int i = 0; i < this->vertices; i++)
        {
            delete[] this->matrix[i];
        }
        delete[] this->matrix;
    }
};

void Graph::print() {
    for(int i = 0; i < this->vertices; i++) {
        for(int j = 0; j < this->vertices; j++) {
            cout << this->matrix[i][j] << " ";
        }
        cout << endl;
    }
}

void Graph::generate(float min_density) { //Yes, I know, it sucks
    int max_edges = this->vertices * (this->vertices - 1) / 2;
    float current_density = (float) this->vertices / max_edges;
    int* degrees = (int*) malloc(this->vertices * sizeof(int));
    int max_degree = this->vertices - 1 - ((this->vertices - 1) % 2) - 2;
    int expandable = true;

    degrees[0] = 2; // Count degree of each vertex

    // Start with Hamilton cycle
    for(int i = 0; i < this->vertices - 1; i++) {
        this->matrix[i][i + 1] = 1;
        this->matrix[i + 1][i] = 1;
        degrees[i + 1] = 2;
    }

    // Create connection between first and last vertex
    this->matrix[0][this->vertices - 1] = 1;
    this->matrix[this->vertices - 1][0] = 1;

    // Create array of vertices to connect
    int cv[3]; 

    srand (time(NULL));

    while(current_density < min_density && expandable) {
        // Check if you can pick 1st vertex
        expandable = false;
        for(int x = 0; x < this->vertices; x++) {
            if(degrees[x] <= max_degree) {
                expandable = true;
                break;
            }
        }

        if(expandable) {
            // Pick vertex 1
            do {
                cv[0] = rand() % this->vertices;
            } while (degrees[cv[0]] > max_degree);

            // Check if you can pick 2nd vertex
            expandable = false;
            for(int x = 0; x < this -> vertices; x++) {
                if(degrees[x] <= max_degree && x != cv[0] && this->matrix[cv[0]][x] == 0) {
                    expandable = true;
                    break;
                }
            }
            //cout << cv[0] << " ";

            if(expandable) {
                // Pick vertex 2
                do {
                    cv[1] = rand() % this->vertices;
                } while (degrees[cv[1]] > max_degree || cv[1] == cv[0] || this->matrix[cv[0]][cv[1]] == 1);

                //cout << cv[1] << " ";

                // Search if there is vertex 3, that can be connected to vertices 1 and 2. If so, create the connection
                expandable = false;
                for(int x = 0; x < this->vertices; x++) {
                    if(degrees[x] <= max_degree && x != cv[0] && x != cv[1] && this->matrix[cv[0]][x] == 0 && this->matrix[cv[1]][x] == 0) {
                        cv[2] = x;
                        expandable = true;
                        break;
                    }
                }
                /*if(expandable) cout << cv[2] << endl;
                else cout << endl;*/
            }

            if(expandable) {
                //cout << current_density << endl;

                // Connect vertices if all 3 were found
                for(auto i : cv) {
                    // Increase degrees of chosen vertices
                    degrees[i] += 2;
                    for(auto j : cv) {
                        if(i == j) continue;
                        this->matrix[i][j] = 1;
                    }
                }

                // Increate density
                current_density += 3.0 / max_edges;
            }
        }
    }
    free(degrees);
}

// Input is matrix in text file
void Graph::fromFile(string file) {
    ifstream in;
    string line;
    int lin_ind, counter = 0;

    in.open(file);

    while(!in.eof()) {
        getline(in, line);
        for(int x = 0; x < this->vertices; x++) {
            lin_ind = line[x * 2] - '0';
            matrix[counter][x] = lin_ind;
        }
        counter++;
    }
}

// Create Adjacency matrix
void create_AM(int **AM, int n, int m) {
    int x, y, h, i, all_visited;
    bool *visit = new bool[n];

    i = m;
    while(i) {
        y = rand()%n;
        x = rand()%n;
        if(AM[x][y] != 1 && x != y) {
            AM[x][y] = AM[y][x] = 1;
            i--;
        }
    }

    for(x = 0; x < n - 1; x++) {
        h = Check_deg(AM, n, x);
        if (h%2) {
            y = rand()%(n - x - 1) + x + 1;
            if (AM[x][y]) {
                AM[x][y] = 0;
                AM[y][x] = 0;
                i--;
            }
            else {
                AM[x][y] = 1;
                AM[y][x] = 1;
                i++;
            }
        }
    }

    all_visited = 1;

    dfs(n, 0, visit, AM);

    for(x=0; x < n - 1; x++) {
        if (!visit[x]) {
            all_visited = 0;
            break;
        }
    }
    if (all_visited == 0) {
        nullify(AM, n);
        create_AM(AM, n, m);
    }
}

// Check degree
int Check_deg(int **AM, int n, int x) {

    int j = 0;
    for (int i = 0; i < n; i++) {
        if (AM[x][i] == 1)
            j++;
    }

    return j;
}

// Dfs
void dfs(int n, int v, bool* visited, int **AM) {

    visited[v] = 1;
    for (int x = 0; x < n; x++) {
        if (AM[v][x] && !visited[x]) {
            dfs(n, x, visited, AM);
        }
    }
}

// Erase connection in a graph
void nullify(int **AM, int n) {

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)  {
            AM[i][j] = 0;
        }
    }
}


// Copy Graph
void copy(int **AM, int **AM_cp, int n) {

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)  {
            AM_cp[i][j] = AM[i][j];
        }
    }
}

// Find Euler cycle
void Euler(int** AM, int n, int v) {

    for (int x = 0; x < n; x++) {
        if (AM[v][x]) {
            AM[v][x] = 0;
            AM[x][v] = 0;
            Euler(AM, n, x);
        }
    }
}

// Find Hamilton cycle
int Hamilton(int n, int v, int* path, bool* visited, int** AM) {

    path[nr++] = v;
    if (nr != n) {
        visited[v] = 1;
        for (int x = 0; x < n; x++)
            if (AM[v][x] && !visited[x])
                Hamilton(n, x, path, visited, AM);
        visited[v] = 0;
    }
    else if (AM[v][0]) {
        if (!found) {
            timeEnd = clock();
            timeUsed = (double)(timeEnd-timeStart)/CLOCKS_PER_SEC;
            printf("Hamilton: %.3f\n", timeUsed * 1000);
            found = 1;
        }
        CH++;
    }
    nr--;

    return CH/2;
}



int main() {
    int n, m, i, x;
    float nasycenie;
    srand(time(0));
    printf("n: ");
    scanf("%d", &n);
    printf("nasycenie (0.0 - 1.0): ");
    scanf("%f", &nasycenie);
    m = 0.5 * nasycenie * n * (n-1);

    /*int **AM = (int**) malloc (n * sizeof(int*));
    for (i = 0; i < n; i++)
        AM[i] = (int*) malloc (n * sizeof(int*));*/

    int **AM_cp = (int**) malloc (n * sizeof(int*));
    for (i = 0; i < n; i++)
        AM_cp[i] = (int*) malloc (n * sizeof(int*));

    bool *visited = new bool[n];
    int *path = new int[n];

    //create_AM(AM, n, m);
    Graph* g1 = new Graph(n);
    g1->generate(nasycenie);
    copy(g1->matrix, AM_cp, n);
    timeStart = clock();
    Euler(AM_cp, n, 0);
    timeEnd = clock();
    timeUsed = (double)(timeEnd-timeStart)/CLOCKS_PER_SEC;


    printf("Euler: %.3f\n", timeUsed * 1000);
    timeStart = clock();
    printf("Liczba wszystkich cykli Hamiltona: %d\n", Hamilton(n, 0, path, visited, g1->matrix));
    timeEnd = clock();
    timeUsed = (double)(timeEnd-timeStart)/CLOCKS_PER_SEC;
    printf("wszystki cykli Hamiltona: %.3f\n", timeUsed * 1000);

    return 0;
}