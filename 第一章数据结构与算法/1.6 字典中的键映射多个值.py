# 问题
#  怎样实现一个键对应多个值的字典（也叫 multidict）？

# 解决方案
# 一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，那么你就需要将这多个值放到另外的容器中，
#  比如列表或者集合里面。比如，你可以像下面这样构造这样的字典：

d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

from collections import defaultdict

d = defaultdict(list)  # defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，所以你只需要关注添加元素操作了
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d['c'] = 1


# 需要注意的是， defaultdict 会自动为将要访问的键（就算目前字典中并不存在这样的键）创建映射实体。
#  如果你并不需要这样的特性，你可以在一个普通的字典上使用 setdefault() 方法来代替。比如：

d = {} # 一个普通的字典
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)


# 讨论
'''
一般来讲，创建一个多值映射字典是很简单的。但是，如果你选择自己实现的话，那么对于值的初始化可能会有点麻烦，
 你可能会像下面这样来实现：
'''
pairs = [['a', 2], ['b', 4],['a',5]]
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

#  如果使用 defaultdict 的话代码就更加简洁了
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)

print(d)










