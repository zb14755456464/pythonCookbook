# 问题
# 你有一系列排序序列，想将它们合并后得到一个排序序列并在上面迭代遍历

# 解决方案
# heapq.merge() 函数可以帮你解决这个问题。比如：

import heapq

a = [1, 4, 7, 10]

b = [2, 5, 6, 11]

print(list(heapq.merge(a, b)))

for c in heapq.merge(a, b): # heapq.merge(a, b) 合并后是一个有顺序的新的迭代器
    print(c)

# 讨论
#　heapq.merge 可迭代特性意味着它不会立马读取所有序列。
# 这就意味着你可以在非常长的序列中使用它，而不会有太大的开销。 比如，下面是一个例子来演示如何合并两个排序文件


