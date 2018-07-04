# 问题
# 你想同时迭代多个序列，每次分别从一个序列中取一个元素。

#解决方案
#为了同时迭代多个序列，使用 zip() 函数。比如：

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]

for x, y in zip(xpts,ypts): # 这个以最短的为主
    print(x, y)  # 在这里把元祖进行了拆包

"""
zip(a, b) 会生成一个可返回元组 (x, y) 的迭代器，其中x来自a，y来自b。 
一旦其中某个序列到底结尾，迭代宣告结束。 因此迭代长度跟参数中最短序列长度一致。
"""
print("+"*50)
# 如果这个不是你想要的效果，那么还可以使用 itertools.zip_longest() 函数来代替。比如：
from itertools import zip_longest

a = [1, 2]
b = ['w', 'x', 'y', 'z']

for i in zip_longest(a,b): # 长度不够的用None代替
    print(i)

# 讨论
# 当你想成对处理数据的时候 zip() 函数是很有用的。 比如，假设你头列表和一个值列表，就像下面这样：


headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]

s = dict(zip(headers,values)) # {'name': 'ACME', 'shares': 100, 'price': 490.1}

print(s)



# 最后强调一点就是， zip() 会创建一个迭代器来作为结果返回。 如果你需要将结对的值存储在列表中，要使用 list() 函数。比如













