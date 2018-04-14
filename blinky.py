from picamera import PiCamera
import RPi.GPIO as IO
import time
GPIO.setwarnings(False)

IO.setmode(IO.BOARD)
IO.setup(40,IO.OUT)

camera = PiCamera()

camera.start_preview()
IO.output(40,1)
time.sleep(10)
camera.stop_preview()
IO.cleanup()
time.sleep(1)
