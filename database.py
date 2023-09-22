class Database:
  def __init__(self, account):
    self.account = account
    self.operations = {"time": [], "action": [], "ip": []}
    # 记录每个新分钟的第一个元素的index
    self.time_index = [0]

  def sort_time(self):
    # 对操作记录按时间排序
    self.operations = sorted(zip(self.operations['time'], self.operations['action'], self.operations['ip']))

    curr = self.operations[0][0]
    for o in range(len(self.operations)):
      if self.operations[o][0] != curr:
        self.time_index.append(o)
        curr = self.operations[o][0]

  def add_entry(self, time, action, ip):
    # 添加新的操作记录
    self.operations["time"].append(time)
    self.operations["action"].append(action)
    self.operations["ip"].append(ip)

  # 用于测试,显示database object中含有的内容
  def print_entries(self):
    for entry in self.operations:
      time, action, ip = entry
      print(f"Time: {time}, Action: {action}, IP: {ip}")
    print(f"time_index: {self.time_index}")