# 问题
# 你正在试着用正则表达式匹配某个文本模式，但是它找到的是模式的最长可能匹配。 而你想修改它变成查找最短的可能匹配

import re

str_pat = re.compile(r'"(.*)"')
text2 = 'Computer says "no." Phone says "yes."'
res = str_pat.findall(text2) # ['no." Phone says "yes.']　列表里的元素只有一个

# 贪婪模式
# 为了修正这个问题，可以在模式中的*操作符后面加上 ? 修饰符，就像这样
str_pat = re.compile(r'"(.*?)"')
res = str_pat.findall(text2) # ['no.', 'yes.']

# 这样就使得匹配变成非贪婪模式，从而得到最短的匹配，也就是我们想要的结果。