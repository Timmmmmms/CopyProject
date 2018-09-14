# -*- coding:utf-8 -*-
from aip import AipOcr
import configparser

class BaiDuAPI(object):
    # 用于识别文字

    def __init__(self):
        # target = configparser.ConfigParser()
        # target.read("password.ini")
        APPID = "11680264"
        APIKey = "Ck2fFHjcuZpDQQGgt24smxFu"
        SecretKey = "GQn1GuSdlIvjewI0mFvzuh6OCepRhehF"

        # 类内都可用
        self.client = AipOcr(APPID,APIKey,SecretKey)

    def picture2Text(self,filepath):
        # 读取图片
        image = self.getPicture(filepath)
        # 识别图片
        text = self.client.basicGeneral(image)

        print(text['words_result'][0]['words'])

    # 读取图片
    @staticmethod # 静态方法
    def getPicture(filepath):
        with open(filepath,'rb') as fp:
            return fp.read()

if __name__ == '__main__':
    baiduapi = BaiDuAPI()
    baiduapi.picture2Text('imageGrab.png')

