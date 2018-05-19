# 问题
# 你想为 sort() 操作创建一个很短的回调函数，但又不想用 def 去写一个单行函数， 而是希望通过某个快捷方式以内联方式来创建这个函数

add = lambda x, y: x + y
add(2,3) # 5

# 尽管lambda表达式允许你定义简单函数，但是它的使用是有限制的


