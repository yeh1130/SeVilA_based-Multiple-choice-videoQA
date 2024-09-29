import json

# 输入文件路径
input_path = 'picked_baseline.json'

# 读取 JSON 数据
with open(input_path, 'r') as file:
    data = json.load(file)

# 覆盖原文件，将数据以单行格式写回
with open(input_path, 'w') as file:
    json.dump(data, file)

print("数据已更新为单行格式并覆盖保存！")
