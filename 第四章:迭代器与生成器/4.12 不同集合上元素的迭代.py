# 问题
# 你想在多个对象执行相同的操作，但是这些对象在不同的容器中，你希望代码在不失可读性的情况下避免写重复的循环

#解决方案
"""
itertools.chain() 方法可以用来简化这个任务。 它接受一个可迭代对象列表作为输入，
并返回一个迭代器，有效的屏蔽掉在多个容器中迭代细节。 为了演示清楚，考虑下面这个例子
"""

from itertools import chain

a = [1, 2, 3, 4]

b = ['x', 'y', 'z']

for x in chain(a, b): # 都是循环遍历,a,b两个列表,为了避免这样的重复操作,可以使用chain
    print(x)

#讨论
"""
itertools.chain() 接受一个或多个可迭代对象作为输入参数。 然后创建一个迭代器，
依次连续的返回每个可迭代对象中的元素。 这种方式要比先将序列合并再迭代要高效的多。
"""