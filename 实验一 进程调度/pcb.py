#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import random

class PCB:
    
    def __init__(self, name):
        # 进程名
        self.name = name
        # 优先数（响应比）
        self.priority_number = 1
        # 到达时间
        self.arrival_time = random.randint(3, 100)
        # 需要运行时间（进程的长度）
        self.need_time = random.randint(3, 100)
        # 开始运行时间
        self.start_time = -1
        # 已运行时间
        self.run_time = -1
        # 完成时间
        self.end_time = -1
        # 进程状态（未到/就绪/运行/完成）
        self.status = '未到'

    def run(self):
        '''
        更新运行时间
        '''

        self.run_time += 1

    def update_priority(self, now_time):
        '''
        优先数 = (等待时间 + 要求服务时间) / 要求服务时间
        :param now_time: 当前时间
        '''

        wait_time = now_time - self.arrival_time
        priority_number = (wait_time + self.need_time) / self.need_time
        self.priority_number = int(100*priority_number)

    def is_first(self):
        '''
        是否是第一次运行
        :return: 是返回True, 否返回False
        '''

        if -1 == self.start_time:
            return True
        return False

    def is_finish(self):
        '''
        是否运行完成
        :return: 是返回True, 否返回False
        '''

        if self.run_time >= self.need_time:
            return True
        return False

def create_pcb_list(num=5):
    '''
    生成一个PCB列表
    :param num: PCB的数量
    :return: PCB列表
    '''

    # 数量必须大于等于1
    if 1 > num:
        return False

    # 初始化PCB列表
    pcb_list = list()
    tmp_pcb = PCB('PCB_0')
    tmp_pcb.arrival_time = 0
    pcb_list.append(tmp_pcb)

    # 循环创建PCB
    for i in range(1, num):
        tmp_pcb = PCB('PCB_' + str(i))
        pcb_list.append(tmp_pcb)

    # 根据到达时间排序
    pcb_list.sort(key=lambda x:x.arrival_time)

    # 返回创建好的PCB列表
    return pcb_list

def print_pcb_list(pcb_list):
    '''
    打印PCB列表
    :param pcb_list: PCB列表
    '''

    # 打印表格头
    print('+--------+--------+----------+--------------+--------------+------------+----------+----------+')
    print('| 进程名 | 优先数 | 到达时间 | 需要运行时间 | 开始运行时间 | 已运行时间 | 完成时间 | 进程状态 |')
    print('+--------+--------+----------+--------------+--------------+------------+----------+----------+')

    # 打印PCB
    for pcb in pcb_list:
        print('| {:^6} | {:^6} | {:^8} | {:^12} | {:^12} | {:^10} | {:^8} | {:^6} |'.format(
            pcb.name,
            pcb.priority_number,
            pcb.arrival_time,
            pcb.need_time,
            pcb.start_time,
            pcb.run_time,
            pcb.end_time,
            pcb.status,
        ))
        print('+--------+--------+----------+--------------+--------------+------------+----------+----------+')