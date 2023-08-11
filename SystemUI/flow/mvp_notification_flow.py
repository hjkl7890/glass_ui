# creater: chuanwen.peng
# time: 2022/7/12 12:30
import time

import allure

from SystemUI.page.mvp_notification_page import NotificationPagePhone, NotificationPageAuxiliary, NotificationPageGlass


class NotificationFlow(object):

    def __init__(self, driver_list):
        if len(driver_list) == 1:
            self.notification_page_phone = NotificationPagePhone(driver_list[0])
        elif len(driver_list) == 2:
            self.notification_page_phone = NotificationPagePhone(driver_list[0])
            self.notification_page_glass = NotificationPageGlass(driver_list[1])
        else:
            self.notification_page_phone = NotificationPagePhone(driver_list[0])
            self.notification_page_auxiliary = NotificationPageAuxiliary(driver_list[1])
            self.notification_page_glass = NotificationPageGlass(driver_list[2])

    @allure.story("检查超级app通知默认开关")
    def check_default_notification_switch(self):
        self.notification_page_phone.click_control()
        self.notification_page_phone.click_notification()
        self.notification_page_phone.check_receive_set()

    @allure.story("智慧通知和系统通知不可同时开启")
    def smart_and_system_not_meanwhile(self):
        self.notification_page_phone.click_control()
        self.notification_page_phone.click_notification()
        self.notification_page_phone.click_notification_setting()
        self.notification_page_phone.set_smart_notify()
        self.notification_page_phone.check_smart_set()
        self.notification_page_phone.click_notification_setting()
        self.notification_page_phone.set_receive_phone()
        self.notification_page_phone.check_receive_set()

    @allure.story("接通中通话卡片显示")
    def check_in_call_display(self):
        self.notification_page_auxiliary.call_test_phone()
        self.notification_page_phone.test_check_incoming()
        self.notification_page_glass.pickup_incoming()
        self.notification_page_glass.glass_check_hangup()
        self.notification_page_glass.glass_check_time()
        self.notification_page_auxiliary.auxiliaries_hangup()

    @allure.story("1h内通话时长显示")
    def in_call_within1h(self):
        self.notification_page_auxiliary.call_test_phone()
        self.notification_page_phone.test_check_incoming()
        self.notification_page_glass.pickup_incoming()
        self.notification_page_glass.check_1h_display()
        self.notification_page_auxiliary.auxiliaries_hangup()

    @allure.story("来电通话中眼镜端挂断")
    def in_call_glass_hangup(self):
        self.notification_page_auxiliary.call_test_phone()
        self.notification_page_phone.test_check_incoming()
        self.notification_page_glass.pickup_incoming()
        self.notification_page_glass.glass_check_hangup()
        self.notification_page_glass.glass_check_time()
        self.notification_page_glass.short_press_power()
        self.notification_page_glass.glass_check_in_call_disappear()

    @allure.story("来电通话中测试机挂断")
    def in_call_phone_hangup(self):
        self.notification_page_auxiliary.call_test_phone()
        self.notification_page_phone.test_check_incoming()
        self.notification_page_glass.pickup_incoming()
        self.notification_page_glass.glass_check_hangup()
        self.notification_page_glass.glass_check_time()
        self.notification_page_phone.test_hangup_in_call()
        self.notification_page_glass.glass_check_in_call_disappear()

    @allure.story("来电通话中辅助机挂断")
    def in_call_auxiliary_hangup(self):
        self.notification_page_auxiliary.call_test_phone()
        self.notification_page_phone.test_check_incoming()
        self.notification_page_glass.pickup_incoming()
        self.notification_page_glass.glass_check_hangup()
        self.notification_page_glass.glass_check_time()
        self.notification_page_auxiliary.auxiliaries_hangup()
        self.notification_page_glass.glass_check_in_call_disappear()

    @allure.story("呼出通话中眼镜端挂断")
    def out_in_call_glass_hangup(self):
        self.notification_page_phone.call_auxiliary_phone()
        self.notification_page_auxiliary.auxiliary_check_incoming()
        self.notification_page_auxiliary.auxiliary_pickup_incoming()
        self.notification_page_glass.glass_check_hangup()
        self.notification_page_glass.glass_check_time()
        self.notification_page_glass.short_press_power()
        self.notification_page_glass.glass_check_in_call_disappear()

    @allure.story("呼出通话中测试机挂断")
    def out_in_call_phone_hangup(self):
        self.notification_page_phone.call_auxiliary_phone()
        self.notification_page_auxiliary.auxiliary_check_incoming()
        self.notification_page_auxiliary.auxiliary_pickup_incoming()
        self.notification_page_glass.glass_check_hangup()
        self.notification_page_glass.glass_check_time()
        self.notification_page_phone.test_hangup_in_call()
        self.notification_page_glass.glass_check_in_call_disappear()

    @allure.story("呼出通话中辅助机挂断")
    def out_in_call_auxil_hangup(self):
        self.notification_page_phone.call_auxiliary_phone()
        self.notification_page_auxiliary.auxiliary_check_incoming()
        self.notification_page_auxiliary.auxiliary_pickup_incoming()
        self.notification_page_glass.glass_check_hangup()
        self.notification_page_glass.glass_check_time()
        self.notification_page_auxiliary.auxiliaries_hangup()
        self.notification_page_glass.glass_check_in_call_disappear()
