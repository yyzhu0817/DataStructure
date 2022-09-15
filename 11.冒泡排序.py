"""
# 排序方式
遍历列表并比较相邻的元素对，如果元素顺序错误，则交换它们。重复遍历列表未排序部分的元素，直到完成列表排序

# 时间复杂度
因为冒泡排序重复地通过列表的未排序部分，所以它具有最坏的情况复杂度O(n^2)
"""


def BubbleSort(__list):
    for i in range(len(__list)-1, -1, -1):
        for j in range(i):
            if __list[j] > __list[j+1]:
                __list[j], __list[j+1] = __list[j+1], __list[j]
    return __list

_list = [4,5,3,1,9,10,0,2]
_list = [2,1,3]
print(BubbleSort(_list))
