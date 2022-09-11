'''
输入一个链表，反转链表后，输出新链表的表头
思路:
    1、创建2个游标,代表要进行反转操作的节点 和 上一个节点
    2、代码逻辑:
       当前节点指针指向上一个节点
       两个游标同时往后移动
       结束标准: 当要操作的节点为None时,结束! 此时pre代表的是新链表的头节点
'''
from LinkList import SingleLinkList


class Solution(SingleLinkList):
    def __init__(self):
        super().__init__()

    def reverse(self):
        if self.is_empty():
            return
        cur = self.head
        pre = None
        while cur is not None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        self.head = pre


if __name__ == '__main__':
    s = Solution()
    s.append(1)
    s.append(2)
    s.append(3)
    s.append(4)
    s.append(5)
    s.travel()
    s.reverse()
    s.travel()
