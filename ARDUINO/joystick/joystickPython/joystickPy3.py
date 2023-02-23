import pyautogui
import serial
from serial import Serial
# import pyautogui

pyautogui.FAILSAFE=False
screenWidth, screenHeight=pyautogui.size()
print(screenWidth, " x ", screenHeight, " resolution")

arduino_port="/dev/ttyACM0" #Serial port for comunication(ubuntu).
baud=9600#frecuency

ser=serial.Serial(arduino_port, baud)# Connect to /dev/ttyACM0 at 9600 bauds
print("Connected to the arduino port at ", baud, "bauds") # Confirm connection

while True:#comentario de prueba

    # Clear entire serial input buffer
    ser.reset_input_buffer()

    # Read and ignore the next line.
    # This solves the issue that if you start reading now, you 
    # may be starting in the middle of a line. So we'll discard
    # this possibly incomplete line.
    ser.readline()

    data=ser.readline().decode('utf-8').rstrip()

    xy=data.split(",")
    # print("X: ", xy[0], ", Y: ", xy[1])# Consider that the values printed are strings

    """
    It's necesary ot reduce the values obtained from the joystic because
    if not it would be a dissaster. It's important to take in count that the 
    values 500 in the x and y axis from the joystic should be the 0 in pyautogui.
    """
    pyX=int(xy[0])-509 #to set the non-movement to cero
    pyY=int(xy[1])-507 #to set the non-movement to cero
    print(pyX, ", ", pyY)
    pyautogui.move(pyX, pyY)

    # 'data' is now guaranteed to be a most recent, complete
    # line of measurement data from the Arduino.