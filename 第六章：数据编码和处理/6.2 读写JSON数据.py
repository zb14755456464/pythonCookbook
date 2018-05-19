import json

data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}
#  一个Python数据结构转换为JSON
json_str = json.dumps(data) # json的格式就是一个字符串

# 下面演示如何将一个JSON编码的字符串转换回一个Python数据结构：
data = json.loads(json_str) # 这个就会转换成字典

# 如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。例如：

# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f) # 已json的格式存储到文件中

# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)  # 从文件中读取文件中的json内容

