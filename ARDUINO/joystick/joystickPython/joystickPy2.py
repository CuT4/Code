
import serial
from serial import Serial
# import pyautogui

arduino_port="/dev/ttyACM0" #Serial port for comunication(ubuntu).
baud=9600#frecuency

ser=serial.Serial(arduino_port, baud)# Connect to /dev/ttyACM0 at 9600 bauds
print("Connected to the arduino port at ", baud, "bauds") # Confirm connection

while True:

    # Clear entire serial input buffer
    ser.reset_input_buffer()

    # Read and ignore the next line.
    # This solves the issue that if you start reading now, you 
    # may be starting in the middle of a line. So we'll discard
    # this possibly incomplete line.
    ser.readline()

    data=ser.readline().decode('utf-8').rstrip()
    print(data)

    # 'data' is now guaranteed to be a most recent, complete
    # line of measurement data from the Arduino.

   




   
