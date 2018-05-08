import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    '''
    在上面代码中,队列包含了一个 (-priority, index, item) 的元组,优先级为负数的目的是使得元素按照优先级从高到低排序。
    这个跟普通的按优先级从低到高排序的堆排序恰巧相反。

    index 变量的作用是保证同等优先级元素的正确排序,通过保存一个不断增加的 index 下标变量，可以确保元素按照它们插入的顺序排序。
    而且,index 变量也在相同优先级元素比较的时候起到重要作用。
    '''

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # 作用返回一个对象的可打印的字符
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

'''
下面的输出结果
Item('bar') 5 
Item('spam') 4 
Item('foo') 1 0
Item('grok') 1 4
'''

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
