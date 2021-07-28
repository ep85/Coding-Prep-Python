'''
Binary Search Tree (BST)

Every node has at most 2 child nodes
No Duplicates


                15
        12              27
    7       14    20          88
                    23

Insert O(log(n))
Delete O(log(n))
Searching O(log(n))

Searches
-Breadth first search
-Depth first search
    -In order traversal - always going left all the way down first then right
    -Pre order traversal 
    -Post order traversal

In order traversal [7,12,14,15,20,23,27,88]
Pre order traversal [15,12,7,14,27,20,23,88]
Post order traversal [7,14,12,23,20,88,27,15]
'''

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return 
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else: 
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []

        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        #visit base node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
            
        return self



def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    
    for i in range (1,len(elements)):
        root.add_child(elements[i])
    
    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print("Does value 100 exist", numbers_tree.search(100))
    print("Does value 4 exist", numbers_tree.search(4))
    print(numbers_tree.in_order_traversal())
    numbers_tree.delete(20)
    print(numbers_tree.in_order_traversal())