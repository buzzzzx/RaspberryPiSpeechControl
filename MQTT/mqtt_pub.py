# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2018/7/9 上午10:33'

"""
flag:
    - 0: Sensors
    - 1: Operation
"""

import paho.mqtt.client as mqtt
import time
import json

MQTT_Broker = "test.mosquitto.org"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic_Sensors = "/Home/XCXF1703/Sensors"
MQTT_Topic_Operation = "/Home/XCXF1703/Operation"


def on_connect(client, userdata, flags, rc):
    # print("Connected with result code " + str(rc))
    if rc != 0:
        pass
        print("Unable to connect to MQTT Broker...")
    else:
        print("Connected with MQTT Broker: " + str(MQTT_Broker))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)


def publish_data(json_data, flag):
    if flag == 0:
        MQTT_Topic = MQTT_Topic_Sensors
    else:
        MQTT_Topic = MQTT_Topic_Operation
    publish2topic(MQTT_Topic, json_data)
    print("Publishing data ...")


def publish2topic(topic, msg):
    client.publish(topic, msg)
    print("Published: " + str(msg) + " " + "on MQTT Topic: " + str(topic))
    print("")
