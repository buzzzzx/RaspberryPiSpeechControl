# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2018/7/7 上午10:08'

"""
mode: BOARD
channel: 36
GND: 34
"""

import RPi.GPIO as GPIO
import time

channel = 36
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.OUT)


def set(order):
    if order == 1:
        state = GPIO.HIGH
    else:
        state = GPIO.LOW

    GPIO.output(channel, state)
    time.sleep(0.2)

if __name__ == '__main__':
    set(0)