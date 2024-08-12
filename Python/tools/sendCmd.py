import subprocess

def execute_commands_from_file(file_path):
    try:
        # 打开并读取文件
        with open(file_path, 'r') as file:
            for line in file:
                command = line.strip()  # 去除行首尾的空白字符
                if command:
                    print(f"执行命令: {command}")
                    
                    # 执行命令并获取结果
                    result = subprocess.run(command, shell=True, text=True, capture_output=True)
                    
                    # 输出执行结果
                    print(f"标准输出:\n{result.stdout}")
                    print(f"标准错误:\n{result.stderr}")
                    
                    if result.returncode != 0:
                        print(f"命令失败，退出代码: {result.returncode}")
                        break
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在,已创建，请加入命令！")
        # 创建文件
        with open(file_path, 'w') as file:
            file.write("")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    # 指定命令文件路径
    file_path = 'commands.txt'  # 替换为你的文件路径
    execute_commands_from_file(file_path)
