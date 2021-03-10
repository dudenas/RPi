#!/usr/bin/python
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# ultrasonic_2.py
# Measure distance using an ultrasonic module
# in a loop.
#
# Author : Matt Hawkins
# Date   : 28/01/2013

# -----------------------
# Import required Python libraries
# -----------------------
import time
import RPi.GPIO as GPIO

# -----------------------
# Define some functions
# -----------------------


def measure(GPIO_TRIGGER, GPIO_ECHO):
    # This function measures a distance
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        start = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        stop = time.time()

    elapsed = stop-start
    distance = (elapsed * 34300)/2

    return distance


def measure_average(GPIO_TRIGGER, GPIO_ECHO):
    # This function takes 3 measurements and
    # returns the average.
    distance1 = measure(GPIO_TRIGGER, GPIO_ECHO)
    time.sleep(0.1)
    distance2 = measure(GPIO_TRIGGER, GPIO_ECHO)
    time.sleep(0.1)
    distance3 = measure(GPIO_TRIGGER, GPIO_ECHO)
    distance = distance1 + distance2 + distance3
    distance = distance / 3
    return distance


def setGPIOpins(GPIO_TRIGGER, GPIO_ECHO):
    # Set pins as output and input
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)  # Trigger
    GPIO.setup(GPIO_ECHO, GPIO.IN)      # Echo

    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER, False)


# -----------------------
# Main Script
# -----------------------


# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:
    print("Ultrasonic Measurement")

    # Define GPIO to use on Pi
    GPIO_TRIGGER_1 = 22
    GPIO_ECHO_1 = 23
    setGPIOpins(GPIO_TRIGGER_1, GPIO_ECHO_1)

    GPIO_TRIGGER_2 = 24
    GPIO_ECHO_2 = 25
    setGPIOpins(GPIO_TRIGGER_2, GPIO_ECHO_2)

    while True:
        distance_1 = measure_average(GPIO_TRIGGER_1, GPIO_ECHO_1)
        distance_2 = measure_average(GPIO_TRIGGER_2, GPIO_ECHO_2)
        print(f"Distance-1 : {distance_1:.1f} | Distance-2 : {distance_2:.1f}")
        # print(f"Distance-1 : {distance_1:.1f}")
        time.sleep(1)

except KeyboardInterrupt:
    # User pressed CTRL-C
    # Reset GPIO settings
    GPIO.cleanup()
