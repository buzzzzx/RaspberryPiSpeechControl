# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2018/7/9 上午10:40'

import paho.mqtt.client as mqtt
from MQTT.store_data_to_db import sensor_data_hander

MQTT_Broker = "test.mosquitto.org"
MQTT_Port = 1883
Keep_Alive_Interval = 45
# MQTT_Topic = "Home/XCXF1703/#"
MQTT_Topic_Sensors = "/Home/XCXF1703/Sensors"
MQTT_Topic_Operation = "/Home/XCXF1703/Operation"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_Topic_Sensors)
    client.subscribe(MQTT_Topic_Operation)


def on_message(client, userdata, msg):
    print(msg.topic + ": " + str(msg.payload))
    # store data to db
    sensor_data_hander(msg.topic, msg.payload)


def mqtt_listen_data():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)
    client.loop_forever()


if __name__ == '__main__':
    mqtt_listen_data()
