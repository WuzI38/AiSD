#include <stdio.h>
#include <iostream>
#include <fstream>
#include <chrono>
#include <string>
#include "list.cpp"
#include "tree.cpp"

#include <thread>

#define ARRSIZE 20

using namespace std;
using namespace chrono;
using namespace std::this_thread;

void shuffle(int* arr, size_t n)
{
    if (n > 1)
    {
        size_t i;
        srand(time(NULL));
        for (i = 0; i < n - 1; i++)
        {
            size_t j = i + rand() / (RAND_MAX / (n - i) + 1);
            int t = arr[j];
            arr[j] = arr[i];
            arr[i] = t;
        }
    }
}

int main() {
    auto start = steady_clock::now();
    sleep_for(seconds(3));
    auto end = steady_clock::now();
    int seconds = duration_cast<chrono::seconds>(end - start).count();

    string json = "{\"time\": [" + to_string(seconds) + "]}";
    
    ofstream file("data.json");
    if(file.is_open()) {
        file << json;
        file.close();
    }
    else cout << "Unable to open file\n";
    return 0;
}