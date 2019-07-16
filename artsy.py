import picamera
from time import sleep
from datetime import datetime, timedelta

# setup the camera such that it closes
# when we are done with it

# directory
directory = '/home/pi/Desktop/RPI/images/'

print('About to take some artsy pictures')


def currentTime():
    ct = datetime.now()
    picTime = ct.strftime('%m%d-%H%M%S')
    return picTime


def startTime():
    startTime = datetime.now().strftime('%S')
    return int(startTime)

# with picamera.PiCamera() as camera:
#     # take time to warm up the camera
#     camera.resolution = (1280, 720)
#     camera.vflip = True
#     camera.hflip = True

#     camera.start_preview()
#     frameCount = 0
#     running = False
#     start = True

#     # check start time
#     while start:
#         if startTime() == 0:
#             print(startTime())
#             start = False
#             running = True
#     print('It\'s time to take some pictures')

#     # capture loop
#     while running:
#         # camera.capture(filename)
#         filename = directory + 'art-' + currentTime() + '-' + str(frameCount) + '.jpg'
#         camera.capture(filename)
#         frameCount += 1
#         print(filename)
#         sleep(5)
#     camera.close()
# print('Pictures were taken, goodbye')
