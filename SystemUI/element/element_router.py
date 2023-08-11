#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

from common.config_parser import ReadConfig
from common.yaml_parser import ReadYaml
from SystemUI import root_dir

mapping = {
    "TelePagePhone": "system_notification_element_phone.yaml",
    "TelePageGlass": "system_notification_element_glass.yaml",
    "TelePageAuxiliary": "system_notification_element_auxil.yaml",
    "NotificationPagePhone": "mvp_notification_element_phone.yaml",
    "NotificationPageGlass": "mvp_notification_element_glass.yaml",
    "NotificationPageAuxiliary": "mvp_notification_element_auxil.yaml",
    "Data": "data.yaml",
    "MvpData": "mvp_data.yaml"
}


class ElementRouter:
    """定位元素选择路由"""

    @staticmethod
    def select(page_name, file_path):
        region = ReadConfig().get_region
        platform = ReadConfig().get_platform(root_dir.split('\\')[-1])
        filename = None
        if platform == "android":
            if region == "cn":
                filename = mapping.get(page_name)
        elif platform == "ios":
            pass
        if filename is None:
            raise TypeError("cannot find the mapping relationship for " + page_name)
        return ReadYaml().read(os.path.join(root_dir, file_path, filename))
