# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2018/7/7 上午9:58'

"""
read data: 
    mode: BOARD
    channel: 12
    GND: 14
    VCC: 04
    
store:
    gas_data: 0(未检测到) OR 1(检测到)
"""

import RPi.GPIO as GPIO
import time


def action(pin):
    global gas_detected
    gas_detected = 1
    print("Sensor detected action!")


def getdata():
    CHANNEL = 12
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    global gas_detected
    gas_detected = 0
    GPIO.add_event_detect(CHANNEL, GPIO.RISING)
    GPIO.add_event_callback(CHANNEL, action)

    time.sleep(0.5)
    GPIO.cleanup()
    return gas_detected


if __name__ == '__main__':
    aa = getdata()
    print(aa)
