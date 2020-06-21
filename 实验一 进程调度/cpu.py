#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import time
from pcb import print_pcb_list
from scheduler import Scheduler
from config import REFRESH_TIME, TIME_SLICE


class CPU:

    def __init__(self, algorithm, pcb_list):
        # 时间
        self.time = -1
        # 等待插入的进程
        self.wait = pcb_list
        # 就绪的进程
        self.ready = []
        # 完成的进程
        self.finish = []
        # 进程调度算法
        self.algorithm = algorithm

    def calc_avg_turnaround_time(self):
        '''
        计算平均周转时间（周转时间 = 完成时间 - 到达时间）
        :return: 平均周转时间
        '''

        sum_turnaround_time = 0
        for pcb in self.finish:
            turnaround_time = pcb.end_time - pcb.arrival_time
            sum_turnaround_time += turnaround_time
        avg_turnaround_time = int(sum_turnaround_time / len(self.finish))

        return avg_turnaround_time

    def output(self):
        '''
        打印进程调度情况
        '''

        # print('\n\n')
        # os.system('pause')

        # 刷新屏幕
        time.sleep(REFRESH_TIME)
        os.system('cls')

        # 打印基本信息
        print('【{algorithm}】NowTime:'.format(
            algorithm=self.algorithm), self.time)

        # 打印PCB列表
        output_pcb_list = list()
        output_pcb_list += self.ready[:]
        output_pcb_list.sort(key=lambda x: x.arrival_time)
        output_pcb_list += self.finish[:]
        print_pcb_list(output_pcb_list)

    def handle_pcb(self):
        '''
        处理PCB
        '''

        # 获取当前PCB
        now_pcb = self.ready[0]

        # 设置PCB状态
        now_pcb.status = '运行'
        for i in range(1, len(self.ready)):
            self.ready[i].status = '就绪'

        # 如果是第一次运行，设置开始运行时间
        if now_pcb.is_first():
            now_pcb.start_time = self.time

        # 运行PCB
        now_pcb.run()

        # 判断PCB是否运行完成
        if now_pcb.is_finish():
            now_pcb.status = '完成'
            now_pcb.end_time = self.time
            self.finish.append(self.ready.pop(0))

        # 更新优先数
        for i in range(len(self.ready)):
            self.ready[i].update_priority(self.time)

    def add_new_pcb_to_ready(self):
        '''
        判断是否有新PCB加入
        '''

        if 0 < len(self.wait):
            if self.time >= self.wait[0].arrival_time:
                self.wait[0].status = '就绪'
                self.ready.append(self.wait.pop(0))

    def is_finish(self):
        '''
        判断是否已经处理完所有PCB
        :return: 是返回True, 否返回False
        '''

        if 0 < len(self.wait) or 0 < len(self.ready):
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

                # 判断是否有新PCB加入
                self.add_new_pcb_to_ready()

                if 0 < len(self.ready):
                    # 进行进程调度
                    if 0 == now_slice:
                        scheduler.schedule(self.algorithm, self.ready)
                        self.ready = scheduler.get_result()

                    # 运行PCB
                    self.handle_pcb()

                # 打印进程调度情况
                self.output()

        return self.calc_avg_turnaround_time()
