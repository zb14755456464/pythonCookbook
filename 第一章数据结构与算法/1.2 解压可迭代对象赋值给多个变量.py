def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record  # phone_numbers是一个列表 ['773-555-1212', '847-555-1212'],加上* 就是把所有的内容取出来773-555-1212 847-555-1212
# print(name, email, *phone_numbers)


# 当然也可以把列表放在前面
*trailing, current, last = [10, 8, 7, 1, 9, 5, 10, 3]  # 会根据接受的参数自动的去区分
# print(*trailing, current, last)


# 扩展的迭代解压语法是专门为解压不确定个数或任意个数元素的可迭代对象而设计的，一般第一个元素都有确定的规则
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

#  星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')


# 如果你够聪明的话，还能用这种分割语法去巧妙的实现递归算法
def sum(items):
    """
    递归的终止条件
     if tail:
        return head+sum(tail)
    else:
        return head
    """
    head, *tail = items

    return head + sum(tail) if tail else head


items = [1, 10, 7, 4, 5, 10]
print(sum(items))
