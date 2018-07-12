# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2018/7/9 下午5:12'

"""
「operation time」 need done.

Button setting:
    mode: BCM
    channel: 17
    GND: 09
    VCC: 01

Device:
    - 001: Led
    - 002: Fan

flag:
    - 0: Sensors
    - 1: Operation

"""
from VoiceManage import VoiceRecord, Voice2Text, VoiceRecogitive, Text2Voice
from Nodes import LedControl, FanControl
from Sensors import TemperatureHumidity, Gas
from MQTT import mqtt_pub, mqtt_rec

import RPi.GPIO as GPIO
import time
import datetime
import json
import threading


def sensor_data_collect_publish():
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
    # mqtt publish
    flag = 0
    mqtt_pub.publish_data(json_data, flag)


def speech_control():

    try:

        while True:
            if GPIO.input(channel) == GPIO.HIGH:
                print("button pressed!")
                dict_data = {}
                VoiceRecord.voicerecord()
                text = Voice2Text.voice2text()
                result_dict = VoiceRecogitive.vocierecognitive(text)
                device = result_dict['device']
                order = result_dict['order']
                create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                if device == 'Led':
                    device_id = '001'
                    LedControl.set(order)
                elif device == 'Fan':
                    device_id = '002'
                    FanControl.set(order)
                else:
                    # 错误提醒
                    error_msg = "语音输入有误，请重新尝试"
                    Text2Voice.text2voice(error_msg)
                    continue

                dict_data['device_id'] = device_id
                dict_data['device_name'] = device
                dict_data['state'] = order
                dict_data['create_time'] = create_time
                json_data = json.dumps(dict_data)
                # mqtt publish
                flag = 1
                mqtt_pub.publish_data(json_data, flag)

                time.sleep(0.2)
            time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("quit.")


if __name__ == '__main__':
    channel = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # button
    # mqtt listening 【Problem】
    mqtt_rec.mqtt_listen_data()
    # get sensor data and publish by mqtt
    sensor_data_collect_publish()
    # speech control part
    speech_control()
