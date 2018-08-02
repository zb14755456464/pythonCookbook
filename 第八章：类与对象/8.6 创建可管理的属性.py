
# 问题
# 你想给某个实例attribute增加除访问与修改之外的其他处理逻辑，比如类型检查或合法性验证

# 解决方案
# 自定义某个属性的一种简单方法是将它定义为一个property。 例如，下面的代码定义了一个property，增加对一个属性简单的类型检查


class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        print(self._first_name)
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


if __name__ == '__main__':
    a = Person('Guido')
    a.first_name  # 把函数当作属性去使用
    # a.first_name = 12 在设置属性的时候对参数进行了校验，要是修改后的数据不是字符串就会保存

# 注意　－－－－－> 在实例化对象的时候，会自动调用setter方法,对参数进行校验,因此，你可能想在初始化的时候也进行这种类型检查。
# 通过设置 self.first_name ，
# 自动调用 setter 方法， 这个方法里面会进行参数的检查，否则就是直接访问 self._first_name 了

'''
上述代码中有三个相关联的方法，这三个方法的名字都必须一样。 
第一个方法是一个 getter 函数，它使得 first_name 成为一个属性。 
其他两个方法给 first_name 属性添加了 setter 和 deleter 函数。 需要强调的是只有在 first_name 属性被创建后， 
后面的两个装饰器 @first_name.setter 和 @first_name.deleter 才能被定义
'''
