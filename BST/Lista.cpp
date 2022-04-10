#include <iostream>

using namespace std;

struct Node {
    string val;
    Node* next;

    Node(string _val) : val(_val), next(nullptr) {}
};

struct list {
    Node* first;
    Node* last;

    list() : first(nullptr), last(nullptr) {}

    bool pusty() {  /**Funkcja sprawdzania, czy węzły znajdują się na liście**/
        return first == nullptr;
    }

    void insert(string _val) { /**Funkcja dodawania elementu na końcu listy**/
        Node* p = new Node(_val);
        if (pusty()) {
            first = p;
            last = p;
            return;
        }
        last->next = p;
        last = p;
    }

    void print() { /**Funkcja napisania pełnej listy**/
        if (pusty()) return;
        Node* p = first;
        while (p) {
            cout << p->val << " ";
            p = p->next;
        }
        cout << endl;
    }
  
      void delete_first() { /**Funkcja usuwania pierwszego węzła**/
        if (pusty()) return;
        Node* p = first;
        first = p->next;
        delete p;
    }
  
      Node* operator[] (const int index) { /**Funkcja wyszukiwania na liście po podanej wartości**/
        if (pusty()) return nullptr;
        Node* p = first;
        for (int i = 0; i < index; i++) {
            p = p->next;
            if (!p) return nullptr;
        }
        return p;
    }
};

int main()
{
    list l;
    cout << l.pusty() << endl;
    l.insert("3");
    l.insert("123");
    l.insert("8");
    l.print();
    cout << l.pusty() << endl;
 //   l.delet_e("123");
    l.print();
    l.insert("1234");
    l.delete_first();
    l.print();
//    l.remove_last();
    l.print();
    cout << l[1]->val << endl;
    return 0;
}
