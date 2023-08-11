# creater: chuanwen.peng
# time: 2022/7/12 12:11
import os
import re
import time
import allure
from common.base_page import BasePage
from SystemUI.element.element_router import ElementRouter
from SystemUI import root_dir


class NotificationPagePhone(BasePage):

    def __init__(self, driver):
        self.platform = root_dir.split('\\')[-1]
        super(NotificationPagePhone, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__, "element")
        self.data = MvpData(self.driver).data

    @allure.step("点击控制")
    def click_control(self):
        self.find_element_and_click(**self.element["control"])
        self.assert_element_exist(**self.element["notification"])

    @allure.step("点击通知")
    def click_notification(self):
        self.find_element_and_click(**self.element["notification"])
        time.sleep(3)
        self.assert_element_exist(**self.element["notification_page"])

    @allure.step("点击通知设置")
    def click_notification_setting(self):
        self.find_element_and_click(**self.element["notification_menu"])
        time.sleep(1)
        self.assert_element_exist(**self.element["choose_title"])

    @allure.step("设置为接收手机通知")
    def set_receive_phone(self):
        self.find_element_and_click(**self.element["phone_notify"])

    @allure.step("检查设置为接收手机通知")
    def check_receive_set(self):
        self.assert_element_exist(**self.element["receive_set"])

    @allure.step("设置为智慧提醒通知")
    def set_smart_notify(self):
        self.find_element_and_click(**self.element["smart_notify"])

    @allure.step("检查设置为智慧提醒通知")
    def check_smart_set(self):
        self.assert_element_exist(**self.element["smart_set"])

    @allure.step("设置为关闭所有通知")
    def set_close_all(self):
        self.find_element_and_click(**self.element["close_all"])

    @allure.step("检查设置为关闭所有通知")
    def check_close_set(self):
        self.assert_element_exist(**self.element["close_set"])

    @allure.step("测试手机检查来电")
    def test_check_incoming(self):
        # self.assert_element_exist(**self.element["caller_icon"])
        assert self.driver(resourceId="com.android.incallui:id/caller_icon").exists

    @allure.step("测试手机挂断通话")
    def test_hangup_in_call(self):
        self.driver.open_notification()
        time.sleep(1)
        # self.find_element_and_click(check_toast=False, **self.element["in_call_hangup"])
        self.driver(resourceId="android:id/actions_container").click()
        time.sleep(2)
        self.press_back()

    @allure.step("返回")
    def press_back(self):
        self.driver.press("back")
        time.sleep(1)

    @allure.step("给辅助手机拨打电话")
    def call_auxiliary_phone(self):
        number = self.data["common"]["auxil_number"]
        self.driver.shell("am start -a android.intent.action.CALL -d tel:%s" % number)
        time.sleep(10)


class NotificationPageAuxiliary(BasePage):

    def __init__(self, driver):
        self.platform = root_dir.split('\\')[-1]
        super(NotificationPageAuxiliary, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__, "element")
        self.data = MvpData(self.driver).data

    @allure.step("给测试手机拨打电话")
    def call_test_phone(self):
        number = self.data["common"]["phone_number"]
        self.driver.shell("am start -a android.intent.action.CALL -d tel:%s" % number)
        time.sleep(10)

    @allure.step("辅助机挂断电话")
    def auxiliaries_hangup(self):
        self.driver.shell("input keyevent KEYCODE_ENDCALL")
        time.sleep(3)

    @allure.step("辅助手机检查来电")
    def auxiliary_check_incoming(self):
        assert self.driver(resourceId="com.android.incallui:id/caller_icon").exists

    @allure.step("辅助手机接听电话")
    def auxiliary_pickup_incoming(self):
        self.driver.shell("input keyevent 5")
        time.sleep(2)


class NotificationPageGlass(BasePage):

    def __init__(self, driver):
        self.platform = root_dir.split('\\')[-1]
        super(NotificationPageGlass, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__, "element")
        self.data = MvpData(self.driver).data

    @allure.step("接听来电")
    def pickup_incoming(self):
        self.find_element_and_click(**self.element["call_pickup"])
        time.sleep(1)

    @allure.step("检查挂断按钮")
    def glass_check_hangup(self):
        self.assert_element_exist(**self.element["hangup_icon"])

    @allure.step("检查通话时间")
    def glass_check_time(self):
        self.assert_element_exist(**self.element["call_time"])

    @allure.step("检查1h内通话中显示")
    def check_1h_display(self):
        self.assert_element_exist(**self.element["hangup_icon"])
        call_time = self.find_element(**self.element["call_time"]).get_text()
        assert len(call_time) == 5

    @allure.step("短按power键")
    def short_press_power(self):
        self.driver.shell("input keyevent 26")
        time.sleep(2)

    @allure.step("眼镜端检查通话中消失")
    def glass_check_in_call_disappear(self):
        assert False if self.check_element_existence(**self.element["call_time"]) else True


class MvpData(BasePage):
    def __init__(self, driver):
        self.platform = root_dir.split('\\')[-1]
        super(MvpData, self).__init__(driver)
        self.data = ElementRouter.select(self.__class__.__name__, "data")
