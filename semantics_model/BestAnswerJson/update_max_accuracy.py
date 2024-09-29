import json


def load_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def load_tag_to_file_mapping(filepath):
    tag_to_file = {}
    with open(filepath, 'r') as file:
        for line in file:
            if ': ' in line:
                tag, filename = line.strip().split(': ')
                tag_to_file[tag.strip()] = filename.strip()
    return tag_to_file


def update_questions(baseline_data, tag_to_file):
    for video_id, questions in baseline_data.items():
        for question in questions:
            tags = question['tag']
            for tag in tags:
                if tag in tag_to_file:
                    filename = tag_to_file[tag] + '.json'
                    data = load_json_file(filename)
                    if video_id in data:  # 确保正确的视频ID存在于数据中
                        video_data = data[video_id]
                        for item in video_data:
                            if item['id'] == question['id']:
                                question.update(item)
        print(f"完成更新视频 {video_id}")  # 每完成一个视频ID的更新后打印
    return baseline_data


# 主逻辑
if __name__ == "__main__":
    baseline_path = 'picked_baseline.json'
    mapping_path = 'max_rates_output.txt'

    baseline_data = load_json_file(baseline_path)
    tag_to_file = load_tag_to_file_mapping(mapping_path)

    updated_data = update_questions(baseline_data, tag_to_file)

    # 将更新后的数据写回到 picked_baseline.json
    with open(baseline_path, 'w') as file:
        json.dump(updated_data, file, indent=4)

    print("所有数据更新完毕！")
