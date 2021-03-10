#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

bri = 255
change = -1
while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    #  Do some 'work'
    # time.sleep(1)

    # simple logic
    bri = (bri + change)
    if bri == 0:
        change = 1
    elif bri == 255:
        change = -1

    #  Send reply back to client
    socket.send(bytes(str(bri), 'utf8'))
