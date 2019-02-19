#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'


import nmap
import time
import urllib
from pysnmp.entity.rfc3413.oneliner import cmdgen

def snmpget(printer_ip):
    cg = cmdgen.CommandGenerator() ##获得CommandGenerator对象
    errorIndication, errorStatus, errorIndex, varBinds = cg.getCmd(
        cmdgen.CommunityData('server', 'public', 1),
        cmdgen.UdpTransportTarget((printer_ip, 161)),
        '.1.3.6.1.2.1.4.20.1.3.127.0.0.1'
    )
    subnet_mask = str(varBinds[0]).split('=')[1].strip()
    return subnet_mask

def Scan(target):
    nm = nmap.PortScanner()
    result = nm.scan(hosts=target, arguments="-sU -p 161 --script=snmp-netstat")
    scan_target = 'http://' + target
    pagehandler = urllib.urlopen(scan_target)
    totle_list = str(result['scan'][target]['udp'][161]['script']['snmp-netstat'])

    try:
        if result['scan'][target]['udp'][161]['script']['snmp-netstat'] :
            f = open('test.txt', 'a+')
            f.write(time.strftime('%Y-%m-%d: %I:%M',time.localtime(time.time())))
            f.write(str(result['scan'][target]['udp'][161]['script']['snmp-netstat']))
            f.close()
    except (IOError, KeyError):
        pass
    pagehandler.close()

    return get_target_list(totle_list)


def get_target_list(totle_list):
    now_addr = ''
    check_ips = []
    flag = 0
    line = ''
    lines = []
    for i in totle_list:
        if i != '\n':
            line = line + i
        else:
            lines.append(line)
            line = ''
    for i in range(len(lines)):
        if lines[i]:
            for j in range(28,45):
                try:
                    now_addr += lines[i][j]
                except IndexError:
                    continue
            check_ips.append(now_addr.split(':')[0])
            now_addr = ''


    return check_ips

def compare(subnet, printer_ip, target_list):
    flag = 1
    target_temp = []
    printer_mask = [0,0,0,0]
    target_mask_list = []
    subnet_mask = subnet.split('.')
    printer = printer_ip.split('.')

    for i in range(4):
        printer_mask[i] = int(printer[i]) & int(subnet_mask[i])

    for i in range(len(target_list)):
        target_mask = target_list[i].split('.')
        for i in range(len(target_mask)):
            try:
                target = int(target_mask[i]) & int(subnet_mask[i])
                target_temp.append(target)
            except (ValueError, IndexError):
                continue
        target_mask_list.append(target_temp)
        target_temp = []

    print(target_mask_list, subnet_mask, printer_mask,target_list)

    for i in range(len(target_mask_list)):
        if printer_mask != target_mask_list[i] and target_list[i]!='*' and target_list[i] != '0.0.0.0':
            print('Warning,target_ip:%s'%target_list[i])
            flag = 0
    if flag == 1:
        print ('Safe')

def main():
    while True:
        printer_ip = '127.0.0.1'
        subnet_mask = snmpget(printer_ip)
        target_list = Scan(printer_ip)
        compare(subnet_mask, printer_ip, target_list)

        time.sleep(300)

if __name__ == '__main__':
    main()
