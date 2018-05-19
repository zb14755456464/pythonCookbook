# 问题
# 你想创建一个内嵌变量的字符串，变量被它的值所表示的字符串替换掉。

# 解决方案
# Python并没有对在字符串中简单替换变量值提供直接的支持。 但是通过使用字符串的 format() 方法来解决这个问题。

s = '{name} has {n} messages.'
s.format(name='Guido', n=37) # 'Guido has 37 messages.'


