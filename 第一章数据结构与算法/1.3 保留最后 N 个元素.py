from collections import deque
# 保留有限历史记录正是 collections.deque 大显身手的时候
# 只保留队列中的最后三个
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)

print(q)
"""
在队列两端插入或删除元素时间复杂度都是 O(1) ，区别于列表，在列表的开头插入或删除元素的时间复杂度为 O(N) 
"""

# 取出队列,先进后出
result = q.pop()
print(result)