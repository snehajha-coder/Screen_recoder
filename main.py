import datetime

from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

time_stamp = datetime.datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
file_name = f'screen recoder {time_stamp}.mp4'
print(file_name)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (1920, 1080))

webcam = cv2.VideoCapture(0)

while True:
    img = ImageGrab.grab(bbox=(0,0,1920,1080))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    _, frame = webcam.read()
    fr_height, fr_width, _ = frame.shape
    fr_widthn = int(fr_width/3)
    fr_heightn = int(fr_height/3)
    #resized_frame = cv2.resize(frame, (176, 144))
    resized_frame = cv2.resize(frame, (fr_widthn, fr_heightn))

    #img_final[0:144, 0: 176] = resized_frame[0:144, 0: 176]
    img_final[0:fr_heightn, 0: fr_widthn] = resized_frame[0:fr_heightn, 0: fr_widthn]


    cv2.imshow('Secret Capture', img_final)

    #cv2.imshow('webcam', frame)
    captured_video.write(img_final)

    if cv2.waitKey(10) == ord('q'):
        break