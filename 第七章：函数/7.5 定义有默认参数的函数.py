# 问题
# 你想定义一个函数或者方法，它的一个或多个参数是可选的并且有一个默认值。

# 解决方案
# 定义一个有可选参数的函数是非常简单的，直接在函数定义中给参数指定一个默认值，并放到参数列表最后就行了
def spam(a, b=42):
    print(a, b)

spam(1) # Ok. a=1, b=42
spam(1, 2) # Ok. a=1, b=2

# 如果默认参数是一个可修改的容器比如一个列表、集合或者字典，可以使用None作为默认值，就像下面这样：
def spam(a, b=None):
    if b is None:
        b = []

