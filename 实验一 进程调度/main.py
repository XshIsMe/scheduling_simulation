#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import copy
from cpu import CPU
from config import PCB_NUM
from pcb import create_pcb_list

def main():
    # 创建PCB列表
    pcb_list = create_pcb_list(PCB_NUM)

    # 运行
    cpu_sjf = CPU('SJF', copy.deepcopy(pcb_list))
    sjf_avg_turnaround_time = cpu_sjf.run()
    cpu_rr = CPU('RR', copy.deepcopy(pcb_list))
    rr_avg_turnaround_time = cpu_rr.run()
    cpu_hrrn = CPU('HRRN', copy.deepcopy(pcb_list))
    hrrn_avg_turnaround_time = cpu_hrrn.run()

    print('\n\n')
    print('平均周转时间：')
    print(' SJF:', sjf_avg_turnaround_time)
    print('  RR:', rr_avg_turnaround_time)
    print('HRRN:', hrrn_avg_turnaround_time)
    print('\n\n')

if __name__ == "__main__":
    main()