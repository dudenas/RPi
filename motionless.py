import picamera
import os
from time import sleep
from datetime import datetime, timedelta

# directory
directory = ''

# variables
# time to wait for a new photo to be taken in seconds
timeToWait = 15

# other values
frameCount = 0

print('About to take some artsy pictures')


def currentTime():
    ct = datetime.now()
    picTime = ct.strftime('%m%d-%H%M%S')
    return picTime


with picamera.PiCamera() as camera:
    # flips the camera based on the position
    camera.resolution = (1280, 720)
    camera.vflip = False
    camera.hflip = False
    # start preview
    camera.start_preview()
    # waits for the camera to warm up
    sleep(2)

    print('It\'s time, it\'s time, it\'s time to make some frekin art')
    # set the directory name after the waiting is done
    counter = 0
    directory = '/home/pi/Desktop/tests/' + datetime.now().strftime('%m%d') + \
        '_' + str(counter) + '/'
    # check if the directory exists
    while os.path.exists(directory):
        counter += 1
        directory = '/home/pi/Desktop/tests/' + datetime.now().strftime('%m%d') + \
            '_' + str(counter) + '/'
    # create a new directory
    os.mkdir(directory)
    print("Directory ", directory,  " is Created")

    # capture loop
    # never freakin stops
    while True:
        filename = directory + 'art-' + currentTime() + '-' + str(frameCount) + '.jpg'
        camera.capture(filename)
        frameCount += 1
        sleep(timeToWait)
    camera.close()
print('art is done, go home')
