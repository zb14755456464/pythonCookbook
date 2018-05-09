# 问题
# 怎样找出一个序列中出现次数最多的元素呢

# 解决方案
# collections.Counter 类就是专门为这类问题而设计的， 它甚至有一个有用的 most_common() 方法直接给了你答案。

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_counts = Counter(words)
# 统计出现频率最高的３个单词
# top_three = word_counts.most_common() # 这个是对所有的单词进行统计
top_three = word_counts.most_common(3) #  [('eyes', 8), ('the', 5), ('look', 4)]
print(top_three)

# 作为输入， Counter 对象可以接受任意的由可哈希（hashable）元素构成的序列对象。
# 在底层实现上，一个 Counter 对象就是一个字典，将元素映射到它出现的次数上,比如
print(word_counts['not'])
print(word_counts['eyes'])

# Counter 实例一个鲜为人知的特性是它们可以很容易的跟数学运算操作相结合
morewords = ['why','are','you','not','looking','in','my','eyes']
a = Counter(words)
b = Counter(morewords)
print(a)
print(b)

c = a + b
print(c)
d = a - b
print(d)

# 总结
'''
毫无疑问， Counter 对象在几乎所有需要制表或者计数数据的场合是非常有用的工具。 
在解决这类问题的时候你应该优先选择它，而不是手动的利用字典去实现
'''
