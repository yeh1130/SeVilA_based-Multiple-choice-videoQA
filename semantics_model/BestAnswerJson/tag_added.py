import json

# 读取原始的 base.json 文件
with open('ori_vis32.json', 'r', encoding='utf-8') as file:
    base_data = json.load(file)

# 读取包含 tag 的 mc_question_test.json 文件
with open('mc_question_test.json', 'r', encoding='utf-8') as file:
    mc_data = json.load(file)

# 为 base.json 中的每个问题添加 tag
for video_id, questions in base_data.items():
    if video_id in mc_data:
        for question in questions:
            # 查找对应的 tag
            mc_questions = mc_data[video_id]['mc_question']
            for mc_question in mc_questions:
                if mc_question['id'] == question['id']:
                    question['tag'] = mc_question.get('tag', [])

# 将更新后的数据保存到新的 JSON 文件中，不使用缩进
with open('ori_vis32_updated.json', 'w', encoding='utf-8') as file:
    json.dump(base_data, file, ensure_ascii=False)

print("Tags have been successfully added to base.json and saved to base_updated.json.")
