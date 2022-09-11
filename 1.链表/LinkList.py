class Node:
    """节点类，生成节点的超级工厂"""

    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkList:
    """单链表类，数学模型"""

    def __init__(self):
        """初始化一个空链表：头节点为None的链表为空链表"""
        self.head = None

    def is_empty(self):
        """判断是否为空"""
        return self.head is None

    def travel(self):
        """遍历链表"""
        cur = self.head
        while cur:
            print(f'{cur.value}', end=' ')
            cur = cur.next
        print()

    def add(self, item):
        """在链表头部添加节点"""
        node = Node(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        """在链表尾部添加节点"""
        node = Node(item)
        if self.is_empty():  # 情况1：空链表
            self.head = node
        else:  # 情况2：非空链表
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.next = None

    def remove(self, item):
        """删除链表中的某个相同节点"""
        if self.head.value == item:
            self.remove_head()
        cur = self.head
        pre = cur
        while cur:
            if cur.value != item:
                pre = cur
                cur = cur.next
            else:
                pre.next = cur.next
                break

    def remove_head(self):
        """删除头节点"""
        if self.is_empty():
            return
        self.head = self.head.next

    def remove_all_same_item(self, item):
        """删除所有相同节点"""
        while self.head.value == item:
            self.remove_head()

        cur = self.head
        pre = cur
        while cur:
            if cur.value != item:
                pre = cur
                cur = cur.next
            else:
                pre.next = cur.next
                cur = pre.next


if __name__ == '__main__':
    s = SingleLinkList()
    s.append(1)
    s.append(2)
    s.append(3)
    s.travel()

    while s.head is not None:
        print(s.head.value)
        s.head = s.head.next

    head1 = Node(100)
    head1.next = Node(200)
    head1.next.next = Node(300)
    head1.next.next.next = Node(400)
    print(head1)
    print(head1.next)
    print(head1.next.next)
    print(head1.next.next.next)
