# 问题
# 你想去掉文本字符串开头，结尾或者中间不想要的字符，比如空白。

# 解决方案
# strip() 方法能用于删除开始或结尾的字符。 lstrip() 和 rstrip() 分别从左和从右执行删除操作。
# 默认情况下，这些方法会去除空白字符，但是你也可以指定其他字符
s = ' hello world \n'
s.strip() # 'hello world'

s.lstrip() # 'hello world \n'

s.rstrip() # ' hello world'

t = '-----hello====='
t.lstrip('-') # 'hello====='

t.strip('-=') # 'hello'

# 讨论
# 这些 strip() 方法在读取和清理数据以备后续处理的时候是经常会被用到的。 比如，你可以用它们来去掉空格，引号和完成其他任务

# 如果你想处理中间的空格，那么你需要求助其他技术。比如使用 replace() 方法或者是用正则表达式替换

s.replace(' ', '') # 'helloworld