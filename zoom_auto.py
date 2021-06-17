# Author: u/CoconutJJ
# This software is free by all definitions of "free". You may modify/copy the
# source code to how you see fit for any purpose whatsoever. No attribution
# to the original author is required.

from signal import SIGINT
import pyautogui
import subprocess
import time
import sys
import tkinter as tk
import pyaudio
import cv2
import numpy as np
import signal
import ffmpeg
from PIL import ImageGrab
import os
import wave


def locateAndClick(imgUrl):
    
    
    while (loc := pyautogui.locateCenterOnScreen(imgUrl, grayscale=False, confidence=.5)) is None:
        print("Attempting to find matching GUI: " + imgUrl)
        continue

    pyautogui.click(loc)


def startRecordScreenProcess(outFileName, width, height):

    pid = os.fork()

    if pid == 0:
        stop = False

        def sigHandler(signal, frame):
            nonlocal stop
            stop = True

        signal.signal(SIGINT, sigHandler)

        fourcc = cv2.VideoWriter_fourcc(*'MP4V')

        vid = cv2.VideoWriter(outFileName, fourcc, 30, (width, height))

        while not stop:
            img = ImageGrab.grab(bbox=(0, 0, width, height))
            frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

            vid.write(frame)

        vid.release()
        sys.exit(0)
    else:
        return pid


def startRecordAudioProcess(outFileName):

    pid = os.fork()

    if pid == 0:

        stop = False

        def sigHandler(signal, frame):
            nonlocal stop
            stop = True

        signal.signal(SIGINT, sigHandler)

        p = pyaudio.PyAudio()

        systemSoundIndex = None

        for i in range(p.get_device_count()):

            device = p.get_device_info_by_index(i)

            if device["name"] == "pulse":
                systemSoundIndex = i
                break

        stream = p.open(format=pyaudio.paInt16, channels=2, rate=44100, input=True,
                        frames_per_buffer=1024, input_device_index=systemSoundIndex)

        waveFile = wave.open(outFileName, 'wb')

        waveFile.setnchannels(2)
        waveFile.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        waveFile.setframerate(44100)

        while not stop:
            data = stream.read(1024)
            waveFile.writeframes(data)

        waveFile.close()
        sys.exit(0)
    else:
        return pid


def zoomBot(basepath, meetingid, meetingpasscode, duration, filename):

    sub = subprocess.Popen("zoom")

    locateAndClick(basepath + "icons/meeting_join.png")
    locateAndClick(basepath + "icons/meeting_id_input.png")
    pyautogui.write(meetingid)
    locateAndClick(basepath + "icons/meeting_id_join.png")
    locateAndClick(basepath + "icons/meeting_password_input.png")
    pyautogui.write(meetingpasscode)
    locateAndClick(basepath + "icons/meeting_password_join.png")

    win = tk.Tk()

    screenPid = startRecordScreenProcess(
        "out.mp4", win.winfo_screenwidth(), win.winfo_screenheight())
    audioPid = startRecordAudioProcess("out.wav")

    time.sleep(int(duration * 60))

    os.kill(screenPid, SIGINT)
    os.kill(audioPid, SIGINT)
    try:
        os.waitpid(screenPid, os.WEXITED)
        os.waitpid(audioPid, os.WEXITED)
    except:
        pass

    video = ffmpeg.input('out.mp4')
    audio = ffmpeg.input('out.wav')
    try:
        os.remove(filename)
    except:
        pass

    out = ffmpeg.output(video, audio, filename, vcodec='copy',
                        acodec='aac', strict='experimental')
    out.run()

    os.remove("out.mp4")
    os.remove("out.wav")

    return


if __name__ == "__main__":

    basepath = "/".join(sys.argv[0].split('/')[:-1])

    if len(basepath) != 0:
        basepath += "/"

    print(basepath)

    if len(sys.argv) != 5:
        print("usage: " + sys.argv[0] +
              " [Zoom Meeting Id] [Zoom Meeting Password] [Duration in Minutes] [Out File]")
        exit(1)

    zoomBot(basepath, sys.argv[1], sys.argv[2],
            float(sys.argv[3]), sys.argv[4])
