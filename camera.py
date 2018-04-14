from picamera import PiCamera
import time
from time import sleep
import RPi.GPIO as GPIO


camera = PiCamera()

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.HIGH)
def blink():
    x = 0
    for x in range(0,3):
        GPIO.output(LedPin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LedPin, GPIO.LOW)
        time.sleep(1)
def destroy():
    GPIO.output(LedPin, GPIO.LOW)
    GPIO.cleanup()
        
setup()

camera.start_preview()
try:
    blink()
except KeyboardInterrupt:
    destroy()
sleep(10)
camera.stop_preview()
