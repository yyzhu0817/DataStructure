"""
链式存储方式实现栈
思路：
    1、栈：LIFO 后进先出
    2、设计
       链表头部作为栈顶（入栈、出栈操作）
       链表尾部作为栈底（不进行任何操作）
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkListStack:
    def __init__(self):
        """初始化一个空栈"""
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        """相当于在链表头部增加一个节点"""
        node = Node(item)
        node.next = self.head
        self.head = node


    def pop(self):
        if self.is_empty():
            raise AttributeError('空栈了，pop不出来了，所以没有value属性了')
        item = self.head.value
        self.head = self.head.next
        return item

if __name__ == '__main__':
    s = LinkListStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    p = s.head
    while p:
        print(p.value, end=' ')
        p = p.next
    print('\n-------')
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())



