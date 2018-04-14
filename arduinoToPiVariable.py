from picamera import PiCamera
from time import sleep
import RPi.GPIO as IO
import serial

IO.setmode(IO.BOARD)
IO.setup(40,IO.OUT)
camera = PiCamera()
ser = serial.Serial('/dev/ttyACM0', 9600)

IO.output(40,0)

while (True):
    data = ser.readline()
    s = data
    if (data):
        sleep(1)
        camera.start_preview()
        IO.output(40,1)
        sleep(5)
    else :
        sleep(1)
        camera.stop_preview()
        IO.cleanup()
        camera.stop_preview()
        sleep(1) 

camera.stop_preview()
