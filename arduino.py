import pyfirmata
import time

port = 'COM3'
board = pyfirmata.Arduino(port)

while True:
    insa = input("value:")
    if insa == "1":
        pin = 3
    elif insa == "2":
        pin = 4
    else:
        pin = 0
    board.digital[pin].mode = pyfirmata.SERVO
    for i in range(0, 180):
        board.digital[pin].write(i)
        time.sleep(0.015)
