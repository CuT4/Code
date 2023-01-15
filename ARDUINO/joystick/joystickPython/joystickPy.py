import serial

arduino_port="/dev/ttyACM0"
baud=9600
#in the code I've readen, they took anly 10 samples but I'm gonna collect data till the program, is closed.
samples=10
ser=serial.Serial(arduino_port, baud)
print("Connected to the arduino port at ", baud, "bauds")

line=0

while line<=samples:
    data=ser.readline()
    print(data.decode('utf-8'))
    line+=1
print("Data collection completed")