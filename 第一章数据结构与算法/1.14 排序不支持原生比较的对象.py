# 问题
# 你想排序类型相同的对象，但是他们不支持原生的比较操作。

# 解决方案
# 内置的 sorted() 函数有一个关键字参数 key ，可以传入一个 callable 对象给它，
# 这个 callable 对象对每个传入的对象返回一个值，这个值会被 sorted 用来排序这些对象。
# 比如，如果你在应用程序里面有一个 User 实例序列，并且你希望通过他们的 user_id 属性进行排序，
# 你可以提供一个以 User 实例作为输入并输出对应 user_id 值的 callable 对象

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id) # 打印该对象的时候返回的信息



from operator import attrgetter

def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users) # [User(23), User(3), User(99)]
    print(sorted(users, key=lambda u: u.user_id))   # [User(3), User(23), User(99)]
    res = sorted(users, key=attrgetter('user_id'))
    return res

res = sort_notcompare()
print(res)
