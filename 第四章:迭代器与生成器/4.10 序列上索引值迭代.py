# 问题
# 你想在迭代一个序列的同时跟踪正在被处理的元素索引。

# 解决方案
# 内置的 enumerate() 函数可以很好的解决这个问题：

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
   print(idx, val)

print("="*100)
# 为了按传统行号输出(行号从1开始)，你可以传递一个开始参数：
for idx, val in enumerate(my_list,1):
   print(idx, val)
