import picamera
import os
from time import sleep
from datetime import datetime, timedelta

# directory
directory = ''

# variables
# time to wait for a new photo to be taken in seconds
timeToWait = 15
# hour to start and to finish the command
timeToStart = 4
timeToEnd = 23

# other values
frameCount = 0

print('About to take some artsy pictures')


def currentTime():
    ct = datetime.now()
    picTime = ct.strftime('%m%d-%H%M%S')
    return picTime


with picamera.PiCamera() as camera:
    # flips the camera based on the position
    camera.resolution = (1920, 1080)
    camera.vflip = False
    camera.hflip = False
    # Wait for the automatic gain control to settle
    sleep(2)
    # set the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g

    # start previe
    camera.start_preview()
    # waits for the start hour
    while int(datetime.now().strftime('%H')) != timeToStart:
        pass
        # print(datetime.now().strftime('%H'))

    print('It\'s time, it\'s time, it\'s time to make some frekin art')
    # set the directory name after the waiting is done
    directory = '/home/pi/Desktop/tests/' + datetime.now().strftime('%m%d') + '/'
    # create a new directory if it does not exist
    if not os.path.exists(directory):
        os.mkdir(directory)
        print("Directory ", directory,  " Created ")
    else:
        print("Directory ", directory,  " already exists")

    # capture loop
    # stops at the end hour
    while int(datetime.now().strftime('%H')) != timeToEnd:
        filename = directory + 'art-' + currentTime() + '-' + str(frameCount) + '.jpg'
        camera.capture(filename)
        frameCount += 1
        # print(datetime.now().strftime('%S'), frameCount)
        camera.shutter_speed = camera.exposure_speed
        g = camera.awb_gains
        camera.awb_gains = g
        sleep(timeToWait)
    camera.close()
print('art is done, go home')
