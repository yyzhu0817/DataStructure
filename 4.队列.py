"""
顺序存储方式去实现队列模型
思路：
    1、队列：FIFO 先进先出,队尾负责入队,队头负责出队
    2、设计：
       列表头部作为队头,负责出队
       列表尾部作为队尾,负责入队
"""


class Queue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def enqueue(self, item):
        self.elements.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception('从空队列弹出')
        return self.elements.pop(0)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.elements)
    q.dequeue()
    q.dequeue()
    print(q.elements)
