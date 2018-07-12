# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2018/7/7 上午10:49'

"""
使用：IBM 免费使用 100 分钟

1、注册，创建应用得到 API 用户名和密码
2、安装 speechrecognition: pip3 install speech_recognition

{
  "url": "https://stream.watsonplatform.net/speech-to-text/api",
  "username": "25a206d8-c68f-4081-bdac-6b2ce8bcee82",
  "password": "dCvuLd0uHtUN"
}

"""

import speech_recognition as sr
import time
import datetime
import sys
import io


def voice2text():
    start_time = datetime.datetime.now()
    print("开始转换")
    text = 'a'
    ##音频分块识别
    r = sr.Recognizer()
    try:
        with sr.WavFile(r'/home/pi/Downloads/RaspberryPiSpeechControl/VoiceManage/VoiceFiles/test1.wav') as source:
            audio = r.record(source)
            IBM_USERNAME = '25a206d8-c68f-4081-bdac-6b2ce8bcee82'
            IBM_PASSWORD = 'dCvuLd0uHtUN'
            text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, language='zh-CN')
            text = text.replace(' ', '')
            print(text)
            open(u'/home/pi/Downloads/RaspberryPiSpeechControl/VoiceManage/Texts/output.txt', 'a+', encoding='utf8').write(text)
            time.sleep(5)
            temptime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('%s 已完成' % (temptime))

    except Exception as e:
        print(e)
        temptime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('%s 未完成' % (temptime))

    jietime = datetime.datetime.now()
    last = jietime - start_time
    print('总共花费时间：%s' % last)
    return text


if __name__ == '__main__':
    text = voice2text()
    print(text)
