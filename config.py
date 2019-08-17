"""
Configuration file for Odisseus
"""

import RPi.GPIO as io

import cv2

# Flag indicating if we are on Pi or simply emulating
ON_RASP_PI = True

DEBUG = True
PORT =  5001
HOST = '0.0.0.0'

# The address of the I2C bus
I2CAddr = 0x00000000


SCREEN_SIZE = (320, 240)
ENCODE_PARAMS = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
INDEX_DISPLAY_TEMPLATE_NAME = 'image_server.html'
CAMERA_SLEEP_TIME = 0.05
NEEDED_CAMERA_ROTATION = 0.0

# configuration for multiprocessing
USE_MULTIPROCESSING = False
QUEUE_MAX_SIZE=2

display_queue = None
control_queue = None

from multiprocessing import Queue

control_queue = Queue()
display_queue = Queue(maxsize=QUEUE_MAX_SIZE)


io.setmode(io.BCM)

# the Pins Odisseus is using

IN_PIN_1_MOTOR_1 = 17
IN_PIN_2_MOTOR_1 = 22
ENA_MOTOR_1_PIN_ID = 25
#IN_PIN_3 = 20
#IN_PIN_4 = 21

# the IR sensor PIN ID
#IR_PIN_ID = 18

#io.setup(IN_PIN_1, io.OUT)
#io.setup(IN_PIN_2, io.OUT)
#io.setup(IN_PIN_3, io.OUT)
#io.setup(IN_PIN_4, io.OUT)