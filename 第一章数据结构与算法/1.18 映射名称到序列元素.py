# 问题
# 你有一段通过下标访问列表或者元组中元素的代码，但是这样有时候会使得你的代码难以阅读， 于是你想通过名称来访问元素

# 解决方案
# collections.namedtuple() 函数通过使用一个普通的元组对象来帮你解决这个问题。
# 这个函数实际上是一个返回 Python 中标准元组类型子类的一个工厂方法


from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')  # Subscriber(addr='jonesy@example.com', joined='2012-10-19')
sub.addr # jonesy@example.com


