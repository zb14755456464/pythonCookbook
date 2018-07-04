# 问题
# 你想遍历一个可迭代对象中的所有元素，但是却不想使用for循环。

# 解决方案
#为了手动的遍历可迭代对象，使用 next() 函数并在代码中捕获 StopIteration 异常。 比如，下面的例子手动读取一个文件中的所有行

items = [1, 2, 3, 4]

it = iter(items)

def manual_iter():
        try:
            while True:
                line = next(it)
                print(line, end='')

        except StopIteration:  #  StopIteration 用来指示迭代的结尾
            pass


# 果你手动使用上面演示的 next() 函数的话，你还可以通过返回一个指定值来标记结尾，比如 None 。 下面是示例：
def manual_iter():
    try:
        while True:
            line = next(it,None)  # 如果到达结尾的话,可以返回一个指定值来标记结尾
            if line is None:
                break
            print(line, end='')

    except StopIteration:  # StopIteration 用来指示迭代的结尾
        pass

    
if __name__ == '__main__':
    manual_iter()