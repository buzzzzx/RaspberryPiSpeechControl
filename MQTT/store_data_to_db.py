# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2018/7/9 上午10:57'

"""
install: pip3 install pymysql

"""

import pymysql
import json

# mysql config
config = {
    'host': '47.94.14.4',
    'port': 3306,
    'user': 'root',
    'password': '',
    'db': 'Platform'
}


class DatabaseManager():
    def __init__(self):
        self.conn = pymysql.connect(**config)
        self.curr = self.conn.cursor()

    def add_record(self, sql_query):
        self.curr.execute(sql_query)
        self.conn.commit()

    def __del__(self):
        self.curr.close()
        self.conn.close()


def sensor_data_hander(topic, jsonData):
    jsonData = str(jsonData, encoding="utf-8")
    data_dict = json.loads(jsonData)
    if topic == "/Home/XCXF1703/Sensors":
        temperature = data_dict['temperature']
        humidity = data_dict['humidity']
        smoke = data_dict['gas_detected']
        create_time = data_dict['create_time']

        sql_query = "insert into sensors (temperature, humidity, smoke, create_time) values ('{}', '{}', '{}', '{}')".format(
            temperature, humidity, smoke, create_time)
    elif topic == "/Home/XCXF1703/Operation":
        device_id = data_dict['device_id']
        device_name = data_dict['device_name']
        order = data_dict['operate']
        create_time = data_dict['create_time']
        sql_query = "insert into operation (device_id, device_name, operate, create_time) values ('{}', '{}', '{}', '{}')".format(
            device_id, device_name, order, create_time)

    db_obj = DatabaseManager()

    db_obj.add_record(sql_query)

    del db_obj

    print("Inserted Sensors Data into Database.")
    print("")
