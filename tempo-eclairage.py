from machine import Pin
import time

led = Pin(21, Pin.OUT)
bp = Pin(39, Pin.IN)

compt = 0
while True:
    if not bp.value():
        compt = 20
        print("Light ON")
    print(compt)
    if compt > 0:
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.1)
    compt = compt - 1
    if compt == 0:
        print("Light BBF")
