"""
El problema aparece al utilizar pyautogui, debo de cambiar
la librería para mover el cursor y ver si funciona entonces.
"""

import serial
import pyautogui
import time

arduino_port="/dev/ttyACM0"
baud=9600
#in the code I've readen, they took anly 10 samples but I'm gonna collect data till the program is closed.
ser=serial.Serial(arduino_port, baud)
print("Connected to the arduino port at ", baud, "bauds")
# screenWidth, screenHeight=pyautogui.size()
# mouseX, mouseY=pyautogui.position() #actual positon X and y of the mouse
# screenSize=[screenWidth, screenHeight]# is [1920, 1080] in my monitor



while True:
    data=ser.readline().decode('utf-8').rstrip()
    xyValues=data.split(",")
    final_xyValues=[]
    for i in xyValues:
        final_xyValues.append(int(i))
    print(final_xyValues)
    #to check if it works comment the code below:
    # if len(final_xyValues)==2:
    #     pyautogui.moveRel(final_xyValues[0], final_xyValues[1])
    #     time.sleep(0.2)

"""
Here is where I need help. I want to move the cursor with the values that
the program is constantly receiving and converting to an array called
final_xyValues. The array final_xyValues's first value is the x axis and the
second the y axis.

Take in count that the variable data is a string like this: '405,678', wich is
transform to an array with two integers as values. Now, you must know that the values
of final_xyValues are from an analog input of a joystick connected to an Arduino Uno
and readen from the serial port. I want to move the cursor with the analog inputs of the
joystick

"""
    


   
    
