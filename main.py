#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import subprocess
import time

subprocess.Popen(["python3", "run.py"]).wait()
ret = os.popen("lsof -i:2022 |grep -i java| awk  '{print $2}'")
if ret.readlines():
    kill_cmd = "lsof -i:2022 |grep -i java| awk  '{print $2}'  | xargs kill -9"
    print("kill cmd: %s" % kill_cmd)
    os.system(kill_cmd)
time.sleep(2)
report_path = os.path.join(os.getcwd(), "report")
file_name = [i for i in os.listdir(report_path) if "html_report" in i]
flag = 1 if file_name else 0
if flag:
    report_name = os.path.join(report_path, file_name[0])
    os.system("sudo xauth add $(xauth -f ~xjsd3/.Xauthority list|tail -1)")
    time.sleep(3)
    # run_cmd = "nohup allure open %s -p 2022 &" % report_name
    run_cmd = "sh /home/chuanwen/glass_ui/test.sh %s" % report_name
    print("run cmd: %s" % run_cmd)
    os.system(run_cmd)
    time.sleep(2)
    while not ret.readlines():
        time.sleep(2)
        os.system(run_cmd)
        ret = os.popen("lsof -i:2022 |grep -i java| awk  '{print $2}'")
