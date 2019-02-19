#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'

import os


def pid():
    """
    方法从系统中获取pid
    方法返回pid
    """
    # try:
    #     pid = data.get('python_run_id')
    #     os.kill(int(pid),signal.SIGTERM)
    # except Exception as e:
    #     # py_log.log('killpid ',e )
    #     print('fdfd')
    pid = os.getpid()
    return pid

import psutil
import re
import signal

# if __name__ == "__main__":
#     for proc in psutil.process_iter():
#         print("pid-%d,name:%s" % (proc.pid, proc.name()))
#         if str(proc.name) == 'python.exe':
#             print("->pid-%d,name:%s" % (proc.pid, proc.name()))
#             break


pids = psutil.pids()
# for pid in pids:
#     p = psutil.Process(pid)
#     get process name according to pid
    # process_name = p.name()
    #
    # print("Process name is: %s, pid is: %s" %(process_name, pid))

print("----------------------------- kill specific process --------------------------------")
pids = psutil.pids()
for pid in pids:
    p = psutil.Process(pid)
    # get process name according to pid
    process_name = p.name()
    # kill process "sleep_test1"
    if 'python.exe' == process_name:
        print("kill specific process: name(%s)-pid(%s)" %(process_name, pid))
        # print(p)
