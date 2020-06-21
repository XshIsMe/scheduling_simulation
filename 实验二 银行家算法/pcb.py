#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import random
from bank_algorithm import bank_algorithm

class PCB:
    
    def __init__(self, name):
        # 进程名
        self.name = name
        # 需要的资源总数
        self.max = {
            'A': random.randint(0, 10),
            'B': random.randint(0, 15),
            'C': random.randint(0, 12),
        }
        # 已分配的资源数
        self.allocation = {
            'A': 0,
            'B': 0,
            'C': 0,
        }
        # 请求的资源数
        self.request = {
            'A': 0,
            'B': 0,
            'C': 0,
        }
        # 进程状态（就绪/运行/阻塞/完成）
        self.status = '就绪'

    def run(self):
        # 生成请求
        need = self.get_need()
        self.request['A'] = random.randint(0, need['A'])
        self.request['B'] = random.randint(0, need['B'])
        self.request['C'] = random.randint(0, need['C'])
    
    def get_need(self):
        '''
        获取各类资源的需求数量
        :return: 各类资源需求数量的字典
        '''

        need = {
            'A': self.max['A'] - self.allocation['A'],
            'B': self.max['B'] - self.allocation['B'],
            'C': self.max['C'] - self.allocation['C'],
        }
        return need

    def is_finish(self):
        '''
        是否运行完成
        :return: 是返回True, 否返回False
        '''

        if self.allocation['A'] >= self.max['A']:
            if self.allocation['B'] >= self.max['B']:
                if self.allocation['C'] >= self.max['C']:
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

    # 返回创建好的PCB列表
    return pcb_list