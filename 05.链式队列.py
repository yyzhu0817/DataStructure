"""
链式存储方式去实现队列
思路：
    1、队列：FIFO 先进先出
    2、设计：
       链表头部作为队头,负责出队操作
       链表尾部作为队尾,负责入队操作
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkListQueue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, item):
        node = Node(item)
        # 空队列情况
        if self.is_empty():
            self.head = node
            return
        # 非空队列情况
        q = self.head
        while q.next:
            q = q.next
        q.next = node
        node.next = None

    def dequeue(self):
        if self.is_empty():
            raise Exception('队列为空')
        p = self.head
        self.head = self.head.next
        return p.value

if __name__ == '__main__':
    q = LinkListQueue()
    q.enqueue(100)
    q.enqueue(200)
    q.enqueue(300)
    print(q.dequeue())
    print(q.dequeue())

