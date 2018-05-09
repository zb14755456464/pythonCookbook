# 问题
# 你想构造一个字典，它是另外一个字典的子集

# 解决方案
# 最简单的方式是使用字典推导。比如

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# 创建一个字典，价格超过200
p1 = {key: value for key, value in prices.items() if value > 200}


# 首先提供一个集合的键，去字典中去找，有就创建，没有则返回
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}


