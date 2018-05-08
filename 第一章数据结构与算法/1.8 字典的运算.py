# 问题
# 怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）？

# 解决方案
# 考虑下面的股票名和价格映射字典：

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 求出股票价格中的最大值和最小值,为了对字典值执行计算操作，通常需要使用 zip() 函数先将键和值反转过来
Max = max(zip(prices.values(),prices.keys()))
Min = min(zip(prices.values(),prices.keys()))
# print("Max:{max},Min:{min}".format(**{"max":Max,"min":Min}))

# 对字典按照values进行排序,zip函数可以映射成一个可迭代的对象
result = sorted(zip(prices.values(), prices.keys()))
print(result)

# 需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器。 比如，下面的代码就会产生错误：
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names)) # OK
print(max(prices_and_names)) # ValueError: max() arg is an empty sequence