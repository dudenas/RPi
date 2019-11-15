import picamera
import os
from time import sleep
from datetime import datetime, timedelta
import sys

# directory
directory = ''

# variables
print('About to take some artsy pictures')
print('About to take some artsy pictures')


with picamera.PiCamera() as camera:
    # flips the camera based on the position
    camera.resolution = (1280, 720)
    camera.vflip = False
    camera.hflip = False
    print('test')
    # waits for the camera to warm up

    print('It\'s time, it\'s time, it\'s time to make some frekin art')
    # check if the images folder is, if not create one
    if not os.path.exists('/home/pi/Desktop/art/video/'):
        os.mkdir('/home/pi/Desktop/art/video/')
        print("Directory is Created ")
    else:
        print("Directory already exists")
    # set the directory name after the waiting is done
    directory = '/home/pi/Desktop/art/video/' + datetime.now().strftime('%m%d%M')
    camera.start_recording(directory + "_python_video.h264")
    sleep(10)
    camera.stop_recording()
print('art is done, go home')
