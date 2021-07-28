'''
Tree (General)

Electronic Ecommerce website
Categorizing store items
                        Electronics 
    Laptops             Televisions             Phones
Mac     Windows       Samsung LG  TCL       Iphone  Pixel LTC

Root - Highest NOde
Leaf Nodes - Bottom Row
Parents - Laptops
Children of Laptops - Mac and Windows
Anestors of Iphone - Cell Phones and Electronix

Level0 - Electronicx
Level1 - Laptops
Level2 - Mac,Windows,Samsung...

Insert O(log(n))
Delete O(log(n))
Searching O(log(n))

'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()

if __name__ == '__main__':
    build_product_tree()


from collections import deque
# Traverse a Tree
def traverse(tree):
    if tree == None:
        return
    queue = deque()
    queue.appendleft(tree)
    while queue:
        curr = queue.pop()
        print(curr.data)
        if curr.children:
            for child in curr.children:
              queue.appendleft(child)

