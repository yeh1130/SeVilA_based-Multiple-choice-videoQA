import json

# 读取原始JSON文件
with open('baseline.json', 'r') as file:
    data = json.load(file)

# 提取所需数据
picked_data = {}
for video_id, entries in data.items():
    picked_data[video_id] = [{
        "id": entry["id"],
        "answer_id": entry["answer_id"],
        "tag": entry["tag"]
    } for entry in entries]

# 保存提取的数据到新的JSON文件
with open('picked_baseline.json', 'w') as file:
    json.dump(picked_data, file, indent=4)

print("数据提取并保存成功！")
