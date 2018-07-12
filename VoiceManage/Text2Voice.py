# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2018/7/9 下午6:14'

"""
install: sudo apt-get install mplayer
"""

import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit'
                  '/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safar'
                  'i/537.36',
}


def text2voice(text):
    # per 是语音类型，2，3，5 比较可以
    url = 'http://tts.baidu.com/text2audio?idx=1&tex={0}&cuid=baidu_speech_' \
          'demo&cod=2&lan=zh&ctp=1&pdt=1&spd=4&per=3&vol=5&pit=5'.format(text)

    # # 下载转换后的 MP3 格式语音
    # res = requests.get(url, headers=headers)
    # # 将 MP3 存入本地
    # with open(r'VoiceFiles/erorr_remind.mp3', 'wb') as f:
    #     f.write(res.content)

    # 直接播放
    os.system('mplayer "%s"' % url)
