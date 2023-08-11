# creater: chuanwen.peng
# time: 2022/7/12 12:11
import os
import re
import time
import allure
from common.base_page import BasePage
from SystemUI.element.element_router import ElementRouter
from SystemUI import root_dir


class TelePagePhone(BasePage):

    def __init__(self, driver):
        self.platform = root_dir.split('\\')[-1]
        super(TelePagePhone, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__, "element")
        self.data = Data(self.driver).data

    @allure.step("测试手机检查来电")
    def test_check_incoming(self):
        # self.assert_element_exist(**self.element["incoming"])
        assert self.driver(resourceId="com.upuphone.starchat:id/incoming_phone_allow").exists

    @allure.step("测试手机挂断来电")
    def test_hangup_incoming(self):
        # self.find_element_and_click(check_toast=False, **self.element["hang_up"])
        self.driver(resourceId="com.upuphone.starchat:id/incoming_phone_hang_up").click()
        time.sleep(2)

    @allure.step("测试手机接听来电")
    def test_answer_incoming(self):
        # self.find_element_and_click(check_toast=False, **self.element["incoming"])
        self.driver(resourceId="com.upuphone.starchat:id/incoming_phone_allow").click()
        time.sleep(2)

    @allure.step("测试手机挂断通话")
    def test_hangup_in_call(self):
        # self.find_element_and_click(check_toast=False, **self.element["call_time"])
        # time.sleep(1)
        # self.find_element_and_click(check_toast=False, **self.element["end_call"])
        self.driver(resourceId="com.android.systemui:id/call_time").click()
        time.sleep(1)
        self.driver(resourceId="com.upuphone.starchat:id/incall_end_call").click()
        time.sleep(2)

    @allure.step("打开酷狗音乐")
    def open_kugou_music(self):
        self.driver.app_start("com.kugou.android", wait=True)
        time.sleep(2)

    @allure.step("关闭酷狗音乐")
    def close_kugou_music(self):
        self.driver.app_stop("com.kugou.android")
        time.sleep(2)

    @allure.step("打开超级app")
    def open_super_app(self):
        self.driver.app_start("com.upuphone.star.launcher", wait=True)
        time.sleep(2)

    @allure.step("播放音乐")
    def click_first_music(self):
        time.sleep(2)
        if self.check_element_existence(**self.element["dialog"]):
            self.find_element_and_click(check_toast=False, **self.element["dialog"])
        self.find_element_and_click(check_toast=False, **self.element["search_music"])
        self.driver(focused=True).send_keys("周杰伦")
        if self.check_element_existence(**self.element["dialog"]):
            self.find_element_and_click(check_toast=False, **self.element["dialog"])
        self.find_element_and_click(check_toast=False, **self.element["search_button"])
        time.sleep(1)
        if self.check_element_existence(**self.element["dialog"]):
            self.find_element_and_click(check_toast=False, **self.element["dialog"])
        self.find_element_and_click(check_toast=False, **self.element["play_music"])
        time.sleep(2)
        res = [i.strip() for i in self.driver.shell("dumpsys audio | grep -ie 'state:'").output.split('\n') if i][-2]
        pid = re.findall(r'.*?piid:(.*?) state.*?', res, re.S)[0]
        return pid

    @allure.step("下拉菜单")
    def drop_down_menu(self):
        # self.driver.open_notification()
        self.driver.swipe(1000, 60, 1000, 2000)
        time.sleep(1)
        self.press_back()
        self.driver.swipe(1000, 60, 1000, 2000)
        time.sleep(1)

    @allure.step("检查音乐暂停")
    def check_music_pause(self, pid):
        res = self.driver.shell("dumpsys audio | grep -ie 'piid:%s state'" % pid).output.split('\n')
        status = [i.strip() for i in res if i][-1]
        if 'paused' in status:
            assert True
        else:
            assert False

    @allure.step("检查音乐播放")
    def check_music_playing(self, pid):
        res = self.driver.shell("dumpsys audio | grep -ie 'piid:%s state'" % pid).output.split('\n')
        status = [i.strip() for i in res if i][-1]
        if 'started' in status:
            assert True
        else:
            assert False

    @allure.step("检查蓝牙已连接")
    def check_bluetooth_connected(self):
        self.assert_element_exist(**self.element["connected"])

    @allure.step("返回")
    def press_back(self):
        self.driver.press("back")
        time.sleep(1)

    @allure.step("打开抖音web")
    def open_tiktok_web(self):
        self.find_element_and_click(check_toast=False, **self.element["tiktok"])
        time.sleep(10)

    @allure.step("退出抖音web")
    def close_tiktok_web(self):
        self.find_element_and_click(check_toast=False, **self.element["disconnect"])
        time.sleep(1)
        self.find_element_and_click(check_toast=False, **self.element["confirm"])
        time.sleep(1)

    @allure.step("打开AR实景导航")
    def open_navigation(self):
        self.find_element_and_click(check_toast=False, **self.element["navigation"])
        time.sleep(2)

    @allure.step("打开AR名片")
    def open_card(self):
        self.find_element_and_click(check_toast=False, **self.element["open_glass"])
        time.sleep(2)

    @allure.step("点击搜索框")
    def click_search_btn(self):
        self.find_element_and_click(**self.element["searchBar"])
        time.sleep(1)

    @allure.step("点击并搜索框并输入")
    def click_and_input(self, f_name):
        data = self.data[f_name]["address"]
        self.driver(focused=True).send_keys(data)
        time.sleep(5)
        self.element["select_location"]["textContains"] = self.data[f_name]["addContains"]
        self.find_element_and_click(**self.element["select_location"], index=0)
        time.sleep(3)

    @allure.step("点击路线")
    def click_route(self):
        self.find_element_and_click(**self.element["route"])
        time.sleep(8)

    @allure.step("开始导航")
    def click_start_route(self, f_name):
        self.element["start_navigation"]["text"] = self.data[f_name]["text"]
        status = self.check_element_existence(**self.element["start_navigation"])
        while not status:
            time.sleep(3)
            status = self.check_element_existence(**self.element["start_navigation"])
        self.find_element_and_click(**self.element["start_navigation"])
        time.sleep(2)

    @allure.step("退出导航")
    def click_quit_navi(self):
        self.find_element_and_click(**self.element["exit"])
        time.sleep(1)
        self.find_element_and_click(**self.element["exit_navigation"])
        time.sleep(2)
        for i in range(3):
            self.driver.press("back")
            time.sleep(2)


class TelePageAuxiliary(BasePage):

    def __init__(self, driver):
        self.platform = root_dir.split('\\')[-1]
        super(TelePageAuxiliary, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__, "element")
        self.data = Data(self.driver).data

    @allure.step("给测试手机拨打电话")
    def call_test_phone(self):
        time.sleep(2)
        device = self.data["common"]["auxiliary_device"]
        number = self.data["common"]["phone_number"]
        os.system("adb -s %s shell am start -a android.intent.action.CALL -d tel:%s" % (device, number))
        time.sleep(10)

    @allure.step("给测试手机拨打电话不等待")
    def call_to_test_phone(self):
        device = self.data["common"]["auxiliary_device"]
        number = self.data["common"]["phone_number"]
        os.system("adb -s %s shell am start -a android.intent.action.CALL -d tel:%s" % (device, number))

    @allure.step("辅助机挂断电话")
    def auxiliaries_hangup(self):
        device = self.data["common"]["auxiliary_device"]
        os.system("adb -s %s shell input keyevent KEYCODE_ENDCALL" % device)
        time.sleep(2)

    @allure.step("给测试手机发送短信")
    def send_sms_phone(self, f_name):
        device = self.data["common"]["auxiliary_device"]
        number = self.data["common"]["phone_number"]
        os.system("adb -s %s shell am start -a android.intent.action.SENDTO -d sms:%s" % (device, number))
        time.sleep(5)
        os.system("adb -s %s shell input tap 264 2824" % device)
        content = self.data[f_name]["content"]
        self.driver(focused=True).send_keys(content)
        self.find_element_and_click(**self.element["send_button"])

    @allure.step("给测试手机发送两条短信")
    def send_two_sms_phone(self, f_name):
        device = self.data["common"]["auxiliary_device"]
        number = self.data["common"]["phone_number"]
        os.system("adb -s %s shell am start -a android.intent.action.SENDTO -d sms:%s" % (device, number))
        time.sleep(5)
        os.system("adb -s %s shell input tap 264 2824" % device)
        for num in range(2):
            print("开始发第%d条消息" % (num + 1))
            content = self.data[f_name]["content" + str(num)]
            self.driver(focused=True).send_keys(content)
            self.find_element_and_click(**self.element["send_button"])
            time.sleep(5)

    @allure.step("关闭短信")
    def close_sms(self):
        self.driver.app_stop("com.upuphone.starchat")
        time.sleep(1)

    @allure.step("给测试手机发送qq")
    def send_qq_phone(self, f_name):
        self.driver.app_start("com.tencent.mobileqq", wait=True)
        time.sleep(1)
        # self.find_element_and_click(check_toast=False, **self.element["search"])
        # username = self.data[f_name]["username"]
        # self.driver(focused=True).send_keys(username)
        # self.find_element_and_click(check_toast=False, **self.element["search_result"])
        self.find_element_and_click(check_toast=False, **self.element["friend"])
        content = self.data[f_name]["content"]
        self.find_element_and_input(**self.element["input"], plaintext=content)
        self.find_element_and_click(**self.element["fun_btn"])

    @allure.step("给测试手机发送多条qq")
    def send_multiple_qq_phone(self, f_name, count):
        self.driver.app_start("com.tencent.mobileqq", wait=True)
        time.sleep(1)
        self.find_element_and_click(check_toast=False, **self.element["search"])
        username = self.data[f_name]["username"]
        self.driver(focused=True).send_keys(username)
        self.find_element_and_click(check_toast=False, **self.element["search_result"])
        for num in range(count):
            print("开始发第%d条qq" % (num + 1))
            content = str(num + 1)
            self.find_element_and_input(**self.element["input"], plaintext=content)
            self.find_element_and_click(**self.element["fun_btn"])
            time.sleep(2)

    @allure.step("关闭qq")
    def close_qq(self):
        self.driver.app_stop("com.tencent.mobileqq")
        time.sleep(1)

    @allure.step("给测试手机发送微信")
    def send_weixin_phone(self, f_name):
        self.driver.app_start("com.tencent.mm", wait=True)
        time.sleep(1)
        self.find_element_and_click(check_toast=False, **self.element["search_weixin"])
        username = self.data[f_name]["username"]
        self.driver(focused=True).send_keys(username)
        self.find_element_and_click(check_toast=False, **self.element["weixin_result"])
        content = self.data[f_name]["content"]
        self.find_element_and_input(**self.element["input_weixin"], plaintext=content)
        self.find_element_and_click(**self.element["send_weixin"])

    @allure.step("关闭微信")
    def close_weixin(self):
        self.driver.app_stop("com.tencent.mm")
        time.sleep(1)


class TelePageGlass(BasePage):

    def __init__(self, driver):
        self.platform = root_dir.split('\\')[-1]
        super(TelePageGlass, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__, "element")
        self.data = Data(self.driver).data

    @allure.step("眼镜端检查来电")
    def glass_check_incoming(self):
        self.assert_element_exist(**self.element["call_icon"])

    @allure.step("眼镜端检查来电消失")
    def glass_check_incoming_disappear(self):
        assert False if self.check_element_existence(**self.element["call_icon"]) else True

    @allure.step("检查来电号码")
    def check_call_phone(self, f_name):
        self.element["call_phone"]["text"] = self.data[f_name]["number"]
        self.assert_element_exist(**self.element["call_phone"])

    @allure.step("检查来电归属地")
    def check_call_local(self, f_name):
        self.element["call_local"]["textContains"] = self.data[f_name]["localContains"]
        self.assert_element_exist(**self.element["call_local"])

    @allure.step("单指单击tp")
    def oneclick_tp(self):
        device = self.data["common"]["glass_device"]
        os.system("adb -s %s shell input keyevent KEYCODE_DPAD_CENTER" % device)
        time.sleep(2)

    @allure.step("单指双击tp")
    def two_click_tp(self):
        device = self.data["common"]["glass_device"]
        os.system("adb -s %s shell input keyevent KEYCODE_BACK" % device)
        time.sleep(2)

    @allure.step("单指长按tp")
    def long_press_tp(self):
        device = self.data["common"]["glass_device"]
        os.system("adb -s %s shell input keyevent KEYCODE_MENU" % device)
        time.sleep(2)

    @allure.step("眼镜端power挂断")
    def glass_hangup_power(self):
        device = self.data["common"]["glass_device"]
        os.system("adb -s %s shell input keyevent 26" % device)
        time.sleep(2)

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

    @allure.step("眼镜端检查通话中消失")
    def glass_check_in_call_disappear(self):
        assert False if self.check_element_existence(**self.element["call_time"]) else True

    @allure.step("检查熄屏")
    def check_screen_off(self):
        device = self.data["common"]["glass_device"]
        res = os.popen("adb -s %s shell dumpsys power | findstr Display" % device).read().strip()
        status = re.findall(r'.*?Power: state=(.*?)Ambient.*?', res, re.S)[0]
        assert status == "OFF"

    @allure.step("检查亮屏")
    def check_screen_on(self):
        device = self.data["common"]["glass_device"]
        res = os.popen("adb -s %s shell dumpsys power | findstr Display" % device).read().strip()
        status = re.findall(r'.*?Power: state=(.*?)Ambient.*?', res, re.S)[0]
        assert status == "ON"

    @allure.step("检查短信")
    def check_sms_display(self, f_name, content="content"):
        self.assert_element_exist(**self.element["msg_icon"])
        self.element["msg_title"]["text"] = self.data[f_name]["number"]
        self.assert_element_exist(**self.element["msg_title"])
        device = self.data["common"]["glass_device"]
        # receive_time = os.popen("adb -s %s shell date" % device).read().strip().split()[3][:5]
        # self.element["msg_time"]["text"] = receive_time
        self.assert_element_exist(**self.element["msg_time"])
        self.element["msg_content"]["text"] = self.data[f_name][content]
        self.assert_element_exist(**self.element["msg_content"])

    @allure.step("等待短信显示")
    def wait_sms_display(self):
        start = time.time()
        while not self.check_element_existence(**self.element["msg_icon"]) and (time.time() - start < 5):
            pass

    @allure.step("等待短信堆叠")
    def wait_sms_stack(self):
        start = time.time()
        while not self.check_element_existence(**self.element["next_view"]) and (time.time() - start < 5):
            pass

    @allure.step("检查消息堆叠")
    def check_message_stack(self):
        self.assert_element_exist(**self.element["next_view"])

    @allure.step("检查短信图标显示")
    def check_sms_icon_display(self):
        self.assert_element_exist(**self.element["msg_icon"])

    @allure.step("检查短信图标消失")
    def check_sms_icon_disappear(self):
        assert False if self.check_element_existence(**self.element["msg_icon"]) else True

    @allure.step("检查短信显示5s")
    def check_sms_display_5s(self):
        time.sleep(6)
        self.check_sms_icon_disappear()

    @allure.step("关闭短信通知")
    def close_sms_display(self):
        self.wait_sms_display()
        self.two_click_tp()
        self.check_sms_icon_disappear()

    @allure.step("滑动查看短信通知")
    def swipe_sms_display(self):
        self.wait_sms_display()
        device = self.data["common"]["glass_device"]
        os.system("adb -s %s shell input keyevent KEYCODE_DPAD_LEFT" % device)
        time.sleep(0.5)
        os.system("adb -s %s shell input keyevent KEYCODE_DPAD_RIGHT" % device)
        time.sleep(0.5)

    @allure.step("查看新短信通知")
    def view_new_sms_display(self, f_name):
        self.wait_sms_display()
        self.wait_sms_stack()
        self.check_sms_display(f_name, content="content1")

    @allure.step("检查低电量通知")
    def check_low_battery(self, f_name):
        self.assert_element_exist(**self.element["msg_icon"])
        self.element["system_msg_title"]["text"] = self.data[f_name]["text"]
        self.assert_element_exist(**self.element["system_msg_title"])
        device = self.data["common"]["glass_device"]
        # receive_time = os.popen("adb -s %s shell date" % device).read().strip().split()[3][:5]
        # self.element["msg_time"]["text"] = receive_time
        self.assert_element_exist(**self.element["msg_time"])
        data = self.data[f_name]["textContains"]
        self.assert_text_exist(data)

    @allure.step("检查电量充满通知")
    def check_full_battery(self, f_name):
        self.assert_element_exist(**self.element["msg_icon"])
        self.element["system_msg_title"]["text"] = self.data[f_name]["text"]
        self.assert_element_exist(**self.element["system_msg_title"])
        device = self.data["common"]["glass_device"]
        # receive_time = os.popen("adb -s %s shell date" % device).read().strip().split()[3][:5]
        # self.element["msg_time"]["text"] = receive_time
        self.assert_element_exist(**self.element["msg_time"])
        data = self.data[f_name]["textContains"]
        self.assert_text_exist(data)

    @allure.step("设置低电量")
    def set_low_battery(self):
        device = self.data["common"]["glass_device"]
        os.system("adb -s %s shell dumpsys battery set status 2" % device)
        time.sleep(0.5)
        os.system("adb -s %s shell dumpsys battery unplug" % device)
        time.sleep(0.5)
        os.system("adb -s %s shell dumpsys battery set level 16" % device)
        time.sleep(0.5)
        os.system("adb -s %s shell dumpsys battery set level 15" % device)
        time.sleep(0.5)

    @allure.step("设置电量充满")
    def set_full_battery(self):
        device = self.data["common"]["glass_device"]
        os.system("adb -s %s shell dumpsys battery set status 5" % device)
        time.sleep(0.5)
        os.system("adb -s %s shell dumpsys battery set level 99" % device)
        time.sleep(0.5)
        os.system("adb -s %s shell dumpsys battery set level 100" % device)
        time.sleep(0.5)

    @allure.step("恢复电量设置")
    def reset_battery_set(self):
        device = self.data["common"]["glass_device"]
        os.system("adb -s %s shell dumpsys battery reset" % device)

    @allure.step("检查关机弹窗")
    def check_shutdown_popup(self, f_name):
        self.assert_element_exist(**self.element["confirm_content"])
        self.assert_element_exist(**self.element["confirm_refuse"])
        self.assert_element_exist(**self.element["confirm_agree"])
        data = self.data[f_name]["textContains"]
        self.assert_text_exist(data)

    @allure.step("长按power键2s")
    def long_press_power(self):
        device = self.data["common"]["glass_device"]
        os.system("adb -s %s shell input keyevent --longpress 26" % device)

    @allure.step("语音唤醒")
    def awaken_ai(self):
        self.driver.shell("input keyevent --longpress 289")
        time.sleep(1)

    @allure.step("检查AI语音")
    def check_ai_voice(self):
        self.assert_element_exist(**self.element["ai_voice"])

    @allure.step("检查AI语音不显示")
    def check_ai_no_show(self):
        assert False if self.check_element_existence(**self.element["ai_voice"]) else True

    @allure.step("短按power键")
    def short_press_power(self):
        device = self.data["common"]["glass_device"]
        os.system("adb -s %s shell input keyevent 26" % device)

    @allure.step("检查qq")
    def check_qq_display(self, f_name, content="content"):
        self.assert_element_exist(**self.element["msg_icon"])
        self.element["msg_title"]["textContains"] = self.data[f_name]["friend_name"]
        self.assert_element_exist(**self.element["msg_title"])
        device = self.data["common"]["glass_device"]
        # receive_time = os.popen("adb -s %s shell date" % device).read().strip().split()[3][:5]
        # self.element["msg_time"]["text"] = receive_time
        self.assert_element_exist(**self.element["msg_time"])
        if isinstance(content, int):
            self.element["msg_content"]["text"] = str(content)
        else:
            self.element["msg_content"]["text"] = self.data[f_name][content]
        self.assert_element_exist(**self.element["msg_content"])

    @allure.step("检查长消息显示大于5s")
    def check_long_text_display(self):
        self.wait_sms_display()
        time.sleep(5)
        self.assert_element_exist(**self.element["msg_icon"])


class Data(BasePage):
    def __init__(self, driver):
        self.platform = root_dir.split('\\')[-1]
        super(Data, self).__init__(driver)
        self.data = ElementRouter.select(self.__class__.__name__, "data")
