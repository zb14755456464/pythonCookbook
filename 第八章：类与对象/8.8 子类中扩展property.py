# 问题
# 在子类中，你想要扩展定义在父类中的property的功能。

# 解决方案
# 考虑如下的代码，它定义了一个property：


class Person:
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        print(123)
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


# 下面是一个示例类，它继承自Person并扩展了 name 属性的功能

class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)  # 调用夫类中的设置属性的方法

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)

if __name__ == '__main__':

    s = SubPerson('Guido')
    s.name = 42













