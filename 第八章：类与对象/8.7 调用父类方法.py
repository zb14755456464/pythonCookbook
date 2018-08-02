# 问题
# 你想在子类中调用父类的某个已经被覆盖的方法。

# 解决方案
# 为了调用父类(超类)的一个方法，可以使用 super() 函数，比如：

class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()  # 调用夫类中的方法

# super() 函数的一个常见用法是在 __init__() 方法中确保父类被正确的初始化了




class A:
    def __init__(self):
        self.x = 0

class B(A):
    def __init__(self):
        super().__init__()  # 调用夫类中的__init__ 方法
        self.y = 1

# super() 的另外一个常见用法出现在覆盖Python特殊方法的代码中，比如：

class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value) # Call original __setattr__
        else:
            setattr(self._obj, name, value)



