# -*- coding:utf-8 -*-

# 实现截图

# 控制键盘事件
import time
import sys

import keyboard
from PIL import ImageGrab

from baiDu import BaiDuAPI

def screenShot(filepath):
    if keyboard.wait(hotkey='ctrl+Q') == None:
        time.sleep(3)
        # 读取剪切板里面的图片
        im = ImageGrab.grabclipboard()
        # 保存
        im.save(filepath)

if __name__ =="__main__":
    filepath = "imageGrab.png"
    baiduapi = BaiDuAPI()
    while True:
        print("截取一张图片")
        screenShot(filepath)
        print("正在读取。。。。")
        baiduapi.picture2Text(filepath)