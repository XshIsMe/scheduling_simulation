#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import copy
from cpu import CPU
from config import PCB_NUM
from pcb import create_pcb_list
from resource import Resource

def main():
    # 创建PCB列表
    pcb_list = create_pcb_list(PCB_NUM)
    # 创建资源
    resource = Resource()

    # 运行
    cpu_rr = CPU(resource, 'RR', copy.deepcopy(pcb_list))
    cpu_rr.run()

if __name__ == "__main__":
    main()