import os
import json
import subprocess

def run_packaging():
    # 读取packer_config.json文件
    with open('source_files/packer_config.json', 'r') as f:
        config = json.load(f)
    
    # 获取要打包的内容或路径
    content = config.get('content')
    # 获取打包结果的输出路径
    output_path = config.get('output_path')
    
    # 执行打包操作
    # 根据您的需求自行编写打包逻辑，这里只是一个示例
    command = f'your_packaging_command {content} {output_path}'
    subprocess.run(command, shell=True, check=True)

if __name__ == '__main__':
    run_packaging()
