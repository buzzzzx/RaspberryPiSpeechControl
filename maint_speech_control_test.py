from VoiceManage import VoiceRecord, Voice2Text, VoiceRecogitive, Text2Voice
from Nodes import LedControl, FanControl
from Sensors import TemperatureHumidity, Gas
from MQTT import mqtt_pub

import RPi.GPIO as GPIO
import time
import datetime
import json
import threading


def SpeechControl():
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
            dict_data['operate'] = order
            dict_data['create_time'] = create_time
            json_data = json.dumps(dict_data)
            print(json_data)
            # mqtt publish
            flag = 1
            mqtt_pub.publish_data(json_data, flag)

            time.sleep(0.2)
        time.sleep(0.1)

if __name__ == '__main__':
    channel = 37
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # button

    # open mqtt-rec
    # sensor_data_collect_publish()
    SpeechControl()