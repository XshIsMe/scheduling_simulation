#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import copy

def safe(resource, pcb_list):
    work = copy.deepcopy(resource.available)
    finish = [False] * len(pcb_list)

    while False in finish:
        for i in range(len(pcb_list)+1):
            if i == len(pcb_list):
                return False
            if False == finish[i]:
                need = pcb_list[i].get_need()
                if need['A'] <= work['A'] and need['B'] <= work['B'] and need['C'] <= work['C']:
                    work['A'] += pcb_list[i].allocation['A']
                    work['B'] += pcb_list[i].allocation['B']
                    work['C'] += pcb_list[i].allocation['C']
                    finish[i] = True
                    break

    return True


def legitimate(resource, now_pcb):
    '''
    检查请求资源是否可行
    :param now_pcb: 当前PCB
    :param resource: 资源
    :return: 检查结果（1：请求资源大于需求资源，2：请求资源大于可利用资源）
    '''

    # 请求资源数量和需求资源数量
    request = now_pcb.request
    need = now_pcb.get_need()

    # 如果请求资源数量大于需求资源数量
    if (request['A'] > need['A']) or (request['B'] > need['B']) or (request['C'] > need['C']):
        return False
    # 如果请求资源数量大于可利用资源数量
    elif (request['A'] > resource.available['A']) or (request['B'] > resource.available['B']) or (request['C'] > resource.available['C']):
        return False
    return True

def bank_algorithm(resource, pcb_list):
    '''
    银行家算法
    :param now_pcb: 当前PCB
    :param resource: 资源
    '''

    now_pcb = pcb_list[0]

    # 检查请求是否合法
    if legitimate(resource, now_pcb):
        # 试探性分配
        now_pcb.allocation['A'] += now_pcb.request['A']
        now_pcb.allocation['B'] += now_pcb.request['B']
        now_pcb.allocation['C'] += now_pcb.request['C']
        resource.available['A'] -= now_pcb.request['A']
        resource.available['B'] -= now_pcb.request['B']
        resource.available['C'] -= now_pcb.request['C']
        # 安全性检查
        if safe(resource, pcb_list):
            return '请求成功'
        else:
            now_pcb.allocation['A'] -= now_pcb.request['A']
            now_pcb.allocation['B'] -= now_pcb.request['B']
            now_pcb.allocation['C'] -= now_pcb.request['C']
            resource.available['A'] += now_pcb.request['A']
            resource.available['B'] += now_pcb.request['B']
            resource.available['C'] += now_pcb.request['C']
            return '安全性检查不通过'
    else:
        return '请求不合法'