#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
import os
import subprocess
import time
import uuid

import allure
import pytest
import uiautomator2 as u2
import wda

from common import project_dir
from common.config_parser import ReadConfig
from common.utils import get_installed_package_name
from common.adb_tool import AdbTools


@pytest.fixture(scope="package")
def driver(request):
    global platform, package_name, app_name, devices
    app_name = request.param.get("app_name")
    platform = ReadConfig().get_platform(app_name)
    package_name = get_installed_package_name(app_name)
    if isinstance(package_name, dict):
        package_name = package_name[request.param.get("devices")]
    else:
        package_name = package_name
    if platform == "android":
        devices = request.param.get("devices")
        driver = u2.connect(devices)  # 连接设备(usb只能插入单个设备)
        # driver.service("uiautomator").start()
        # driver.set_fastinput_ime(True)  # 启用自动化定制的输入法
        driver.settings["operation_delay"] = (0.2, 0.2)  # 操作后的延迟，(0, 0)表示操作前等待0s，操作后等待0s
        driver.settings['operation_delay_methods'] = ['click', 'swipe', 'drag', 'press']
        driver.implicitly_wait(ReadConfig().get_implicitly_wait(app_name))  # 设置隐式等待时间，默认20s
        # driver.unlock()  # 解锁
        if not driver.info['screenOn']:
            driver.press("power")
            driver.swipe(0.3, 0.9, 0.9, 0.1)
            # TODO 源码无以下这行，原因是手机滑动之后会有延迟，需增加超时机制
            time.sleep(1)  # 解锁
        os.system('adb -s %s root' % devices)
        screen_off_timeout = os.popen('adb -s %s shell settings get system screen_off_timeout' % devices).read().strip()
        if screen_off_timeout != '1800000':
            os.system('adb -s %s shell settings put system screen_off_timeout 1800000' % devices)
        with driver.watch_context(builtin=True) as ctx:
            ctx.when("^(下载|更新)").when("取消").click()  # 当同时出现（下载 或 更新）和 取消 按钮时，点击取消
            ctx.when("跳过%").click()
            # ctx.when("%允许%").click()
            # ctx.when("允许").click()
            ctx.when("继续").click()
            ctx.when("每次开启").click()
            ctx.when("创建").when("取消").click()
            ctx.when("恢复").when("取消").click()
            for element in ReadConfig().get_popup_elements(app_name):
                ctx.when(element).click()
            ctx.wait_stable(seconds=1.5)  # 开启弹窗监控，并等待界面稳定（两个弹窗检查周期内没有弹窗代表稳定）
            yield driver
            driver.set_fastinput_ime(False)  # 关闭自动化定制的输入法
            # driver.app_stop_all()  # 停止所有应用
            driver.press("home")
            os.system('adb -s %s shell settings put system screen_off_timeout %s' % (devices, screen_off_timeout))
            driver.screen_off()  # 息屏
            # driver.service("uiautomator").stop()
    elif platform == "ios":
        driver = wda.USBClient().session(alert_action=wda.AlertAction.ACCEPT)
        driver.wait_ready()
        driver.implicitly_wait(ReadConfig().get_implicitly_wait)
        # driver.unlock()  # 解锁
        if not driver.info['screenOn']:
            driver.press("power")
            driver.swipe(0.3, 0.9, 0.9, 0.1)
            # TODO 源码无以下这行，原因是手机滑动之后会有延迟，需增加超时机制
            time.sleep(1)
        with driver.alert.watch_and_click():
            for element in ReadConfig().get_popup_elements(app_name):
                ele = driver(labelContains=element).get(timeout=2.5, raise_error=False)
                if ele is None:
                    continue
                else:
                    ele.tap()
            yield driver
            driver.close()
            driver.lock()  # 息屏


@pytest.fixture(scope="function")
def start_stop_app(driver):
    record_file = None
    if platform == "android":
        screenrecord_path = os.path.join(project_dir, "report", "screenrecord")
        if not os.path.exists(screenrecord_path):
            os.makedirs(screenrecord_path)
        record_file = os.path.join(screenrecord_path, time.strftime("%m%d_%H%M%S") + ".mp4")
        try:
            driver.screenrecord(record_file)  # 开始录制视频
            logging.info("start screen recording: %s", str(record_file))
        except Exception as e:
            # logging.error(e)
            logging.info(e)
    logcat_path = os.path.join(project_dir, "report", "logcat")
    if not os.path.exists(logcat_path):
        os.makedirs(logcat_path)
    logcat_filename = os.path.join(logcat_path,
                                   platform + "-" + time.strftime("%m%d_%H%M%S", time.localtime(time.time())) + ".txt")
    logcat_file = open(logcat_filename, "w")
    # driver.unlock()  # 解锁
    if not driver.info['screenOn']:
        driver.press("power")
        driver.swipe(0.3, 0.9, 0.9, 0.1)
        # TODO 源码无以下这行，原因是手机滑动之后会有延迟，需增加超时机制
        time.sleep(1)  # 解锁设备
    # # 自动下载apk, apk路径在app包内的data文件夹下
    base_path = os.path.join(project_dir, app_name, "data")
    pkg_list = [i for i in os.listdir(base_path) if ".apk" in i]
    check_pkg = AdbTools(devices).check_pkg(package_name=package_name)
    if pkg_list and not check_pkg:
        pkg_name = pkg_list[0]
        pkg_path = os.path.join(base_path, pkg_name)
        logging.info("install app: %s", str(package_name))
        AdbTools(devices).install(pkg_path)
    driver.app_stop(package_name)  # 确保待测app已终止
    poplog = None
    if platform == "android":
        os.system("adb logcat -c")
        poplog = subprocess.Popen(["adb", "logcat", "-v", "time"], stdout=logcat_file,
                                  stderr=subprocess.PIPE)  # 启动logcat捕获日志
        logging.info("start capturing log: %s", str(logcat_file))
        driver.app_start(package_name, wait=True)  # 启动app
        # time.sleep(5)
        # while driver.current_app()["package"] != package_name and not driver(textContains="可能包含").exists:
        #     time.sleep(0.5)
        #     logging.info("waiting app start")
        #     if driver(textContains="可能包含").exists:
        #         driver(text="允许").click()
        #         time.sleep(0.5)
        #         # if driver.current_app()["package"] == "com.android.settings":
        #         driver(text="星纪AR").click()
        #         time.sleep(0.5)
        #         driver(text="授予通知使用权").click()
        #         time.sleep(0.5)
        #         driver(text="允许").click()
        #         time.sleep(0.5)
        #         driver.press("back")
        #         time.sleep(0.5)
        #         driver.press("back")
        # driver(resourceId="com.upuphone.xr.sapp:id/card_title", text="AR实景导航").click()
        # time.sleep(2)
        # if driver(text="同意并继续").exists:
        #     driver(resourceId="com.upuphone.xr.sapp:id/agree_privacy").click()
        #     time.sleep(5)
        # # TODO
    elif platform == "ios":
        poplog = subprocess.Popen(["idevicesyslog"], stdout=logcat_file, stderr=subprocess.PIPE)  # 启动idevicesyslog捕获日志
        logging.info("start capturing log: %s", str(logcat_file))
        driver.app_activate(package_name)  # 启动app
    logging.info("start app: %s", str(package_name))
    yield
    if platform == "android":
        driver.screenrecord.stop()  # 停止录制视频
        logging.info("stop screen recording")
        try:
            allure.attach.file(record_file, "执行视频 " + str(record_file), allure.attachment_type.MP4)  # 添加视频到报告中
        except Exception as e:
            logging.info(e)
    logcat_file.close()
    poplog.terminate()  # 停止日志捕获
    logging.info("stop capturing log")
    allure.attach.file(logcat_filename, "logcat日志 " + str(logcat_filename),
                       allure.attachment_type.TEXT)  # 添加logcat日志到报告中
    driver.app_stop(package_name)  # 停止app
    logging.info("stop app: %s", str(package_name))


@pytest.fixture(scope="function")
def clear_cache(driver):
    yield
    logging.info("clear app cache")
    driver.app_clear(package_name)


def _add_screenshot(driver):
    """ 添加截图 """
    screenshot_path = os.path.join(project_dir, "report", "screenshot")
    if not os.path.exists(screenshot_path):
        os.makedirs(screenshot_path)
    filename = os.path.join(screenshot_path, str(uuid.uuid1()) + ".png")
    driver.screenshot(filename)  # 截图
    logging.info("take screenshot: %s", str(filename))
    allure.attach.file(filename, "失败截图 " + time.strftime("%m-%d %H:%M:%S", time.localtime()) + " " + str(filename),
                       allure.attachment_type.PNG)  # 添加截图到报告中


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        for i in item.funcargs:
            if isinstance(item.funcargs[i], u2.Device) or isinstance(item.funcargs[i], wda.Client):
                _add_screenshot(item.funcargs[i])


def pytest_collection_modifyitems(session, items):
    print("收集到的测试用例:%s" % items)
