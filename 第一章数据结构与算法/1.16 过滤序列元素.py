# 问题
# 你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列

# 解决方案
# 最简单的过滤序列元素的方法就是使用列表推导。比如：
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
res = [ n for n in mylist if n >0 ]  # [1, 4, 10, 2, 3]


# 使用列表推导的一个潜在缺陷就是如果输入非常大的时候会产生一个非常大的结果集，占用大量内存。
#  如果你对内存比较敏感，那么你可以使用生成器表达式迭代产生过滤的元素。比如：
res = ( n for n in mylist if n > 0 )

# 讨论
# 列表推导和生成器表达式通常情况下是过滤数据最简单的方式。 其实它们还能在过滤的时候转换数据。比如
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math
[math.sqrt(n) for n in mylist if n > 0]


# 过滤操作的一个变种就是将不符合条件的值用新的值代替，而不是丢弃它们
clip_neg = [n if n > 0 else 0 for n in mylist] # 把小于0的用0代替


# 另外一个值得关注的过滤工具就是 itertools.compress() ，
# 它以一个 iterable 对象和一个相对应的 Boolean 选择器序列作为输入参数。
# 然后输出 iterable 对象中对应选择器为 True 的元素。 当你需要用另外一个相关联的序列来过滤某个序列的时候，这个函数是非常有用的
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

# 生成一个bool值
from itertools import compress

more5 = [n > 5 for n in counts] # [False, False, True, False, False, True, True, False]

# 现在你想将那些对应 count 值大于5的地址全部输出，那么你可以这样做：
res = list(compress(addresses,more5))

# 这里的关键点在于先创建一个 Boolean 序列，指示哪些元素符合条件。
# 然后 compress() 函数根据这个序列去选择输出对应位置为 True 的元素。