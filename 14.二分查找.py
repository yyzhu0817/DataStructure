"""
【1】定义及优点
	二分查找又称折半查找，优点是比较次数少，查找速度快，平均性能好

【2】查找过程
　　二分查找即搜索过程从数组的中间元素开始,如果中间元素正好是要查找的元素,则搜索过程结束;
    如果中间元素大于或小于要查找元素,则在小于或大于中间元素的那一半进行搜索,而且跟开始一样从中间元素开始比较.
    如果在某一步骤数组为空,则代表找不到.这种算法每一次比较都会使搜索范围缩小一半.

【3】适用条件
	'数组必须有序'
"""
def binary_search(li, target):
    """递归版本"""
    mid = len(li) // 2
    if li[mid] == target:
        return True
    if len(li) == 1:
        return False
    if li[mid] > target:
        return binary_search(li[:mid], target)
    else:
        return binary_search(li[mid:], target)

def binary_search_normal(li, target):
    """非递归版本"""
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if target < li[mid]:
            right = mid - 1
        elif target > li[mid]:
            left = mid + 1
        else:
            return True
    return False

if __name__ == '__main__':
    li = [1, 2, 3, 4, 5, 6, 7, 8]
    # 终端1: True
    print(binary_search(li, 8))
    # 终端2: False
    print(binary_search(li, 9))

    print(binary_search_normal(li, 3))
    print(binary_search_normal(li, 9))
