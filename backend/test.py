import serial

ser = serial.Serial("COM6", 9600, timeout=1)
print("Opened COM6 successfully")
ser.close()