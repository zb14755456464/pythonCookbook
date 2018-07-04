# 问题
# 你想迭代遍历一个集合中元素的所有可能的排列或组合

# 解决方案
# itertools模块提供了三个函数来解决这类问题。 其中一个是 itertools.permutations() ， 它接受一个集合并产生一个元组序列，
# 每个元组由集合中所有元素的一个可能排列组成。 也就是说通过打乱集合中元素排列顺序生成一个元组，比如
from itertools import permutations,combinations

items = ['a', 'b', 'c']

print(list(permutations(items,2))) # 对一个列表,进行有序的任意的排列组合,这个是A6,3

print(list(combinations(items,2))) # 这个是C6,3 元素的顺序就不重要了

# 讨论
"""
这一小节我们向你展示的仅仅是 itertools 模块的一部分功能。 尽管你也可以自己手动实现排列组合算法，但是这样做得要花点脑力。 
当我们碰到看上去有些复杂的迭代问题时，最好可以先去看看itertools模块。 如果这个问题很普遍，那么很有可能会在里面找到解决方案！
我们可以对一个列表,指定顺序排列,然后按照顺序确定优先级执行我们想要的操作

"""



