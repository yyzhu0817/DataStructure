"""
二叉树 添加节点
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, node=None):
        """创建了一个空树，或者只有树根的树"""
        self.root = node

    def add(self, value):
        """在树中添加一个节点"""
        node = Node(value)
        # 1. 空树
        if self.root is None:
            self.root = node
            return
        # 2.非空树
        tree_list = [self.root]
        while tree_list:
            # for _ in tree_list:
            #     print(_.value, end=' ')
            # print()
            tree_node = tree_list.pop(0)
            # print(tree_node.value)
            if tree_node.left:
                tree_list.append(tree_node.left)
            else:
                tree_node.left = node
                return
            if tree_node.right:
                tree_list.append(tree_node.right)
            else:
                tree_node.right = node
                return

    def breadth_travle(self):
        # 1.空树的情况
        if self.root is None:
            return
        node_list = [self.root]
        while node_list:
            tree_node = node_list.pop(0)
            print(tree_node.value, end=' ')
            if tree_node.left:
                node_list.append(tree_node.left)
            if tree_node.right:
                node_list.append(tree_node.right)


    def pre_travel(self, node):
        """前序遍历"""
        if node:
            print(node.value, end=' ')
            self.pre_travel(node.left)
            self.pre_travel(node.right)
        else:
            return
    def mid_travel(self, node):
        """中序遍历"""
        if node:
            self.mid_travel(node.left)
            print(node.value, end=' ')
            self.mid_travel(node.right)
        else:
            return
    def last_travel(self, node):
        """后序遍历"""
        if node:
            self.last_travel(node.left)
            self.last_travel(node.right)
            print(node.value, end=' ')
        else:
            return

if __name__ == '__main__':
    node = Node(10)
    node.left = Node(20)
    node.right = Node(21)
    node.left.left = Node(31)
    node.left.right = Node(32)
    node.right.left = Node(33)

    tree = Tree(node)
    tree.add(34)
    tree.add(41)
    tree.breadth_travle()
    print()
    tree.pre_travel(node)
    print()
    tree.mid_travel(node)
    print()
    tree.last_travel(node)