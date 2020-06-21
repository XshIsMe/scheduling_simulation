#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import random

def init():
    global startTrack
    startTrack = 100
    global processNum
    processNum = 10

def createProcess():
    global processList
    processList = [0]*processNum
    for i in range(processNum):
        processList[i] = random.randint(1, 200)

def output(resultList):
    # 平均寻道长度
    avgDistance = 0
    # 头部
    print('+-----------------------------+')
    print('|     （从{}号磁道开始）     |'.format(startTrack))
    print('+--------------+--------------+')
    print('|   被访问的   |   移动距离   |')
    print('| 下一个磁道号 |  （磁道数）  |')
    print('+-----------------------------+')
    # 内容
    for i in range(processNum):
        # 被访问的下一个磁道号
        nextTrack = resultList[i]['nextTrack']
        # 移动距离（磁道数）
        distance = resultList[i]['distance']
        # 打印
        print('| {:^12} | {:^12} |'.format(str(nextTrack), str(distance)))
        print('+--------------+--------------+')
        # 平均寻道长度
        avgDistance += distance
    # 尾部
    avgDistance /= processNum
    avgDistance = round(avgDistance, 2)
    print('|     平均寻道长度: {:5}     |'.format(avgDistance))
    print('+-----------------------------+')

def FCFS():
    resultList = list()
    nowTrack = startTrack
    for i in range(processNum):
        # 被访问的下一个磁道号
        nextTrack = processList[i]
        # 移动距离（磁道数）
        distance = abs(nowTrack-nextTrack)
        # 保存结果
        resultList.append({
            'nextTrack': nextTrack,
            'distance': distance,
        })
        # 更新磁道号
        nowTrack = nextTrack
    output(resultList)

def SSTF():
    resultList = list()
    nowTrack = startTrack
    wait = processList
    while 0 < len(wait):
        # 找到距离当前磁头最近的磁道
        minDistanceIndex = 0
        for i in range(len(wait)):
            nowDistance = abs(nowTrack-processList[i])
            minDistance = abs(nowTrack-processList[minDistanceIndex])
            if nowDistance < minDistance:
                minDistanceIndex = i
        # 被访问的下一个磁道号
        nextTrack = processList[minDistanceIndex]
        # 移动距离（磁道数）
        distance = abs(nowTrack-nextTrack)
        # 保存结果
        resultList.append({
            'nextTrack': nextTrack,
            'distance': distance,
        })
        # 更新磁道号
        nowTrack = nextTrack
        # 移出当前进程
        wait.pop(minDistanceIndex)
    output(resultList)

def SCAN():
    resultList = list()
    nowTrack = startTrack

    waitSmall = list()
    waitBig = list()
    wait = processList
    wait.sort()
    for i in range(processNum):
        if processList[i] > nowTrack:
            waitBig = wait[i:]
            waitSmall = list(reversed(wait[0:i]))
            break
    
    for i in range(len(waitBig)):
        # 被访问的下一个磁道号
        nextTrack = waitBig[i]
        # 移动距离（磁道数）
        distance = abs(nowTrack-nextTrack)
        # 保存结果
        resultList.append({
            'nextTrack': nextTrack,
            'distance': distance,
        })
        # 更新磁道号
        nowTrack = nextTrack
    
    for i in range(len(waitSmall)):
        # 被访问的下一个磁道号
        nextTrack = waitSmall[i]
        # 移动距离（磁道数）
        distance = abs(nowTrack-nextTrack)
        # 保存结果
        resultList.append({
            'nextTrack': nextTrack,
            'distance': distance,
        })
        # 更新磁道号
        nowTrack = nextTrack
    
    output(resultList)

def CSCAN():
    resultList = list()
    nowTrack = startTrack

    waitSmall = list()
    waitBig = list()
    wait = processList
    wait.sort()
    for i in range(processNum):
        if processList[i] > nowTrack:
            waitBig = wait[i:]
            waitSmall = wait[0:i]
            break
    
    for i in range(len(waitBig)):
        # 被访问的下一个磁道号
        nextTrack = waitBig[i]
        # 移动距离（磁道数）
        distance = abs(nowTrack-nextTrack)
        # 保存结果
        resultList.append({
            'nextTrack': nextTrack,
            'distance': distance,
        })
        # 更新磁道号
        nowTrack = nextTrack
    
    for i in range(len(waitSmall)):
        # 被访问的下一个磁道号
        nextTrack = waitSmall[i]
        # 移动距离（磁道数）
        distance = abs(nowTrack-nextTrack)
        # 保存结果
        resultList.append({
            'nextTrack': nextTrack,
            'distance': distance,
        })
        # 更新磁道号
        nowTrack = nextTrack
    
    output(resultList)

def main():
    init()
    createProcess()
    #FCFS()
    #SSTF()
    #SCAN()
    CSCAN()

if __name__ == "__main__":
    main()