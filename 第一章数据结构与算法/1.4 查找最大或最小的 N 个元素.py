import heapq

# 使用场景

#  如果 N 快接近集合大小了，那么使用排序操作会更好些
# sorted(items)[:N] 或者是 sorted(items)[-N:] ）


# 从列表中获取最大和最小的N个元素
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# 从nums列表中获取最大的三个元素
print(heapq.nlargest(3, nums))  # [42, 37, 23]

# 从nums列表中获取最小的三个元素
print(heapq.nsmallest(3, nums))  # [-4, 1, 2]

#  两个函数都能接受一个关键字参数，用于更复杂的数据结构中：
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# 上面代码在对每个元素进行对比的时候，会以 price 的值进行比较。

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])

expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])