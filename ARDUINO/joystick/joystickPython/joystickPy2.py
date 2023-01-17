
import serial
import pyautogui
import time
#I import the libraries.
arduino_port="/dev/ttyACM0" #Serial port for comunication(ubuntu).
baud=9600#frecuency

ser=serial.Serial(arduino_port, baud)# Connect to /dev/ttyACM0 at 9600 bauds
print("Connected to the arduino port at ", baud, "bauds") # Confirm connection

while True:#I'm using a while because I want it to run while the program is running, forever.
    data=ser.readline().decode('utf-8').rstrip() # Decode the data printed by arduino in the serial port.
    xyValues=data.split(",")# creates an array like this: ['x','y']
    final_xyValues=[]# declaration of a new array
    for i in xyValues:
        final_xyValues.append(int(i))
    #When the loop has finished, I have this array: [x, y], where x and y are integers.
    print(final_xyValues)
    #to check the problem uncomment the code below:
    """
    if len(final_xyValues)==2:
        pyautogui.moveRel(final_xyValues[0], final_xyValues[1])
        time.sleep(0.2)
    """

"""
Here is where I need help. I want to move the cursor with the values that
the program is constantly receiving and converting to an array called
final_xyValues. The array final_xyValues's first value is the x axis and the
second the y axis.

Take in count that the variable data is a string like this: '405,678', wich is
transform to an array with two integers as values. Now, you must know that the values
of final_xyValues are from an analog input of a joystick connected to an Arduino Uno
and readen from the serial port. I want to move the cursor with the analog inputs of the
joystick.

ISSUE: when I uncomment the code from line 21 to 25 the first values of the joystick x and y
position in that moment are ok but after that the data continues identical to the first values
read. The values are correctly and constantly been updated if I comment this part of the code,
if I move the joystick the data changes.
"""
    


   
