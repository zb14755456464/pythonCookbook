# 问题
# 你想封装类的实例上面的“私有”数据，但是Python语言并没有访问控制。

# 解决方案
# Python程序员不去依赖语言特性去封装数据，而是通过遵循一定的属性和方法命名规约来达到这个效果。
#  第一个约定是任何以单下划线_开头的名字都应该是内部实现。比如

class A:
    def __init__(self):
        self._internal = 0 # An internal attribute
        self.public = 1 # A public attribute

    def public_method(self):
        '''
        A public method
        '''
        pass

    def _internal_method(self):
        print(123)


class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        print(123)


    def public_method(self):
        pass
        self.__private_method()


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1 # Does not override B.__private

    # Does not override B.__private_method()
    def __private_method(self):
        pass




if __name__ == '__main__':
    a = A()
    a._internal_method()  # 单下划线可以外部调用

    b = B()
    # b._internal_method() 不可以外部调用
    b.public_method()   # 双下划线这个只能在内部调用

    c = C()
    print(dir(c)) # ['_B__private', '_B__private_method', '_C__private', '_C__private_method']


# 讨论

'''
上面提到有两种不同的编码约定(单下划线和双下划线)来命名私有属性，那么问题就来了：到底哪种方式好呢？ 大多数而言，
你应该让你的非公共名称以单下划线开头。
但是，如果你清楚你的代码会涉及到子类， 并且有些内部属性应该在子类中隐藏起来，那么才考虑使用双下划线方案
'''
