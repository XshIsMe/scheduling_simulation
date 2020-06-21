#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import time
from scheduler import Scheduler
from bank_algorithm import bank_algorithm
from config import REFRESH_TIME, TIME_SLICE

class CPU:

    def __init__(self, resource, algorithm, pcb_list):
        # 时间
        self.time = -1
        # 资源
        self.resource = resource
        # 就绪的进程
        self.ready = pcb_list
        # 完成的进程
        self.finish = []
        # 进程调度算法
        self.algorithm = algorithm

    def output(self, now_pcb_name, result):
        '''
        打印进程调度情况
        '''

        #print('\n\n')
        #os.system('pause')

        # 刷新屏幕
        time.sleep(REFRESH_TIME)
        os.system('cls')

        # 打印基本信息
        print('【{algorithm}】NowTime:'.format(algorithm=self.algorithm), self.time)
        print('【{} {}】'.format(now_pcb_name, result))

        text = self.ready[:]
        text.sort(key=lambda x:x.name[-1])
        text += self.finish[:]

        self.resource.print_resource_allocation_table(text)

    def handle_pcb(self):
        '''
        处理PCB
        '''

        # 获取当前PCB
        now_pcb = self.ready[0]

        # 设置PCB状态
        now_pcb.status = '运行'
        for i in range(1, len(self.ready)):
            if '阻塞' != self.ready[i].status:
                self.ready[i].status = '就绪'

        # 运行PCB
        now_pcb.run()
        result = bank_algorithm(self.resource, self.ready)
        if '请求成功' != result:
            now_pcb.status = '阻塞'

        # 判断PCB是否运行完成
        if now_pcb.is_finish():
            now_pcb.status = '完成'
            self.resource.available['A'] += now_pcb.allocation['A']
            self.resource.available['B'] += now_pcb.allocation['B']
            self.resource.available['C'] += now_pcb.allocation['C']
            now_pcb.allocation['A'] = 0
            now_pcb.allocation['B'] = 0
            now_pcb.allocation['C'] = 0
            self.finish.append(self.ready.pop(0))
        
        # 打印进程调度情况
        self.output(now_pcb.name, result)

    def is_finish(self):
        '''
        判断是否已经处理完所有PCB
        :return: 是返回True, 否返回False
        '''

        if 0 < len(self.ready):
            return False
        return True

    def run(self):
        '''
        开始运行CPU
        '''

        # 进程调度器
        scheduler = Scheduler()

        while False == self.is_finish():
            # 一个时间片
            for now_slice in range(TIME_SLICE):
                # 更新时间
                self.time += 1

                # 进行进程调度
                if 0 == now_slice:
                    scheduler.schedule(self.algorithm, self.ready)
                    self.ready = scheduler.get_result()

                # 运行PCB
                self.handle_pcb()