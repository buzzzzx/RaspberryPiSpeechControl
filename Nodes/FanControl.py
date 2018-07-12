# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2018/7/7 上午10:14'

"""
mode: BOARD
channel: 32
GND: 30
"""

import RPi.GPIO as GPIO
import time

channel = 32
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