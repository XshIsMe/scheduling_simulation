#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class Scheduler:

    def schedule_by_sjf(self):
        '''
        短进程优先
        '''

        self.pcb_list.sort(key=lambda x:x.need_time)

    def schedule_by_rr(self):
        '''
        时间片轮转
        '''

        self.pcb_list.append(self.pcb_list.pop(0))

    def schedule_by_hrrn(self):
        '''
        高响应比优先
        '''

        self.pcb_list.sort(key=lambda x:x.priority_number, reverse=True)

    def schedule(self, algorithm, pcb_list):
        '''
        进程调度
        :param algorithm: 进程调度算法
        :param pcb_list: PCB列表
        '''

        self.pcb_list = pcb_list
        if 'SJF' == algorithm:
            self.schedule_by_sjf()
        elif 'RR' == algorithm:
            self.schedule_by_rr()
        elif 'HRRN' == algorithm:
            self.schedule_by_hrrn()
        
    def get_result(self):
        '''
        获取进程调度结果
        :return: 调度后的PCB列表
        '''

        return self.pcb_list