# 问题
# 你有一个被其他python代码使用的callable对象，可能是一个回调函数或者是一个处理器， 但是它的参数太多了，导致调用时出错。

# 解决方案
"""
如果需要减少某个函数的参数个数，你可以使用 functools.partial() 。
partial() 函数允许你给一个或多个参数设置固定的值，减少接下来被调用时的参数个数。 为了演示清楚，假设你有下面这样的函数
"""
def spam(a, b, c, d):
    print(a, b, c, d)

# 现在我们使用 partial() 函数来固定某些参数值：
from functools import partial

# 下面给span　参数中的a默认设置为1
s1 = partial(spam, 1) # a = 1 默认值
s1(2, 3, 4) # 1 2 3 4

s2 = partial(spam, d=42) # d = 42 默认值
s2(1, 2, 3) # 1 2 3 42

s3 = partial(spam, 1, 2, d=42) # a = 1, b = 2, d = 42
s3(3)  # 1 2 3 42



