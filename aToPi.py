import serial, string, time

output = " "
ser = serial.Serial('/dev/ttyACMO', 9600, 8, 'N', 1, timeout=1)

for i in range(0,256):
    print unichr(i)
    ser.write(chr(i))
    time.sleep(1)
              

