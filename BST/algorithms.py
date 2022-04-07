from sys import getrefcount
from random import sample


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    @classmethod
    def listSearch(cls, node):
        if node.next is not None:
            cls.listSearch(node.next)
        print(node.value)

    @staticmethod
    def insert(node, value):
        new_node = ListNode(value)
        prev = None
        while node.next is not None and node.value < value:
            prev = node
            node = node.next
        if prev is None and node.value > value:
            node.value, new_node.value = new_node.value, node.value
            new_node.next = node.next
            node.next = new_node
        elif node.next is None and node.value < value:
            node.next = new_node
        else:
            prev.next = new_node
            new_node.next = node


    def __delete__(self):
        print("LIST NODE DELETED")


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    @classmethod
    def height(cls, root):
        if root is None:
            return 0
        left_h = cls.height(root.left)
        right_h = cls.height(root.right)
        return max(left_h, right_h) + 1

    @classmethod
    def treeSearchInorder(cls, root):
        if root.left is not None:
            cls.treeSearchInorder(root.left)
        print(root.value)
        if root.right is not None:
            cls.treeSearchInorder(root.right)

    @classmethod
    def treeSearchPreorder(cls, root):
        print(root.value)
        if root.left is not None:
            cls.treeSearchPreorder(root.left)
        if root.right is not None:
            cls.treeSearchPreorder(root.right)

    @classmethod
    def treeSearchPostorder(cls, root):
        if root.left is not None:
            cls.treeSearchPostorder(root.left)
        if root.right is not None:
            cls.treeSearchPostorder(root.right)
        print(root.value)

    @staticmethod
    def insert(root, value):
        new_root = TreeNode(value)
        while True:
            if new_root.value > root.value and root.right is None:
                root.right = new_root
                break
            elif new_root.value < root.value and root.left is None:
                root.left = new_root
                break
            elif new_root.value > root.value and root.right is not None:
                root = root.right
            else:
                root = root.left


    #def __delete__(self, instance):
        #print("TREE NODE DELETED")


def random_array(scope, length):
    return sample(range(scope), length)


"""def delarr(index):
    del locals()["index"]

arr = [1, 2, 3]
delarr(arr[0])
print(arr)"""


numbers = random_array(1000, 100)
# numbers2 = random_array(1000, 100)

"""pine = TreeNode(numbers[0])

for i in numbers[1:]:
    TreeNode.insert(pine, i)"""

#TreeNode.treeSearchInorder(pine)
#TreeNode.treeDelete(pine)

sequence = ListNode(numbers[0])
for i in numbers[1:]:
    ListNode.insert(sequence, i)

ListNode.listDelete(sequence)

ListNode.listSearch(sequence)

"""arr = []

while sequence.next is not None:
    arr.append(sequence.value)
    sequence = sequence.next
arr.append(sequence.value)

for x in range(1000):
    print(arr == sorted(numbers))"""


