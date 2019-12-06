import picamera
import os
from time import sleep
from datetime import datetime, timedelta
import sys

# directory
directory = '/home/pi/Desktop/rec/'
print("test")

# variables
print('About to take some artsy video')


with picamera.PiCamera() as camera:
    # flips the camera based on the position
    camera.resolution = (1920, 1080)
    camera.vflip = False
    camera.hflip = False
    # waits for the camera to warm up

    print('It\'s time, it\'s time, it\'s time to make some frekin art')
    # check if the images folder is, if not create one
    if not os.path.exists(directory):
        os.mkdir(directory)
        print("Directory is Created ")
    else:
        print("Directory already exists")
    # set the name
    name = directory + datetime.now().strftime('%m%d%H%M')

    # show video
    camera.start_preview()
    camera.start_recording(name + ".h264")
    while True:
        print(datetime.now().strftime('%m%d%H%M%S'))
        sleep(60)
print('art is done, go home')
