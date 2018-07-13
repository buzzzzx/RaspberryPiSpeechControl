# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2018/7/9 下午5:12'

from Sensors import TemperatureHumidity, Gas

import RPi.GPIO as GPIO
import time
import datetime
import json
import threading
from MQTT import mqtt_pub


def sensor_data_collect_publish():
    try:
        threading.Timer(3.0, sensor_data_collect_publish).start()
        all_dict = {}
        dh_dict = TemperatureHumidity.getdata()
        gas_detected = Gas.getdata()
        create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        all_dict['temperature'] = dh_dict['temperature']
        all_dict['humidity'] = dh_dict['humidity']
        all_dict['gas_detected'] = gas_detected
        all_dict['create_time'] = create_time
        json_data = json.dumps(all_dict)
        print(json_data)
        # mqtt publish
        flag = 0
        mqtt_pub.publish_data(json_data, flag)

    except KeyboardInterrupt:
        print("Collect done...")


if __name__ == '__main__':
    # channel = 17
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # button

    # open mqtt-rec
    sensor_data_collect_publish()
    # SpeechControl()