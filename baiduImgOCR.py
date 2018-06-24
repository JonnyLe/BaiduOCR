__author__ = 'Jonny',
#-*- coding:utf-8 -*-
#借助百度的aip智能库，进行图片的文字识别。获取图片中的文字信息

from aip import AipOcr

def signUp():
    """ 你的 APPID AK SK """
    APP_ID = '10745268'
    API_KEY = '5gceIUGsak6t376e2MolshkL'
    SECRET_KEY = 'yRBjSyN0LpyveVP4WnpUkOhubpnMWIt1'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    return client

def get_file_content(imgPath):
    with open (imgPath,'rb') as f:
        return f.read()

def get_img_word(img):
    """
    根据图片进行文字识别，并提取
    :param imgPath:
    :return: res，
    """
    flag = 1
    #调用可选参数
    options = {}
    #判断图片中的语言的类别
    options["language_type"] = "CHN_ENG"
    #判断图片是否有倾斜角度
    options["detect_direction"] = "true"
    #检测语言
    options["detect_language"] = "true"
    #检测识别的可信度
    options["probability"] = "true"
    # img = get_file_content(imgPath)
    #图片识别技术
    if flag ==1:
        # 高精度图片识别技术
        res = signUp().basicAccurate(img,options)
    else:
        # 通用精度图片识别技术
        res = signUp().basicGeneral(img,options)
    #print(res)
    return res


# 通用文字识别 返回示例
#
# {
# "log_id": 2471272194,
# "words_result_num": 2,
# "words_result":
#     [
#         {"words": " TSINGTAO"},
#         {"words": "青島睥酒"}
#     ]
# }
