# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2018/7/7 上午12:01'

"""
read data:
    mode: BCM
    channel: 14(08)
    GND: 06
    VCC: 02
store data:
    mqtt publish
"""

import Adafruit_DHT


def getdata():
    dh_dict = {}
    sensor1 = Adafruit_DHT.DHT11
    channel = 14
    humidity_data, temperature_data = Adafruit_DHT.read_retry(sensor1, channel)
    dh_dict['humidity'] = humidity_data
    dh_dict['temperature'] = temperature_data
    print(humidity_data, temperature_data)
    return dh_dict

if __name__ == '__main__':
    aa = getdata()
    print(aa)
