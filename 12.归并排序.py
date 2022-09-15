"""
# 思想
分而治之算法

# 步骤
1) 连续划分未排序列表，直到有N个子列表，其中每个子列表有1个"未排序"元素，N是原始数组中的元素数
2) 重复合并，即一次将两个子列表合并在一起，生成新的排序子列表，直到所有元素完全合并到一个排序数组中
"""


def merge_sort(li):
    # 递归出口
    if len(li) == 1:
        return li

    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]
    # 递归思想
    left_li = merge_sort(left)
    right_li = merge_sort(right)

    return merge(left_li, right_li)


def merge(left_li, right_li):
    """将2个有序列表合并为一个有序列表"""
    result = []
    # print(f'lift_li: {left_li} --- right_li: {right_li}')
    while left_li and right_li:
        if left_li[0] >= right_li[0]:
            result.append(right_li.pop(0))
        else:
            result.append(left_li.pop(0))

    # 循环结束时,一定有一个列表为空了
    if left_li:
        result.extend(left_li)
    else:
        result.extend(right_li)
    # print(f'result: {result}')
    return result


if __name__ == '__main__':
    li = [3, 1, 2, 5]
    r = merge_sort(li)
    print(r)
