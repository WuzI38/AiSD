#include <stdio.h>
#include <iostream>
#include <fstream>
#include <chrono>
#include <string>
#include "list.cpp"
#include "tree.cpp"

#define MEASURE_POINTS 30
#define INITIAL 100
#define STEP 300
#define ARRSIZE (INITIAL + (MEASURE_POINTS - 1) * STEP)

using namespace std;
using namespace chrono;

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

void vecToAVL(vector<int> tab, vector <int> *tab_avl) {
    tab_avl->push_back(tab[(tab.size() - 1) / 2]);
    if (tab.size() == 2)
        tab_avl->push_back(tab[(tab.size() - 1) / 2 + 1]);
    if (tab.size() > 2)
    {
        vecToAVL(vector<int>(tab.begin(), tab.begin() + (tab.size() - 1) / 2), tab_avl);
        vecToAVL(vector<int>(tab.begin() + (tab.size() - 1) / 2 + 1, tab.end()), tab_avl);
    }
}

int main() {
    Linkedlist list;
    BST tree;
    BST treeAVL;

    int list_creation_time[MEASURE_POINTS];
    int tree_creation_time[MEASURE_POINTS];
    int list_search_time[MEASURE_POINTS];
    int tree_search_time[MEASURE_POINTS];
    int list_deletion_time[MEASURE_POINTS];
    int tree_deletion_time[MEASURE_POINTS];

    int tree_height[MEASURE_POINTS];
    int treeAVL_height[MEASURE_POINTS];

    int numbers[ARRSIZE];

    for(int x = 0; x < ARRSIZE; x++) //Generate awfuly long array (or chicken, whatever)
        numbers[x] = x;

    shuffle(numbers, ARRSIZE);
    
    auto start = steady_clock::now();
    auto end = steady_clock::now();
    int time;

    vector <int> nums;
    vector <int> numsAVL;

    // Generate time data
    for(int x = 0; x < MEASURE_POINTS; x++) {
        // List Creation Time
        start = steady_clock::now();
        for(int y = 0; y < INITIAL + x * STEP; y++) {
            list.insertNode(numbers[y]);
        }
        end = steady_clock::now();

        time = duration_cast<chrono::microseconds>(end - start).count();
        list_creation_time[x] = time;

        // Tree Creation Time
        start = steady_clock::now();
        for(int y = 0; y < INITIAL + x * STEP; y++) {
            tree.insertNode(numbers[y]);
        }
        end = steady_clock::now();
        
        time = duration_cast<chrono::microseconds>(end - start).count();
        tree_creation_time[x] = time;

        // List Search Time
        start = steady_clock::now();
        for(int y = 0; y < INITIAL + x * STEP; y++) {
            list.search(numbers[y]);
        }
        end = steady_clock::now();
        
        time = duration_cast<chrono::microseconds>(end - start).count();
        list_search_time[x] = time;

        // Tree Search Time
        start = steady_clock::now();
        for(int y = 0; y < INITIAL + x * STEP; y++) {
            tree.search(numbers[y]);
        }
        end = steady_clock::now();
        
        time = duration_cast<chrono::microseconds>(end - start).count();
        tree_search_time[x] = time;

        // Tree height 
        tree_height[x] = tree.getHeight(tree.getHead());

        // List Deletion Time
        start = steady_clock::now();
        list.deleteList();
        end = steady_clock::now();

        time = duration_cast<chrono::microseconds>(end - start).count();
        list_deletion_time[x] = time;

        // Tree Deletion Time
        start = steady_clock::now();
        tree.deleteTree(tree.getHead());
        end = steady_clock::now();
        
        time = duration_cast<chrono::microseconds>(end - start).count();
        tree_deletion_time[x] = time;
    }

    // Generate AVL tree

    for(int x = 0; x < MEASURE_POINTS; x++) {
        nums.clear();
        numsAVL.clear();

        for(int y = 0; y < INITIAL + x * STEP; y++) {
            nums.push_back(y);
        }
        
        vecToAVL(nums, &numsAVL);

        for(int y = 0; y < INITIAL + x * STEP; y++) {
            treeAVL.insertNode(numsAVL[y]);
        }

        treeAVL_height[x] = treeAVL.getHeight(treeAVL.getHead());

        treeAVL.deleteTree(treeAVL.getHead());
    }
        

    //Save to json

    string json = "{\"list\": {\"creation\": [";

    for(int x = 0; x < MEASURE_POINTS; x++) {
        json += to_string(list_creation_time[x]);
        if(x != MEASURE_POINTS - 1)
            json += ", ";
    }

    json += "], \"search\": [";

    for(int x = 0; x < MEASURE_POINTS; x++) {
        json += to_string(list_search_time[x]);
        if(x != MEASURE_POINTS - 1)
            json += ", ";
    }

    json += "], \"deletion\": [";

    for(int x = 0; x < MEASURE_POINTS; x++) {
        json += to_string(list_deletion_time[x]);
        if(x != MEASURE_POINTS - 1)
            json += ", ";
    }

    json += "]}, \"tree\": {\"creation\": [";

    for(int x = 0; x < MEASURE_POINTS; x++) {
        json += to_string(tree_creation_time[x]);
        if(x != MEASURE_POINTS - 1)
            json += ", ";
    }

    json += "], \"search\": [";

    for(int x = 0; x < MEASURE_POINTS; x++) {
        json += to_string(tree_search_time[x]);
        if(x != MEASURE_POINTS - 1)
            json += ", ";
    }

    json += "], \"deletion\": [";

    for(int x = 0; x < MEASURE_POINTS; x++) {
        json += to_string(tree_deletion_time[x]);
        if(x != MEASURE_POINTS - 1)
            json += ", ";
    }

    json += "]}}";

    string json2 = "{\"tree\": [";

    for(int x = 0; x < MEASURE_POINTS; x++) {
        json2 += to_string(tree_height[x]);
        if(x != MEASURE_POINTS - 1)
            json2 += ", ";
    }

    json2 += "], \"tree_AVL\": [";

    for(int x = 0; x < MEASURE_POINTS; x++) {
        json2 += to_string(treeAVL_height[x]);
        if(x != MEASURE_POINTS - 1)
            json2 += ", ";
    }

    json2 += "]}";

    ofstream file("data.json");
    if(file.is_open()) {
        file << json;
        file.close();
    }

    ofstream file2("dataAVL.json");
    if(file2.is_open()) {
        file2 << json2;
        file2.close();
    }

    return 0;
}