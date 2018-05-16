# 问题
# 怎样在一个序列上面保持元素顺序的同时消除重复的值？

# 解决方案
# 如果序列上的值都是 hashable 类型，那么可以很简单的利用集合或者生成器来解决这个问题
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
'''
对上面的代码进行解释，因为dedupe加上了yield后变成了一个生成器，通过集合操作过滤重复出现的值，这样就会返回不重复的一个对象，
在通过list(生成器)转换成一个列表
'''
a = [1, 5, 2, 1, 9, 1, 5, 10]
result = list(dedupe(a))  # 消除重复并保留顺序
# print(result)


#  如果你仅仅就是想消除重复元素，通常可以简单的构造一个集合。比如：
res = set(a)
# print(res)


# 这个方法仅仅在序列中元素为 hashable 的时候才管用。 如果你想消除元素不可哈希（比如 dict 类型）的序列中重复元素的话，
# 你需要将上述代码稍微改变一下，就像这样：

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)  # 把列表中的每个元素转换成(1,2)
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

res = list(dedupe(a, key=lambda d: (d['x'],d['y'])))
print(res)