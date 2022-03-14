import time as t
import serial as s

arduino = s.Serial("COM3", baudrate=9600, timeout=1)
from pynput.keyboard import Key, Controller
teclado = Controller()

while True:
    val = arduino.readline().decode()
    val = val.replace("\n", "")
    val = val.replace("\r", "")
    print(val)

    if val[1] == '1':
        teclado.press('a')
        print("A")
    else:
        teclado.release('a')
    if val[2] == '1':
        teclado.press('s')
        print("S")
    else:
        teclado.release('s')
    if val[3] == '1':
        teclado.press('d')
        print("D")
    else:
        teclado.release('d')

    if val[4] == '1':
        teclado.press('w')
        print("W")
    else:
        teclado.release('w')
    if val[5] == '1':
        teclado.press('z')
        print("Z")
    else:
        teclado.release('z')
    if val[6] == '1':
        teclado.press('x')
        print("x")
    else:
        teclado.release('x')

    if val[7] == '1':
        teclado.press('c')
        print("c")
    else:
        teclado.release('c')
    if val[8] == '1':
        teclado.press('v')
        print("v")
    else:
        teclado.release('v')
    t.sleep(.001)


