import json

# 输入文件路径
input_path = 'picked_baseline.json'

# 读取 JSON 数据
with open(input_path, 'r') as file:
    data = json.load(file)

# 删除每个视频中每个问题的 'tag' 字段
for video_id, questions in data.items():
    for question in questions:
        if 'tag' in question:
            del question['tag']

# 覆盖原文件，将更新后的数据写回
with open(input_path, 'w') as file:
    json.dump(data, file)

print("已从所有问题中删除 'tag' 字段并覆盖保存！")
