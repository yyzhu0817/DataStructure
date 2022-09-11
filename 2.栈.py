"""
顺序存储的方式实现栈
思路：
    1、栈 ：LIFO 后进先出
    2、设计
       列表尾部作为栈顶（入栈、出栈操作）
       列表头部作为栈底（不进行任何操作）
"""
class Stack:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push(self, item):
        self.elems.append(item)
        print(self.elems)

    def destack(self):
        if self.is_empty():
            raise IndexError(f'从空栈弹出')
        return self.elems.pop()

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.destack())
    print(stack.destack())
    print(stack.destack())
    print(stack.destack())
    print(stack.destack())









