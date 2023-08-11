#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
import pytest
import platform

from common import project_dir
from common.config_parser import ReadConfig


def local_run(app_name):
    env = ReadConfig().get_env
    # args = [app_name + "/case/", "--alluredir",
    #         project_dir + "/report/raw_data/"]
    args = [app_name + "/case/test_mvp_notification_message.py", "-m D", "--alluredir",
            project_dir + "/report/raw_data/"]
    pytest.main(args)


def generate_report():
    report_path = os.path.join(project_dir, "report",
                               "html_report_" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())))
    os.system("allure generate " + project_dir + "/report/raw_data/ -o " + report_path)
    return report_path


def open_report(report_path):
    # windows TODO 判断平台在linux会出错
    os.system("allure open %s -p 2022" % report_path)
    # linux
    # os.system("nohup allure open %s -p 2022 &" % report_path)


if __name__ == "__main__":
    app_list = ReadConfig().pkg_config_path
    report_list = []
    for app_name in app_list:
        platform = ReadConfig().get_platform(app_name)
        local_run(app_name)
        report_path = generate_report()
        print("report location: %s" % report_path)
        report_list.append(report_path)
    [open_report(i) for i in report_list]
