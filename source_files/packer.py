import json
import shutil

# 读取配置文件
with open('source_files/packer_config.json', 'r') as f:
    config = json.load(f)

# 打包逻辑
def package_files(paths, target_dir):
    for path in paths:
        shutil.make_archive(target_dir, 'zip', path)

# 调用打包函数
package_files(config['paths'], 'target_folder')
