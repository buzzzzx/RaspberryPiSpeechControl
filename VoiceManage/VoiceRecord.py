# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2018/7/7 上午10:16'

"""
record 5s voice

prepare:
    sudo apt-get install portaudio19-dev
    pip install pyaudio
"""

import pyaudio
import wave
import os
import sys

def voicerecord():
    CHUNK = 512
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "/home/pi/Downloads/RaspberryPiSpeechControl/VoiceManage/VoiceFiles/test1.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("recording...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("done")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

if __name__ == '__main__':
    voicerecord()