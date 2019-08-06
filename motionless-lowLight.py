import picamera
import os
from time import sleep
from datetime import datetime, timedelta

# directory
directory = ''

# variables
# time to wait for a new photo to be taken in seconds
timeToWait = 5

# other values
frameCount = 0

print('About to take some artsy pictures')


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
    counter = 0
    # check if the images folder is, if not create one
    if not os.path.exists('/home/pi/Desktop/tests/images/'):
        os.mkdir('/home/pi/Desktop/tests/images/')
        print("Directory is Created ")
    else:
        print("Directory already exists")
    # set the directory name after the waiting is done
    directory = '/home/pi/Desktop/tests/images/' + datetime.now().strftime('%m%d') + \
        '_' + str(counter) + '/'
    # check if the directory exists
    while os.path.exists(directory):
        counter += 1
        directory = '/home/pi/Desktop/tests/images/' + datetime.now().strftime('%m%d') + \
            '_' + str(counter) + '/'
    # create a new directory
    os.mkdir(directory)
    print("Directory ", directory, " is Created")

    # capture loop
    # never freakin stops
    while True:
        filename = directory + 'art' + str(frameCount) + '.jpg'
        camera.capture(filename)
        frameCount += 1
        sleep(timeToWait)
    camera.close()
print('art is done, go home')
