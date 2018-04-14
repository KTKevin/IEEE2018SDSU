# Needed modules will be imported and configured.
import RPi.GPIO as GPIO
import time
   
GPIO.setmode(GPIO.BCM)
   
# Declaration of the LED and sensor pins
LED_PIN = 24
Sensor_PIN = 23
GPIO.setup(Sensor_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
   

   
# This output function will be started at signal detection
def ausgabeFunktion(null):
        GPIO.output(LED_PIN, True)
   
# This output function will be started at signal detection 
GPIO.add_event_detect(Sensor_PIN, GPIO.FALLING, callback=ausgabeFunktion, bouncetime=10) 
   
# main program loop
bolFall =0;

try:
        while True:
                time.sleep(1)
                if GPIO.input(Sensor_PIN):
                        GPIO.output(LED_PIN, False)
                        

# Scavenging work after the program has ended
except KeyboardInterrupt:
        GPIO.cleanup()
