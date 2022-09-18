"""
【1】介绍
    快速排序也是一种分而治之的算法，在大多数标准实现中，它的执行速度明显快于归并排序

【2】排序步骤：
    2.1) 首先选择一个元素，称为数组的基准元素
    2.2) 将所有小于基准元素的元素移动到基准元素的左侧；将所有大于基准元素的移动到基准元素的右侧
    2.3) 递归地将上述两个步骤分别应用于比上一个基准元素值更小和更大的元素的每个子数组
"""


def quick_sort(li, first, last):
    """快速排序"""
    # 递归出口
    if first > last:
        return

    # position:基准值正确位置下标索引,即:分隔li为左右两部分的值
    pivot = sort(li, first, last)
    # 递归思想,左右两部分继续执行快速排序
    quick_sort(li, first, pivot - 1)
    quick_sort(li, pivot + 1, last)


def sort(li, first, last):
    """
    :param li: 无序的数组
    :param first: 基准值所在位置的索引
    :param last: 右游标的索引
    :return: 基准值正确位置的下标索引
    """
    l = first + 1
    r = last
    while True:
        # 左游标右移
        while l <= r and li[l] <= li[first]:
            l += 1
        # 右游标左移
        while l <= r and li[r] >= li[first]:
            r -= 1

        if l < r:
            # 左右游标互换位置
            li[l], li[r] = li[r], li[l]
        else:
            # 右游标和基准值互换位置
            # 右游标就是基准值的正确位置
            li[first], li[r] = li[r], li[first]
            # 返回了基准值正确位置的下标索引
            return r

if __name__ == '__main__':
    li = [6, 5, 3, 1, 8, 7, 2, 8, 666, 6, 2, 4]
    # li = [6, 0, 1, 3, 2, 4, 3]
    quick_sort(li, 0, len(li) - 1)
    print(li)
