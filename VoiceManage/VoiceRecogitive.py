# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2018/7/7 上午10:54'

"""
order:
    - 1: open
    - 0: close

device:
    - Led
    - Fan

"""


def vocierecognitive(text):
    result_dict = {}
    if '热' in text:
        device = 'Fan'
        order = 1
    elif '冷' in text:
        device = 'Fan'
        order = 0
    elif '黑' in text:
        device = 'Led'
        order = 1
    elif '睡觉' in text:
        device = 'Led'
        order = 0
    else:
        device = None
        order = None

    result_dict['device'] = device
    result_dict['order'] = order

    return result_dict


if __name__ == '__main__':
    text = "巴拉扒拉扒拉扒拉扒了"
    r = vocierecognitive(text)
    print(r['device'], r['order'])
