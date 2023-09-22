import csv
import tools
from database import *
from algorithm import singly_linked_list

from collections import defaultdict

# 创建一个 defaultdict 用于按照类别分组数据
grouped_data = defaultdict(list)

def main(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        # 跳过第一行标题行
        next(csv_reader)

        for row in csv_reader:
            category = row[2]
            grouped_data[category].append(row)

    # 创建一个单链表 data_list
    data_list = singly_linked_list.LinkedList()

    # 遍历分组数据并创建数据库对象
    for category, group in grouped_data.items():
        curr_database = Database(group[0][2])  # 使用组内第一个元素创建数据库对象
        for row in group:
            curr_action = tools.clean_access(row[4])
            curr_date = tools.convert_time(row[0])
            curr_ip = row[5]

            curr_database.add_entry(curr_date, curr_action, curr_ip)

        curr_database.sort_time()  # 对数据库对象排序
        data_list.insert_tail(curr_database)  # 将数据库对象添加到单链表尾部

    # 用于测试的代码，打印数据
    '''for node in data_list:
        node.print_entries()'''
    # 返回单链表
    return data_list

