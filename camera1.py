from picamera import PiCamera
from time import sleep
import RPi.GPIO as IO

camera = PiCamera()
IO.setmode(IO.BOARD)
IO.setup(40,IO.OUT)

IO.output(40,0)
camera.start_preview()
IO.output(40,1)
sleep(5)
IO.cleanup()
sleep(1)
camera.stop_preview()
