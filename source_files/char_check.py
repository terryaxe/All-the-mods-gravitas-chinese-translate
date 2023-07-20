import os
import re

# 定义需要替换的标点符号
PUNCTUATIONS = {
    ',': '，',
    '.': '。',
    ';': '；',
    '?': '？',
    '!': '！',
    '(': '（',
    ')': '）',
    '[': '【',
    ']': '】',
    '{': '｛',
    '}': '｝',
    '<': '《',
    '>': '》',
    '/': '／',
    '\\': '＼',
    '|': '｜',
}

# 定义需要检查的文件类型
FILE_TYPES = ['.json']

# 定义检查文件的函数
def check_file(file_path):
    # 获取文件扩展名
    _, ext = os.path.splitext(file_path)
    # 判断文件类型是否需要检查
    if ext not in FILE_TYPES:
        return
    # 打开文件，读取内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # 遍历标点符号字典，进行替换
    for p, c in PUNCTUATIONS.items():
        # 对于 json 文件，只替换冒号后面的标点符号
        if ext == '.json':
            content = re.sub(f'(?<=[^"\':\u4e00-\u9fa5]){re.escape(p)}(?=[^"\':\u4e00-\u9fa5])', c, content)
        # 对于其他文件，替换所有标点符号
        else:
            content = re.sub(f'(?<=[^\u4e00-\u9fa5]){re.escape(p)}(?=[^\u4e00-\u9fa5])', c, content)
    # 将替换后的内容写入文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 遍历当前目录下的所有文件，进行检查
for root, dirs, files in os.walk('.'):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        check_file(file_path)
