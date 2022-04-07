#include <stdio.h>
#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node()
    {
        data = 0;
        next = NULL;
    }
    Node(int data)
    {
        this->data = data;
        this->next = NULL;
    }
};

class Linkedlist {
    Node* head;

public:
    Linkedlist() { head = NULL; }
    void insertNode(int);
    void printList();
    void deleteNode(int);
    void deleteList();
    void search(int);
};

void Linkedlist::deleteNode(int nodeOffset) {
    Node* temp1 = head, * temp2 = NULL;
    int ListLen = 0;

    if (head == NULL) {
        cout << "List empty." << endl;
        return;
    }
    while (temp1 != NULL) {
        temp1 = temp1->next;
        ListLen++;
    }
    if (ListLen < nodeOffset) {
        cout << "Index out of range"
            << endl;
        return;
    }
    temp1 = head;
    if (nodeOffset == 1) {
        head = head->next;
        delete temp1;
        return;
    }
    while (nodeOffset-- > 1) {
        temp2 = temp1;
        temp1 = temp1->next;
    }
    temp2->next = temp1->next;
    delete temp1;
}

void Linkedlist::insertNode(int data) {
    Node* newNode = new Node(data);
    if (head == NULL) {
        head = newNode;
        return;
    }
    Node* temp = head;
    while (temp->next != NULL && temp->next->data < newNode->data) {
        temp = temp->next;
    }
    if (temp->data == head->data && temp->data > data)
    {
        newNode->next = temp;
        head = newNode;
        return;
    }
    newNode->next = temp->next;
    temp->next = newNode;
}

void Linkedlist::printList() {
    Node* temp = head;
    if (head == NULL) {
        cout << "List empty" << endl;
        return;
    }
    while (temp != NULL) {
        cout << temp->data << " ";
        temp = temp->next;
    }
}

void Linkedlist::deleteList() {
    Node* temp = head;
    while (head != NULL)
    {
        temp = head;
        head = head->next;
        delete temp;
    }
    return;
} 

void Linkedlist::search(int data) {
    Node* temp = head;
    bool not_found = false;
    while(temp->data < data) {
        if(temp = temp->next) ;
        else {
            not_found = true;
            break;
        }
    }
    if(!not_found && temp->data == data) cout << "Found it \n";
    else cout << "Value does not exist \n";
}