# 问题
# 你想在字符串中搜索和匹配指定的文本模式

# 解决方案
# 对于简单的字面模式，直接使用 str.replace() 方法即可，比如：
text = 'yeah, but no, but yeah, but no, but yeah'
res = text.replace('yeah', 'yep') # yep, but no, but yep, but no, but yep

# 对于复杂的模式，请使用 re 模块中的 sub() 函数。
# 为了说明这个，假设你想将形式为 11/27/2012 的日期字符串改成 2012-11-27 。示例如下：

import re
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
res = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)  # Today is 2012-11-27. PyCon starts 2013-3-13.
# sub() 函数中的第一个参数是被匹配的模式，第二个参数是替换模式。反斜杠数字比如 \3 指向前面模式的捕获组号



