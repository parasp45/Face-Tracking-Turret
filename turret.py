import serial
import keyboard 
import time

# Replace with the correct port for your system (e.g., 'COM3' for Windows or '/dev/ttyUSB0' for Linux/Mac)
arduino_port = '/dev/ttyUSB0'  # Change this to match your Arduino's port
baud_rate = 9600 
arduino = serial.Serial(port='COM4',baudrate= 9600, timeout=0)
# Wait for the Arduino to initializead
while True:
        time.sleep(0.1)
        # Print out which key is pressed for debugging purposes
        if keyboard.is_pressed("a"):
            print("Key 'a' detected.")
            arduino.write(b"a")
            print('a')
        elif keyboard.is_pressed("s"):
            print("Key 's' detected.")
            arduino.write(b"s")
            print('s')
        elif keyboard.is_pressed("d"):
            print("Key 'd' detected.")
            arduino.write(b"d")
            print('d')
        elif keyboard.is_pressed("w"):
            print("Key 'w' detected.")
            arduino.write(b"w")
            print('w')
        elif keyboard.is_pressed("e"):
            print("Key 'e' detected.")
            arduino.write(b"e")
            print('f')
        elif keyboard.is_pressed('x') == "x":
             break
# Close the serial connection
arduino.close()
