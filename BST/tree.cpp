#include <stdio.h>
#include <iostream>

using namespace std;

class TreeNode {
    public:
        int data;
        TreeNode* left;
        TreeNode* right;
    TreeNode()
    {
        data = 0;
        left = NULL;
        right = NULL;
    }
    TreeNode(int data)
    {
        this->data = data;
        this->left = NULL;
        this->right = NULL;
    }
};

class BST {
    TreeNode* head;
public:
    BST() { head = NULL; }
    TreeNode* getHead() { return head; }
    int getHeadData() { return head->data; }
    void insertNode(int);
    void printTreeInorder(TreeNode*);
    void printTreePostorder(TreeNode*);
    void deleteTree(TreeNode*);
    void search(int);
};

void BST::insertNode(int data)  {
    TreeNode* newNode = new TreeNode(data);
    if (head == NULL) 
    {
        head = newNode;
        return;
    }
    TreeNode* temp = head;
    while (1)
    {
        if (newNode->data > temp->data && temp->right == NULL)
        {
            temp->right = newNode;
            break;
        }
        if (newNode->data < temp->data && temp->left == NULL)
        {
            temp->left = newNode;
            break;
        }
        if (newNode->data < temp->data && temp->left != NULL)
            temp = temp->left;
        if (newNode->data > temp->data && temp->right != NULL)
            temp = temp->right;
    }
}

void BST::printTreeInorder(struct TreeNode *root) {
    if (root != NULL) {
        printTreeInorder(root->left);
        cout << root->data << " ";
        printTreeInorder(root->right);
    }
    return;
}

void BST::printTreePostorder(struct TreeNode *root) {
    if (root != NULL) {
        printTreePostorder(root->left);
        printTreePostorder(root->right);
        cout << root->data << " ";
    }
    return;
}

void BST::deleteTree(struct TreeNode *root) {
    if (root != NULL) {
        deleteTree(root->left);
        deleteTree(root->right);
        delete root;
    }
    return;
}

void BST::search(int x) {
    struct TreeNode* ptr = head;
    while (ptr) {
        if (x > ptr->data && ptr->right != NULL)
            ptr = ptr->right; else if (x < ptr->data && ptr->left != NULL)
            ptr = ptr->left; else
            break;
    }
    cout << ptr->data;
}