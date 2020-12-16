# coding=utf-8
from PIL import ImageGrab
import numpy as np
import cv2
import os
import sys
from PublicModule import profile

class video_record():
    def __init__(self, name):
        self.name = name
        # self.file_dir = "R:\\%s\\Recod" %profile.http_server
        self.file_dir = "F:\\Recod"
        self.video_path="F:\\Record_csv"
    def deletevedio(self):
        os.listdir(self.video_path)
        pass

    def start(self):
        print("start Recording ........%s" %self.name)
        screen = ImageGrab.grab()  # 获取当前的屏幕
        width, high = screen.size  # 获取屏幕的大小
        # video_decode_style = cv2.VideoWriter_fourcc(*'XVID') # 编码格式
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')  #  MPEG-4编码,文件后缀可为.avi .asf
        # video = cv2.VideoWriter('R:\\%s\\%s.avi' %(profile.http_server,self.name), video_decode_style, 25, (length,width)) # 输出文件名为 ，帧率为32 可以调节
        # video = cv2.VideoWriter('F:\\Record_csv\\%s.avi' %(self.name), video_decode_style, 25, (width, high)) # 输出文件名为 ，帧率为32 可以调节
        video = cv2.VideoWriter('%s\\%s.avi' %(self.video_path,self.name), fourcc, 15, (width, high)) # （文件名，编码器，帧率，视频宽高）
  #print('3秒后开始录制----')  # 可选
        while True:
            im = ImageGrab.grab()  # 图片为RGB模式
            imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)  # 转为opencv的BGR 格式
            video.write(imm)   # 写入
            td = os.path.exists(self.file_dir)
            if not td:
                print("end Recording ...")
                break

        video.release()
        cv2.destroyAllWindows()

if __name__  ==  "__main__":
    name = sys.argv[1]
    r = video_record(name)
    r.start()
