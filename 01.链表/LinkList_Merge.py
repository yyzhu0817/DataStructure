'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则

思路:
    1、程序最终返回的是: 合并后的链表的头节点
    2、先确定新链表的头节点
    3、互相比较,移动值小的游标
'''
from LinkList import SingleLinkList
class Solution(SingleLinkList):
    def __init__(self):
        super().__init__()

    def merge_two_linklist(self, p1, p2):
        """
        :param head1:
        :param head2:
        :return: head
        """
        # 1.确定新的表头节点
        if p1.value < p2.value:
            cur = p1
            p1 = p1.next
        else:
            cur = p2
            p2 = p2.next
        head = cur
        # 2.一次循环比较其他节点
        while p1 and p2:
            if p1.value < p2.value:
                cur.next = p1
                cur = cur.next
                p1 = p1.next
            else:
                cur.next = p2
                cur = cur.next
                p2 = p2.next
        # 3.循环结束，p1 or p2一定有一个为None
        #   将cur指向不为None的那一个
        if p1:
            cur.next = p1
        else:
            cur.next = p2

        return head


if __name__ == '__main__':
    s1 = Solution()
    s2 = Solution()
    s1.append(1)
    s1.append(2)
    s1.append(5)
    s1.append(6)
    s1.travel()
    # print(s1.head)

    s2.append(3)
    s2.append(4)
    s2.append(7)
    s2.append(8)
    s2.travel()
    # print(s2.head)

    s3 = Solution()
    node = s3.merge_two_linklist(s1.head, s2.head)
    while node:
        print(node.value, end=' ')
        node = node.next