#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class Memory:

    def __init__(self, address, size):
        self.address = address
        self.size = size

class JCB:

    def __init__(self, name, operation, requestSize):
        self.name = name
        self.operation = operation
        self.requestSize = requestSize

def init():
    # 初始状态下，可用内存空间
    global INITIAL_SIZE
    INITIAL_SIZE  = 640
    # 最小分区大小
    global SIZE
    SIZE = 0
    # 空闲内存链
    global memoryList
    memoryList = initMemoryList()
    # 被占用内存链
    global busyMemoryList
    busyMemoryList = dict()
    # 作业队列
    global jcbQueue
    jcbQueue = initJcbQueue()
    # 当前JCP指针
    global nowJcb
    nowJcb = None

def initMemoryList():
    memoryList = list()
    memory = Memory(0, INITIAL_SIZE)
    memoryList.append(memory)
    return memoryList

def initJcbQueue():
    jcbQueue = list()
    jcbQueue.append(JCB('作业1', '申请', 130))
    jcbQueue.append(JCB('作业2', '申请', 60))
    jcbQueue.append(JCB('作业3', '申请', 100))
    jcbQueue.append(JCB('作业2', '释放', 60))
    jcbQueue.append(JCB('作业4', '申请', 200))
    jcbQueue.append(JCB('作业3', '释放', 100))
    jcbQueue.append(JCB('作业1', '释放', 130))
    jcbQueue.append(JCB('作业5', '申请', 140))
    jcbQueue.append(JCB('作业6', '申请', 60))
    jcbQueue.append(JCB('作业7', '申请', 50))
    jcbQueue.append(JCB('作业8', '申请', 60))
    return jcbQueue

def firstFit():
    for i in range(len(memoryList)):
        nowMemory = memoryList[i]
        if nowMemory.size > nowJcb.requestSize:
            if nowMemory.size - nowJcb.requestSize <= SIZE:
                busyMemoryList[nowJcb.name] = nowMemory.address
                memoryList.pop(i)
            else:
                busyMemoryList[nowJcb.name] = nowMemory.address
                nowMemory.address += nowJcb.requestSize
                nowMemory.size -= nowJcb.requestSize
            return True
    return False

def bestFit():
    memoryList.sort(key=lambda x: x.size)
    return firstFit()

def reclaimMemory():
    address = busyMemoryList[nowJcb.name]
    for i in range(len(memoryList)):
        if memoryList[i].address > address or 0 == memoryList[i].size:
            if(
                # 与前一个临接
                0 != i and
                address == memoryList[i-1].address + memoryList[i-1].size and
                # 且与后一个临接
                len(memoryList)-1 != i and
                address + nowJcb.requestSize == memoryList[i].address
            ):
                memoryList[i-1].size = memoryList[i].address + memoryList[i].size - memoryList[i-1].address
                memoryList.pop(i)
            elif(
                # 与前一个临接
                0 != i and
                address == memoryList[i-1].address + memoryList[i-1].size
            ):
                memoryList[i-1].size += nowJcb.requestSize
            elif(
                # 与后一个临接
                len(memoryList)-1 != i and
                address + nowJcb.requestSize == memoryList[i].address
            ):
                memoryList[i].address = address
                memoryList[i].size += nowJcb.requestSize
            else:
                memory = Memory(address, nowJcb.requestSize)
                memoryList.insert(i, memory)
            break

def printMemory():
    for memory in memoryList:
        print('[Address: {}, Size: {}] →'.format(
            memory.address,
            memory.size,
        ), end=' ')
    print('Null')

def main():
    init()

    global nowJcb

    while 0 < len(jcbQueue):
        nowJcb = jcbQueue.pop(0)
        print('\n' + nowJcb.name, nowJcb.operation, str(nowJcb.requestSize) + 'KB')
        if '申请' == nowJcb.operation:
            print('分配前: ', end='')
            printMemory()
            if True == bestFit():
            #if True == firstFit():
                print('分配成功，地址为：' + str(busyMemoryList[nowJcb.name]))
            else:
                print('分配失败')
            print('分配后: ', end='')
            printMemory()
        elif '释放' == nowJcb.operation:
            print('释放前: ', end='')
            printMemory()
            reclaimMemory()
            print('释放后: ', end='')
            printMemory()

if __name__ == "__main__":
    main()