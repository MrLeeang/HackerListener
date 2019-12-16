#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time         : 2019/11/18 15:51
# @Author       : Li Hongwei
# @Email        : lihongwei@integritytech.com.cn
# @File         : main.py
# @Software     : PyCharm

import subprocess, time


def poll_tcpdump(device):
    cmd = ["tcpdump", "-n", "-e", "-vvv"]
    if device:
        cmd.append("-i")
        cmd.append(device)

    p = subprocess.Popen(" ".join(cmd), shell=True, stdout=subprocess.PIPE)
    return p


def read_tcpdump(p, attack=True):
    while True:
        line = p.stdout.readline()
        line = line.strip()
        if not line:
            time.sleep(0.5)
        if attack:
            attack_message(line)
        else:
            defense_message(line)


def attack_message(message):
    print(message)


def defense_message(message):
    print(message)


if __name__ == "__main__":
    # 攻击
    ap = poll_tcpdump("eth1")
    read_tcpdump(ap)
    # 防守
    dp = poll_tcpdump("eth2")
    read_tcpdump(dp, attack=False)
    pass
