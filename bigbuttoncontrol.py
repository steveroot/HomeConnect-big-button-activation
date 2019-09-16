# Python script for using a Raspberry Pi,
# to couple some buttons and LEDs to IFTTT events
# Version 0.1
# by Steve Root
# apps@sroot.eu, www.sroot.eu
# 

from gpiozero import LED
from gpiozero import Button
from time import sleep
import secrets
import requests

key = secrets.iftttkey

if key == "Put the key here":
  print("key is still using the placeholder text. Get a key from IFTTT")
  print("Quiting as no valid key")
  quit()
else:
  print("Key is not the default, that much is true,")
  print("as for if it's valid, I don't have a clue")
print("--- key check done---")  
sleep(5)

ifttturlstart = "https://maker.ifttt.com/trigger/"
ifttturlend = "/with/key/"+key

redbuttonurl = ifttturlstart+"redbutton"+ifttturlend
greenbuttonurl = ifttturlstart+"greenbutton"+ifttturlend

#requests.get(redbuttonurl)

ledred = LED(17)
ledgreen = LED(27)
buttonred = Button(2)
buttongreen = Button(3)

while True:
    # Flashing the LEDs was useful during setup to see things are working.
    # ledred.on()
    # ledgreen.on()
    # print("led-flash")
    # sleep(0.5)
    # ledred.off()
    # ledgreen.off()
    # print("led-off")
    # sleep(0.5)
    
    # The print lines are useful when running the script manually on a screen
    # where you can view the output. When the pi is runing headless I didn't
    # see the need to output messages.

    if buttonred.is_pressed:
        #print("Pressed red")
        ledred.on()
        requests.get(redbuttonurl)
        sleep(10)
    else:
        #print("released red")
        ledred.off()
    if buttongreen.is_pressed:
        #print("Pressed green")
        ledgreen.on()
        requests.get(greenbuttonurl)
        sleep(10)
    else:
        #print("released green")
        ledgreen.off()
    # I found that without this short sleep at the end of the loop,
    # CPU usages was 100%.  Having the sleep hasn't affected detecting
    # the button press in my tests
    sleep(0.02)
    