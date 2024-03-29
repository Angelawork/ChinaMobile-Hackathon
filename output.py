
class Output:
    def __init__(self, path):
        # 初始化方法， 定义输出文件的路径与输出的字符串
        self.path = path
        self.output = ""

    def append(self, content: list):
        # 向输出内容添加一行记录
        self.output += f"{content[0]},{content[1].strftime('%Y-%m-%d %H:%M')},{content[2]}\n"

    def save(self):
        # 保存输出到文件
        self.file = open(self.path, 'w', encoding='utf-8')
        self.file.write("异常账号,异常时间,异常类型\n")  # 写入标题行
        self.file.write(f"{self.output}\n")  # 写入输出内容
        print(f"输出文件已保存至 {self.path}")
        self.file.close()

