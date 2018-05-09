# 问题
#你需要在数据序列上执行聚集函数（比如 sum() , min() , max() ）， 但是首先你需要先转换或者过滤数据


# 解决方案
#一个非常优雅的方式去结合数据计算与转换就是使用一个生成器表达式参数。 比如，如果你想计算平方和，可以像下面这样做

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)  # 生成器作为一个参数传惨,可以省略了括号


portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio) #  生成器作为一个参数传惨,可以省略了括号

# 总结：在使用一些聚集函数比如 min() 和 max() 的时候你可能更加倾向于使用生成器版本


