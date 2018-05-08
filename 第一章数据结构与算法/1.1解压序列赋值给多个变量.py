p = (4, 5)
x, y = p
print(x, y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name, shares, price)

#  实际上，这种解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。 包括字符串，文件对象，迭代器和生成器
s = 'Hello'
a, b, c, d, e = s
print(a, b, c, d, e)

# 有时候，你可能只想解压一部分，丢弃其他的值。
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares, price)
