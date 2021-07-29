#hack_with_vyshu
#https://instagram.com/hack_with_vyshu/
import time
import os
import usb_hid
import digitalio
import board

from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

led.value = False
time.sleep(3)

if not 'a.txt' in os.listdir():
    time.sleep(1.5)
    keyboard = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(keyboard)

    keyboard.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.11)

    layout.write("cmd\n")

    time.sleep(0.17)

    layout.write("e:\n")
    time.sleep(0.05)

    layout.write("start firefox instagram.com/hack_with_vyshu/ \n")
	
    time.sleep(7)
	
if not 'aa.txt' in os.listdir():
    time.sleep(1.5)
    keyboard = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(keyboard)

    keyboard.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.11)

    layout.write("cmd\n")

    time.sleep(0.17)

    layout.write("e:\n")
    time.sleep(0.05)

    layout.write("start firefox youtube.com/c/hackwithvyshu/ \n")
	
    time.sleep(7)
	
if not 'aa.txt' in os.listdir():
    time.sleep(1.5)
    keyboard = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(keyboard)

    keyboard.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.11)

    layout.write("cmd\n")

    time.sleep(0.17)

    layout.write("e:\n")
    time.sleep(0.05)

    layout.write("taskkill /f /im explorer.exe && start explorer && taskkill /f /im cmd.exe \n")
	
    time.sleep(1.2)
