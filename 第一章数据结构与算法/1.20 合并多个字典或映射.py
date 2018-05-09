# 问题
# 现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某些操作， 比如查找值或者检查某些键是否存在

# 解决方案
# 假如你有如下两个字典:

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

# 现在假设你必须在两个字典中执行查找操作（比如先从 a 中找，如果找不到再在 b 中找）。
# 一个非常简单的解决方案就是使用 collections 模块中的 ChainMap 类。比如：

from collections import ChainMap

c = ChainMap(a, b)
print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)

# 讨论
'''
一个 ChainMap 接受多个字典并将它们在逻辑上变为一个字典。 
然后，这些字典并不是真的合并在一起了， ChainMap 类只是在内部创建了一个容纳这些字典的列表 
并重新定义了一些常见的字典操作来遍历这个列表。大部分字典操作都是可以正常使用的
'''
print(len(c))
print(c.keys())