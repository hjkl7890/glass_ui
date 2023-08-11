#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Author   : chuanwen.peng
# @Time     : 2022/11/14 14:48
# @File     : test_notification_message.py
# @Project  : glass_ui
"""
import allure
import pytest
import inspect

from SystemUI.flow.notification_flow import TeleFlow
from SystemUI import root_dir
from common.config_parser import ReadConfig

devices_dic = ReadConfig().get_package_name(root_dir.split('\\')[-1])
devices = [i for i in list(devices_dic.keys())]
data_list = []
for num in range(len(devices)):
    locals()['test_data' + str(num)] = [
        {
            "app_name": root_dir.split('\\')[-1],
            "devices": devices[num]
        }]
    data_list.append(locals()['test_data' + str(num)])


@allure.epic("电话通知")
class TestTelephoneNotification:
    @allure.feature("76272")
    @allure.title("来电未接听时通知显示")
    @pytest.mark.D
    @pytest.mark.run(order=0)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_display_no_answer(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.call_check_no_answer_display(inspect.stack()[0][3])

    @allure.feature("76273")
    @allure.title("通话中通知显示")
    @pytest.mark.D
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_display_in_call(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.call_check_in_call_display()

    @allure.feature("76277")
    @allure.title("来电未接听时辅助手机挂断电话")
    @pytest.mark.D
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_call_auxiliary_hangup(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.call_no_answer_auxiliary_hangup()

    @allure.feature("76278")
    @allure.title("来电未接听时测试手机挂断电话")
    @pytest.mark.D
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_call_phone_hangup(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.call_no_answer_test_hangup()

    @allure.feature("76279")
    @allure.title("来电未接听时眼镜端挂断电话")
    @pytest.mark.D
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_call_glass_hangup(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.call_no_answer_glass_hangup()

    @allure.feature("76280")
    @allure.title("来电通知测试机接听")
    @pytest.mark.D
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_call_phone_answer(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.call_phone_answer()

    @allure.feature("76281")
    @allure.title("来电通知眼镜端接听")
    @pytest.mark.D
    @pytest.mark.run(order=6)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_call_glass_answer(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.call_glass_answer()

    @allure.feature("76282")
    @allure.title("通话中辅助手机挂断电话")
    @pytest.mark.D
    @pytest.mark.run(order=7)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_in_call_auxiliary_hangup(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.in_call_auxiliary_hangup()

    @allure.feature("76283")
    @allure.title("通话中测试手机挂断电话")
    @pytest.mark.D
    @pytest.mark.run(order=8)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_in_call_phone_hangup(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.in_call_phone_hangup()

    @allure.feature("76284")
    @allure.title("通话中眼镜端挂断电话")
    @pytest.mark.D
    @pytest.mark.run(order=9)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_in_call_glass_hangup(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.in_call_glass_hangup()

    @allure.feature("76285")
    @allure.title("收到来电时不进行任何操作")
    @pytest.mark.D
    @pytest.mark.run(order=10)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_do_nothing_when_call(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.do_nothing_when_call()

    @allure.feature("76286")
    @allure.title("1h内通话时长显示")
    @pytest.mark.D
    @pytest.mark.run(order=11)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_in_call_within1h(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.display_within1h()

    @allure.feature("76288")
    @allure.title("来电时单指单击tp")
    @pytest.mark.D
    @pytest.mark.run(order=12)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_call_oneclick_tp(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.call_oneclick_tp()

    @allure.feature("76289")
    @allure.title("来电时单指双击tp")
    @pytest.mark.D
    @pytest.mark.run(order=13)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_call_two_click_tp(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.call_two_click_tp()

    @allure.feature("76290")
    @allure.title("来电时短按Power键")
    @pytest.mark.D
    @pytest.mark.run(order=14)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_call_click_power(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.call_click_power()

    @allure.feature("76292")
    @allure.title("通话中单指单击tp")
    @pytest.mark.D
    @pytest.mark.run(order=15)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_in_call_oneclick_tp(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.in_call_oneclick_tp()

    @allure.feature("76293")
    @allure.title("通话中单指长按tp")
    @pytest.mark.D
    @pytest.mark.run(order=16)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_in_call_long_press_tp(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.in_call_long_press_tp()

    @allure.feature("76294")
    @allure.title("通话中单指双击tp")
    @pytest.mark.D
    @pytest.mark.run(order=17)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_in_call_two_click_tp(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.in_call_two_click_tp()

    @allure.feature("76295")
    @allure.title("通话中短按Power键")
    @pytest.mark.D
    @pytest.mark.run(order=18)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_in_call_click_power(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.in_call_click_power()

    @allure.feature("76351")
    @allure.title("播放音乐时来电")
    @pytest.mark.S
    @pytest.mark.run(order=19)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_music_incoming(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.music_incoming()

    @allure.feature("76353")
    @allure.title("播放音乐时来电并接听")
    @pytest.mark.S
    @pytest.mark.run(order=20)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_music_incoming_answer(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.music_incoming_answer()

    @allure.feature("76354")
    @allure.title("播放视频时来电")
    @pytest.mark.D
    @pytest.mark.run(order=21)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_video_incoming(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.video_incoming()

    @allure.feature("76356")
    @allure.title("导航时来电")
    @pytest.mark.S
    @pytest.mark.run(order=22)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_navi_incoming(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.navi_incoming(inspect.stack()[0][3])

    @allure.feature("76358")
    @allure.title("使用AR名片时来电")
    @pytest.mark.S
    @pytest.mark.run(order=23)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_card_incoming(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.card_incoming()

    @allure.feature("76291")
    @allure.title("来电时连续多次短按Power键")
    @pytest.mark.S
    @pytest.mark.run(order=24)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_incoming_several_power(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.incoming_several_power()

    @allure.feature("76296")
    @allure.title("通话中连续多次短按Power键")
    @pytest.mark.S
    @pytest.mark.run(order=25)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_in_call_several_power(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.in_call_several_power()

    @allure.feature("76378")
    @allure.title("通话中唤醒AI语音助理")
    @pytest.mark.S
    @pytest.mark.run(order=26)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_in_call_ai_voice(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.in_call_ai_voice()

    @allure.feature("76377")
    @allure.title("来电未接听时唤醒AI语音助理")
    @pytest.mark.S
    @pytest.mark.run(order=27)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_incoming_ai_voice(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.incoming_ai_voice()


@allure.epic("短信通知")
class TestSMSNotification:
    @allure.feature("76301")
    @allure.title("短信通知显示")
    @pytest.mark.S
    @pytest.mark.run(order=0)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_display_sms_notification(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        sms_flow = TeleFlow(driver_list)
        sms_flow.display_sms_notification(inspect.stack()[0][3])

    @allure.feature("76306")
    @allure.title("信息展示5s无操作后自动消失")
    @pytest.mark.S
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_sms_display_5s(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        sms_flow = TeleFlow(driver_list)
        sms_flow.sms_display_5s(inspect.stack()[0][3])

    @allure.feature("76307")
    @allure.title("单指双击tp关闭短信通知")
    @pytest.mark.S
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_sms_two_click_tp(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        sms_flow = TeleFlow(driver_list)
        sms_flow.sms_two_click_tp(inspect.stack()[0][3])

    @allure.feature("76308")
    @allure.title("TouchPad前后滑动查看长文本信息")
    @pytest.mark.S
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_swipe_view_long_sms(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        sms_flow = TeleFlow(driver_list)
        sms_flow.swipe_view_long_sms(inspect.stack()[0][3])

    @allure.feature("76311")
    @allure.title("Touchpad滑动过程中收到其他通知")
    @pytest.mark.S
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_swipe_receive_new_sms(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        sms_flow = TeleFlow(driver_list)
        sms_flow.swipe_receive_new_sms(inspect.stack()[0][3])

    @allure.feature("76312")
    @allure.title("长文本自动滚动过程中收到其他通知")
    @pytest.mark.S
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_roll_receive_new_sms(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        sms_flow = TeleFlow(driver_list)
        sms_flow.roll_receive_new_sms(inspect.stack()[0][3])

    @allure.feature("76313")
    @allure.title("长文本自动滚动过程短按power键熄屏/亮屏")
    @pytest.mark.S
    @pytest.mark.run(order=6)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_roll_power(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        sms_flow = TeleFlow(driver_list)
        sms_flow.roll_power(inspect.stack()[0][3])

    @allure.feature("76315")
    @allure.title("手动滑动至底部后不再自动滚动展示")
    @pytest.mark.S
    @pytest.mark.run(order=7)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_swipe_no_roll(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        sms_flow = TeleFlow(driver_list)
        sms_flow.swipe_no_roll(inspect.stack()[0][3])


@allure.epic("系统通知")
class TestSystemNotification:
    @allure.feature("76316")
    @allure.title("低电量提醒（15%）")
    @pytest.mark.S
    @pytest.mark.run(order=0)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_low_battery_reminder(self, driver, driver2, start_stop_app, start_stop_app2):
        driver_list = [driver, driver2]
        system_flow = TeleFlow(driver_list)
        system_flow.low_battery_reminder(inspect.stack()[0][3])

    @allure.feature("76317")
    @allure.title("电量充满提醒（100%）")
    @pytest.mark.S
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_full_battery_reminder(self, driver, driver2, start_stop_app, start_stop_app2):
        driver_list = [driver, driver2]
        system_flow = TeleFlow(driver_list)
        system_flow.full_battery_reminder(inspect.stack()[0][3])

    @allure.feature("76321")
    @allure.title("关机确认弹窗检查")
    @pytest.mark.S
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_shutdown_confirm_popup(self, driver, driver2, start_stop_app, start_stop_app2):
        driver_list = [driver, driver2]
        system_flow = TeleFlow(driver_list)
        system_flow.shutdown_confirm_popup(inspect.stack()[0][3])

    @allure.feature("76352")
    @allure.title("播放音乐时收到弹窗通知")
    @pytest.mark.S
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_music_shutdown_confirm(self, driver, driver2, start_stop_app, start_stop_app2):
        driver_list = [driver, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.music_shutdown_confirm(inspect.stack()[0][3])

    @allure.feature("76355")
    @allure.title("播放视频时收到弹窗通知")
    @pytest.mark.S
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_video_shutdown_confirm(self, driver, driver2, start_stop_app, start_stop_app2):
        driver_list = [driver, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.video_shutdown_confirm(inspect.stack()[0][3])

    @allure.feature("76357")
    @allure.title("导航时收到弹窗通知")
    @pytest.mark.S
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_navi_shutdown_confirm(self, driver, driver2, start_stop_app, start_stop_app2):
        driver_list = [driver, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.navi_shutdown_confirm(inspect.stack()[0][3])

    @allure.feature("76359")
    @allure.title("使用AR名片时收到弹窗通知")
    @pytest.mark.S
    @pytest.mark.run(order=6)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_card_shutdown_confirm(self, driver, driver2, start_stop_app, start_stop_app2):
        driver_list = [driver, driver2]
        tele_flow = TeleFlow(driver_list)
        tele_flow.card_shutdown_confirm(inspect.stack()[0][3])


@allure.epic("应用通知")
class TestAppNotification:
    @allure.feature("76322")
    @allure.title("应用通知显示")
    @pytest.mark.S
    @pytest.mark.run(order=0)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_app_notification_display(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        app_flow = TeleFlow(driver_list)
        app_flow.app_notification_display(inspect.stack()[0][3])

    @allure.feature("76323")
    @allure.title("长文本IM消息")
    @pytest.mark.S
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_long_text_im_message(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        app_flow = TeleFlow(driver_list)
        app_flow.long_text_im_message(inspect.stack()[0][3])

    @allure.feature("76326")
    @allure.title("信息展示5s无操作后自动消失")
    @pytest.mark.S
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_im_display_5s(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        app_flow = TeleFlow(driver_list)
        app_flow.im_display_5s(inspect.stack()[0][3])

    @allure.feature("76327")
    @allure.title("单指双击tp关闭IM通知")
    @pytest.mark.S
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_im_two_click_tp(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        app_flow = TeleFlow(driver_list)
        app_flow.im_two_click_tp(inspect.stack()[0][3])

    @allure.feature("76328")
    @allure.title("TouchPad前后滑动查看长文本信息")
    @pytest.mark.S
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_swipe_view_long_im(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        app_flow = TeleFlow(driver_list)
        app_flow.swipe_view_long_im(inspect.stack()[0][3])

    @allure.feature("76330")
    @allure.title("手动滑动至底部后不再自动滚动展示")
    @pytest.mark.S
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_swipe_no_roll_im(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        app_flow = TeleFlow(driver_list)
        app_flow.swipe_no_roll_im(inspect.stack()[0][3])

    @allure.feature("76332")
    @allure.title("其他通知")
    @pytest.mark.S
    @pytest.mark.run(order=6)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_other_notification(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        app_flow = TeleFlow(driver_list)
        app_flow.other_notification(inspect.stack()[0][3])


@allure.epic("通知规则")
class TestNotificationRule:
    @allure.feature("76333")
    @allure.title("通知展示5s没有交互自动消失")
    @pytest.mark.S
    @pytest.mark.run(order=0)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_notification_display_5s(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        rule_flow = TeleFlow(driver_list)
        rule_flow.notification_display_5s(inspect.stack()[0][3])

    @allure.feature("76334")
    @allure.title("多条通知展示5s没有交互自动消失")
    @pytest.mark.S
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_multiple_notifications_5s(self, driver, driver1, driver2, start_stop_app, start_stop_app1,
                                       start_stop_app2):
        driver_list = [driver, driver1, driver2]
        rule_flow = TeleFlow(driver_list)
        rule_flow.multiple_notifications_5s(inspect.stack()[0][3])

    @allure.feature("76335")
    @allure.title("通知未消失时熄屏或关机")
    @pytest.mark.S
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_notification_power(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        rule_flow = TeleFlow(driver_list)
        rule_flow.notification_power(inspect.stack()[0][3])

    @allure.feature("76337")
    @allure.title("同类型通知按最新时间收纳展示")
    @pytest.mark.S
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_multiple_notifications_display_latest(self, driver, driver1, driver2, start_stop_app, start_stop_app1,
                                                   start_stop_app2):
        driver_list = [driver, driver1, driver2]
        rule_flow = TeleFlow(driver_list)
        rule_flow.multiple_notifications_display_latest(inspect.stack()[0][3])

    @allure.feature("76338")
    @allure.title("多条通知堆叠显示")
    @pytest.mark.S
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_multiple_notifications_stack_display(self, driver, driver1, driver2, start_stop_app, start_stop_app1,
                                                  start_stop_app2):
        driver_list = [driver, driver1, driver2]
        rule_flow = TeleFlow(driver_list)
        rule_flow.multiple_notifications_stack_display(inspect.stack()[0][3])

    @allure.feature("76339")
    @allure.title("来电通知第一优先级展示")
    @pytest.mark.S
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_call_first_display(self, driver, driver1, driver2, start_stop_app, start_stop_app1, start_stop_app2):
        driver_list = [driver, driver1, driver2]
        rule_flow = TeleFlow(driver_list)
        rule_flow.call_first_display(inspect.stack()[0][3])

    @allure.feature("76340")
    @allure.title("通话中多通知展示规则")
    @pytest.mark.S
    @pytest.mark.run(order=6)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_in_call_notifications_display(self, driver, driver1, driver2, start_stop_app, start_stop_app1,
                                           start_stop_app2):
        driver_list = [driver, driver1, driver2]
        rule_flow = TeleFlow(driver_list)
        rule_flow.in_call_notifications_display(inspect.stack()[0][3])

    @allure.feature("76341")
    @allure.title("多通知tp交互")
    @pytest.mark.S
    @pytest.mark.run(order=7)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_multi_notification_tp_interaction(self, driver, driver1, driver2, start_stop_app, start_stop_app1,
                                               start_stop_app2):
        driver_list = [driver, driver1, driver2]
        rule_flow = TeleFlow(driver_list)
        rule_flow.multi_notification_tp_interaction(inspect.stack()[0][3])

    @allure.feature("76342")
    @allure.title("弹窗优先级高于非来电未接听通知")
    @pytest.mark.S
    @pytest.mark.run(order=8)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_shutdown_higher_notification(self, driver, driver1, driver2, start_stop_app, start_stop_app1,
                                          start_stop_app2):
        driver_list = [driver, driver1, driver2]
        rule_flow = TeleFlow(driver_list)
        rule_flow.shutdown_higher_notification(inspect.stack()[0][3])

    @allure.feature("76343")
    @allure.title("多条通知时通知自动关闭逻辑")
    @pytest.mark.S
    @pytest.mark.run(order=9)
    @pytest.mark.parametrize('driver', data_list[0], indirect=True)
    @pytest.mark.parametrize('driver1', data_list[1], indirect=True)
    @pytest.mark.parametrize('driver2', data_list[2], indirect=True)
    def test_multi_notification_auto_close(self, driver, driver1, driver2, start_stop_app, start_stop_app1,
                                           start_stop_app2):
        driver_list = [driver, driver1, driver2]
        rule_flow = TeleFlow(driver_list)
        rule_flow.multi_notification_auto_close(inspect.stack()[0][3])
