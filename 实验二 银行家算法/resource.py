#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class Resource:

    def __init__(self):
        # 资源数量
        self.available = {
            'A': 10,
            'B': 15,
            'C': 12,
        }

    def print_resource_allocation_table(self, pcb_list):
        head = '''\
+-------+-------------+-------------+-------------+-------------+-------------+--------+
|       |     Max     |  Allocation |    Need     |  Available  |   Request   | Status |
+       +-------------+-------------+-------------+-------------+-------------+--------+
|       |  A   B   C  |  A   B   C  |  A   B   C  |  A   B   C  |  A   B   C  |        |
+-------+-------------+-------------+-------------+-------------+-------------+--------+
'''

        prepare_body = '''\
| {:^3} | {:^3} {:^3} {:^3} | {:^3} {:^3} {:^3} | {:^3} {:^3} {:^3} | {:^3} {:^3} {:^3} | {:^3} {:^3} {:^3} |  {:^2}  |
+-------+-------------+-------------+-------------+-------------+-------------+--------+
'''

        output = head

        for pcb in pcb_list:
            output += prepare_body.format(
                pcb.name,
                pcb.max['A'],
                pcb.max['B'],
                pcb.max['C'],
                pcb.allocation['A'],
                pcb.allocation['B'],
                pcb.allocation['C'],
                pcb.get_need()['A'],
                pcb.get_need()['B'],
                pcb.get_need()['C'],
                self.available['A'],
                self.available['B'],
                self.available['C'],
                pcb.request['A'],
                pcb.request['B'],
                pcb.request['C'],
                pcb.status,
            )

        print(output)