# creater: chuanwen.peng
# time: 2022/7/12 12:30
import time

import allure

from SystemUI.page.notification_page import TelePagePhone, TelePageAuxiliary, TelePageGlass


class TeleFlow(object):

    def __init__(self, driver_list):
        if len(driver_list) == 1:
            self.tele_page_phone = TelePagePhone(driver_list[0])
        elif len(driver_list) == 2:
            self.tele_page_phone = TelePagePhone(driver_list[0])
            self.tele_page_glass = TelePageGlass(driver_list[1])
        else:
            self.tele_page_phone = TelePagePhone(driver_list[0])
            self.tele_page_auxiliary = TelePageAuxiliary(driver_list[1])
            self.tele_page_glass = TelePageGlass(driver_list[2])

    @allure.story("来电未接听时通知显示")
    def call_check_no_answer_display(self, f_name):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_phone.test_check_incoming()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.check_call_phone(f_name)
        self.tele_page_glass.check_call_local(f_name)
        self.tele_page_auxiliary.auxiliaries_hangup()

    @allure.story("通话中通知显示")
    def call_check_in_call_display(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_phone.test_check_incoming()
        self.tele_page_glass.oneclick_tp()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_auxiliary.auxiliaries_hangup()

    @allure.story("来电未接听时辅助手机挂断电话")
    def call_no_answer_auxiliary_hangup(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_auxiliary.auxiliaries_hangup()
        self.tele_page_glass.glass_check_incoming_disappear()

    @allure.story("来电未接听时测试手机挂断电话")
    def call_no_answer_test_hangup(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_phone.test_hangup_incoming()
        self.tele_page_glass.glass_check_incoming_disappear()
        self.tele_page_auxiliary.auxiliaries_hangup()

    @allure.story("来电未接听时眼镜端挂断电话")
    def call_no_answer_glass_hangup(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.two_click_tp()
        self.tele_page_glass.glass_check_incoming_disappear()
        self.tele_page_auxiliary.auxiliaries_hangup()

    @allure.story("来电通知测试机接听")
    def call_phone_answer(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_phone.test_check_incoming()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_phone.test_answer_incoming()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_auxiliary.auxiliaries_hangup()

    @allure.story("来电通知眼镜端接听")
    def call_glass_answer(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.oneclick_tp()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_auxiliary.auxiliaries_hangup()

    @allure.story("通话中辅助手机挂断电话")
    def in_call_auxiliary_hangup(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.oneclick_tp()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_auxiliary.auxiliaries_hangup()
        self.tele_page_glass.glass_check_in_call_disappear()

    @allure.story("通话中测试手机挂断电话")
    def in_call_phone_hangup(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.oneclick_tp()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_phone.test_hangup_in_call()
        self.tele_page_glass.glass_check_in_call_disappear()

    @allure.story("通话中眼镜端挂断电话")
    def in_call_glass_hangup(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.oneclick_tp()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_glass.two_click_tp()
        self.tele_page_glass.glass_check_in_call_disappear()

    @allure.story("收到来电时不进行任何操作")
    def do_nothing_when_call(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        time.sleep(15)
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_auxiliary.auxiliaries_hangup()
        self.tele_page_glass.glass_check_in_call_disappear()

    @allure.story("1h内通话时长显示")
    def display_within1h(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_phone.test_check_incoming()
        self.tele_page_glass.oneclick_tp()
        self.tele_page_glass.check_1h_display()
        self.tele_page_auxiliary.auxiliaries_hangup()

    @allure.story("来电时单指单击tp")
    def call_oneclick_tp(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_phone.test_check_incoming()
        self.tele_page_glass.oneclick_tp()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_auxiliary.auxiliaries_hangup()

    @allure.story("来电时单指双击tp")
    def call_two_click_tp(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.two_click_tp()
        self.tele_page_glass.glass_check_incoming_disappear()
        self.tele_page_auxiliary.auxiliaries_hangup()

    @allure.story("来电时短按Power键")
    def call_click_power(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.glass_hangup_power()
        self.tele_page_glass.glass_check_incoming_disappear()
        self.tele_page_auxiliary.auxiliaries_hangup()

    @allure.story("通话中单指单击tp")
    def in_call_oneclick_tp(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.oneclick_tp()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_glass.oneclick_tp()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_auxiliary.auxiliaries_hangup()

    @allure.story("通话中单指长按tp")
    def in_call_long_press_tp(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.oneclick_tp()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_glass.long_press_tp()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_auxiliary.auxiliaries_hangup()

    @allure.story("通话中单指双击tp")
    def in_call_two_click_tp(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.oneclick_tp()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_glass.two_click_tp()
        self.tele_page_glass.glass_check_in_call_disappear()

    @allure.story("通话中短按Power键")
    def in_call_click_power(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.oneclick_tp()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_glass.glass_hangup_power()
        self.tele_page_glass.glass_check_in_call_disappear()

    @allure.story("播放音乐时来电")
    def music_incoming(self):
        self.tele_page_phone.open_kugou_music()
        pid = self.tele_page_phone.click_first_music()
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_phone.check_music_pause(pid)
        self.tele_page_phone.drop_down_menu()
        self.tele_page_phone.check_bluetooth_connected()
        self.tele_page_auxiliary.auxiliaries_hangup()
        self.tele_page_phone.check_music_playing(pid)
        self.tele_page_phone.check_bluetooth_connected()
        self.tele_page_phone.close_kugou_music()
        self.tele_page_phone.press_back()

    @allure.story("播放音乐时来电并接听")
    def music_incoming_answer(self):
        self.tele_page_phone.open_kugou_music()
        pid = self.tele_page_phone.click_first_music()
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.oneclick_tp()
        self.tele_page_phone.drop_down_menu()
        self.tele_page_phone.check_music_pause(pid)
        self.tele_page_phone.check_bluetooth_connected()
        self.tele_page_auxiliary.auxiliaries_hangup()
        self.tele_page_glass.glass_check_in_call_disappear()
        self.tele_page_phone.check_music_playing(pid)
        self.tele_page_phone.check_bluetooth_connected()
        self.tele_page_phone.close_kugou_music()
        self.tele_page_phone.open_super_app()

    @allure.story("播放视频时来电")
    def video_incoming(self):
        self.tele_page_phone.open_tiktok_web()
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.two_click_tp()
        self.tele_page_glass.glass_check_incoming_disappear()
        self.tele_page_auxiliary.auxiliaries_hangup()
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.oneclick_tp()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_glass.two_click_tp()
        self.tele_page_glass.glass_check_in_call_disappear()
        self.tele_page_phone.close_tiktok_web()

    @allure.story("导航时来电")
    def navi_incoming(self, f_name):
        self.tele_page_phone.open_navigation()
        self.tele_page_phone.click_search_btn()
        self.tele_page_phone.click_and_input(f_name)
        self.tele_page_phone.click_route()
        self.tele_page_phone.click_start_route(f_name)
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.two_click_tp()
        self.tele_page_glass.glass_check_incoming_disappear()
        self.tele_page_auxiliary.auxiliaries_hangup()
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.oneclick_tp()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_glass.two_click_tp()
        self.tele_page_glass.glass_check_in_call_disappear()
        self.tele_page_phone.click_quit_navi()

    @allure.story("使用AR名片时来电")
    def card_incoming(self):
        self.tele_page_phone.open_card()
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.two_click_tp()
        self.tele_page_glass.glass_check_incoming_disappear()
        self.tele_page_auxiliary.auxiliaries_hangup()
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.oneclick_tp()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_glass.two_click_tp()
        self.tele_page_glass.glass_check_in_call_disappear()
        self.tele_page_glass.two_click_tp()

    @allure.story("来电时连续多次短按Power键")
    def incoming_several_power(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.glass_hangup_power()
        self.tele_page_glass.glass_check_incoming_disappear()
        self.tele_page_auxiliary.auxiliaries_hangup()
        self.tele_page_glass.glass_hangup_power()
        self.tele_page_glass.check_screen_off()
        self.tele_page_glass.glass_hangup_power()
        self.tele_page_glass.check_screen_on()

    @allure.story("通话中连续多次短按Power键")
    def in_call_several_power(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.oneclick_tp()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_glass.glass_hangup_power()
        self.tele_page_glass.glass_check_in_call_disappear()
        self.tele_page_glass.glass_hangup_power()
        self.tele_page_glass.check_screen_off()
        self.tele_page_glass.glass_hangup_power()
        self.tele_page_glass.check_screen_on()

    @allure.story("通话中唤醒AI语音助理")
    def in_call_ai_voice(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.oneclick_tp()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_glass.awaken_ai()
        self.tele_page_glass.check_ai_no_show()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_glass.two_click_tp()
        self.tele_page_glass.glass_check_in_call_disappear()

    @allure.story("来电未接听时唤醒AI语音助理")
    def incoming_ai_voice(self):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.awaken_ai()
        self.tele_page_glass.check_ai_voice()
        self.tele_page_glass.two_click_tp()
        self.tele_page_glass.check_ai_no_show()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.two_click_tp()
        self.tele_page_glass.glass_check_incoming_disappear()
        self.tele_page_auxiliary.auxiliaries_hangup()

    @allure.story("短信通知显示")
    def display_sms_notification(self, f_name):
        self.tele_page_auxiliary.send_sms_phone(f_name)
        self.tele_page_glass.wait_sms_display()
        self.tele_page_glass.check_sms_display(f_name)
        self.tele_page_auxiliary.close_sms()

    @allure.story("信息展示5s无操作后自动消失")
    def sms_display_5s(self, f_name):
        self.tele_page_auxiliary.send_sms_phone(f_name)
        self.tele_page_glass.wait_sms_display()
        self.tele_page_glass.check_sms_display_5s()
        self.tele_page_auxiliary.close_sms()

    @allure.story("单指双击tp关闭短信通知")
    def sms_two_click_tp(self, f_name):
        self.tele_page_auxiliary.send_sms_phone(f_name)
        self.tele_page_glass.close_sms_display()
        self.tele_page_auxiliary.close_sms()

    @allure.story("TouchPad前后滑动查看长文本信息")
    def swipe_view_long_sms(self, f_name):
        self.tele_page_auxiliary.send_sms_phone(f_name)
        self.tele_page_glass.swipe_sms_display()
        self.tele_page_auxiliary.close_sms()

    @allure.story("Touchpad滑动过程中收到其他通知")
    def swipe_receive_new_sms(self, f_name):
        self.tele_page_auxiliary.send_two_sms_phone(f_name)
        self.tele_page_glass.swipe_sms_display()
        self.tele_page_glass.view_new_sms_display(f_name)
        self.tele_page_auxiliary.close_sms()

    @allure.story("长文本自动滚动过程中收到其他通知")
    def roll_receive_new_sms(self, f_name):
        self.tele_page_auxiliary.send_two_sms_phone(f_name)
        time.sleep(2)
        self.tele_page_glass.view_new_sms_display(f_name)
        self.tele_page_auxiliary.close_sms()

    @allure.story("长文本自动滚动过程短按power键熄屏/亮屏")
    def roll_power(self, f_name):
        self.tele_page_auxiliary.send_sms_phone(f_name)
        self.tele_page_glass.wait_sms_display()
        self.tele_page_glass.glass_hangup_power()
        self.tele_page_glass.glass_hangup_power()
        self.tele_page_glass.check_sms_icon_display()
        self.tele_page_auxiliary.close_sms()

    @allure.story("手动滑动至底部后不再自动滚动展示")
    def swipe_no_roll(self, f_name):
        self.tele_page_auxiliary.send_sms_phone(f_name)
        self.tele_page_glass.wait_sms_display()
        self.tele_page_glass.swipe_sms_display()
        self.tele_page_glass.check_sms_display_5s()
        self.tele_page_auxiliary.close_sms()

    @allure.story("低电量提醒（15%）")
    def low_battery_reminder(self, f_name):
        self.tele_page_glass.set_low_battery()
        self.tele_page_glass.check_low_battery(f_name)
        self.tele_page_glass.reset_battery_set()

    @allure.story("电量充满提醒（100%）")
    def full_battery_reminder(self, f_name):
        self.tele_page_glass.set_full_battery()
        self.tele_page_glass.check_full_battery(f_name)
        self.tele_page_glass.reset_battery_set()

    @allure.story("关机确认弹窗检查")
    def shutdown_confirm_popup(self, f_name):
        self.tele_page_glass.long_press_power()
        self.tele_page_glass.check_shutdown_popup(f_name)
        self.tele_page_glass.two_click_tp()

    @allure.story("播放音乐时收到弹窗通知")
    def music_shutdown_confirm(self, f_name):
        self.tele_page_phone.open_kugou_music()
        self.tele_page_phone.click_first_music()
        self.tele_page_glass.long_press_power()
        self.tele_page_glass.check_shutdown_popup(f_name)
        self.tele_page_glass.two_click_tp()
        self.tele_page_phone.close_kugou_music()

    @allure.story("播放视频时收到弹窗通知")
    def video_shutdown_confirm(self, f_name):
        self.tele_page_phone.open_tiktok_web()
        self.tele_page_glass.long_press_power()
        self.tele_page_glass.check_shutdown_popup(f_name)
        self.tele_page_glass.two_click_tp()
        self.tele_page_phone.close_tiktok_web()

    @allure.story("导航时收到弹窗通知")
    def navi_shutdown_confirm(self, f_name):
        self.tele_page_phone.open_navigation()
        self.tele_page_phone.click_search_btn()
        self.tele_page_phone.click_and_input(f_name)
        self.tele_page_phone.click_route()
        self.tele_page_phone.click_start_route(f_name)
        self.tele_page_glass.long_press_power()
        self.tele_page_glass.check_shutdown_popup(f_name)
        self.tele_page_glass.two_click_tp()
        self.tele_page_phone.click_quit_navi()

    @allure.story("使用AR名片时收到弹窗通知")
    def card_shutdown_confirm(self, f_name):
        self.tele_page_phone.open_card()
        self.tele_page_glass.long_press_power()
        self.tele_page_glass.check_shutdown_popup(f_name)
        self.tele_page_glass.two_click_tp()
        self.tele_page_glass.two_click_tp()

    @allure.story("应用通知显示")
    def app_notification_display(self, f_name):
        self.tele_page_auxiliary.send_qq_phone(f_name)
        self.tele_page_glass.wait_sms_display()
        self.tele_page_glass.check_qq_display(f_name)
        self.tele_page_auxiliary.close_qq()

    @allure.story("长文本IM消息")
    def long_text_im_message(self, f_name):
        self.tele_page_auxiliary.send_qq_phone(f_name)
        self.tele_page_glass.check_long_text_display()
        self.tele_page_auxiliary.close_qq()

    @allure.story("信息展示5s无操作后自动消失")
    def im_display_5s(self, f_name):
        self.tele_page_auxiliary.send_qq_phone(f_name)
        self.tele_page_glass.wait_sms_display()
        self.tele_page_glass.check_sms_display_5s()
        self.tele_page_auxiliary.close_qq()

    @allure.story("单指双击tp关闭IM通知")
    def im_two_click_tp(self, f_name):
        self.tele_page_auxiliary.send_qq_phone(f_name)
        self.tele_page_glass.close_sms_display()
        self.tele_page_auxiliary.close_qq()

    @allure.story("TouchPad前后滑动查看长文本信息")
    def swipe_view_long_im(self, f_name):
        self.tele_page_auxiliary.send_qq_phone(f_name)
        self.tele_page_glass.swipe_sms_display()
        self.tele_page_auxiliary.close_qq()

    @allure.story("手动滑动至底部后不再自动滚动展示")
    def swipe_no_roll_im(self, f_name):
        self.tele_page_auxiliary.send_qq_phone(f_name)
        self.tele_page_glass.wait_sms_display()
        self.tele_page_glass.swipe_sms_display()
        self.tele_page_glass.check_sms_display_5s()
        self.tele_page_auxiliary.close_qq()

    @allure.story("其他通知")
    def other_notification(self, f_name):
        self.tele_page_auxiliary.send_weixin_phone(f_name)
        self.tele_page_glass.wait_sms_display()
        self.tele_page_glass.check_qq_display(f_name)
        self.tele_page_auxiliary.close_weixin()

    @allure.story("通知展示5s没有交互自动消失")
    def notification_display_5s(self, f_name):
        self.tele_page_auxiliary.send_qq_phone(f_name)
        self.tele_page_glass.wait_sms_display()
        self.tele_page_glass.check_sms_display_5s()
        self.tele_page_auxiliary.close_qq()

    @allure.story("多条通知展示5s没有交互自动消失")
    def multiple_notifications_5s(self, f_name):
        count = 5
        self.tele_page_auxiliary.send_multiple_qq_phone(f_name, count)
        self.tele_page_glass.wait_sms_display()
        time.sleep(2)
        for i in range(3):
            self.tele_page_glass.check_qq_display(f_name, range(count)[-(i + 1)] + 1)
            time.sleep(5)
        self.tele_page_glass.check_sms_icon_disappear()
        self.tele_page_auxiliary.close_qq()

    @allure.story("通知未消失时熄屏或关机")
    def notification_power(self, f_name):
        self.tele_page_auxiliary.send_qq_phone(f_name)
        self.tele_page_glass.wait_sms_display()
        for i in range(2):
            self.tele_page_glass.short_press_power()
        self.tele_page_glass.check_qq_display(f_name)
        self.tele_page_auxiliary.close_qq()
        self.tele_page_auxiliary.send_qq_phone(f_name)
        self.tele_page_glass.wait_sms_display()
        self.tele_page_glass.long_press_power()
        self.tele_page_glass.check_sms_icon_disappear()
        self.tele_page_glass.two_click_tp()
        self.tele_page_glass.check_qq_display(f_name)
        self.tele_page_auxiliary.close_qq()

    @allure.story("同类型通知按最新时间收纳展示")
    def multiple_notifications_display_latest(self, f_name):
        count = 5
        self.tele_page_auxiliary.send_multiple_qq_phone(f_name, count)
        self.tele_page_glass.wait_sms_display()
        time.sleep(2)
        for i in range(3):
            self.tele_page_glass.check_qq_display(f_name, range(count)[-(i + 1)] + 1)
            time.sleep(5)
        self.tele_page_glass.check_sms_icon_disappear()
        self.tele_page_auxiliary.close_qq()

    @allure.story("多条通知堆叠显示")
    def multiple_notifications_stack_display(self, f_name):
        count = 5
        self.tele_page_auxiliary.send_multiple_qq_phone(f_name, count)
        self.tele_page_glass.wait_sms_display()
        time.sleep(2)
        for i in range(2):
            self.tele_page_glass.check_message_stack()
            time.sleep(5)
        self.tele_page_glass.check_qq_display(f_name, 3)
        self.tele_page_auxiliary.close_qq()

    @allure.story("来电通知第一优先级展示")
    def call_first_display(self, f_name):
        self.tele_page_auxiliary.call_to_test_phone()
        self.tele_page_auxiliary.send_qq_phone(f_name)
        self.tele_page_glass.wait_sms_stack()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_auxiliary.close_qq()
        self.tele_page_auxiliary.send_qq_phone(f_name)
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.check_message_stack()
        self.tele_page_auxiliary.auxiliaries_hangup()
        self.tele_page_glass.glass_check_incoming_disappear()
        self.tele_page_glass.check_qq_display(f_name)
        self.tele_page_auxiliary.close_qq()

    @allure.story("通话中多通知展示规则")
    def in_call_notifications_display(self, f_name):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        self.tele_page_glass.oneclick_tp()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_auxiliary.send_multiple_qq_phone(f_name, 2)
        self.tele_page_glass.wait_sms_display()
        self.tele_page_glass.glass_check_hangup()
        self.tele_page_glass.glass_check_time()
        self.tele_page_glass.wait_sms_stack()
        self.tele_page_glass.check_qq_display(f_name, 2)
        self.tele_page_auxiliary.close_qq()
        self.tele_page_auxiliary.auxiliaries_hangup()

    @allure.story("多通知tp交互")
    def multi_notification_tp_interaction(self, f_name):
        self.tele_page_auxiliary.call_test_phone()
        self.tele_page_glass.glass_check_incoming()
        count = 5
        self.tele_page_auxiliary.send_multiple_qq_phone(f_name, count)
        self.tele_page_glass.wait_sms_stack()
        time.sleep(5)
        self.tele_page_glass.two_click_tp()
        self.tele_page_glass.glass_check_incoming_disappear()
        for i in range(3):
            self.tele_page_glass.check_qq_display(f_name, range(count)[-(i + 1)] + 1)
            self.tele_page_glass.two_click_tp()
        self.tele_page_glass.check_sms_icon_disappear()
        self.tele_page_auxiliary.close_qq()

    @allure.story("弹窗优先级高于非来电未接听通知")
    def shutdown_higher_notification(self, f_name):
        self.tele_page_glass.long_press_power()
        self.tele_page_glass.check_shutdown_popup(f_name)
        self.tele_page_auxiliary.send_qq_phone(f_name)
        self.tele_page_glass.wait_sms_stack()
        self.tele_page_auxiliary.close_qq()
        self.tele_page_glass.two_click_tp()
        self.tele_page_glass.check_qq_display(f_name)

    @allure.story("多条通知时通知自动关闭逻辑")
    def multi_notification_auto_close(self, f_name):
        self.tele_page_auxiliary.send_multiple_qq_phone(f_name, 2)
        self.tele_page_glass.wait_sms_stack()
        self.tele_page_glass.two_click_tp()
        time.sleep(3)
        self.tele_page_glass.check_sms_icon_disappear()
