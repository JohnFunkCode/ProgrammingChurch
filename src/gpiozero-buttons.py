from gpiozero import LED
from gpiozero import PWMLED
from gpiozero import Button
from time import sleep

#setup the LEDs
led=[]
sleeptime=.01 

for i in range(0,10):
    led.append(LED(i+2))

sololed = PWMLED(17)


# define a function to run the LEDs up
def race_up():
    for i in range(0,10):
        print("{} on".format(i))
        led[i].on()
        sleep(sleeptime)
        print("  off")
        led[i].off()
        sleep(sleeptime)

#define a function to run the LEDs down
def race_down():
    for i in range(9,-1,-1):
        print("{} on".format(i))
        led[i].on()
        sleep(sleeptime)
        print("  off")
        led[i].off()
        sleep(sleeptime)


#define the buttons
b1=Button(20,pull_up=True)
b2=Button(21)

print("Let's start by testing the buttons")

print("press button 1")
b1.wait_for_press()
print("Button 1 pressed")

print("press button 2")
b2.wait_for_press()
print("Button 2 pressed")

print("Go...")
# blink the solo led 3 times to signal we are ready
for i in range(0,3):
    sololed.on()
    sleep(.5)
    sololed.off()
    sleep(.5)


# Pulse the LED while we're waiting for input
#sololed.pulse(n=3,background=False)
sololed.pulse()

print("Press a button to make the LEDs race up or down")
while True:
    b1.when_pressed=race_up
    b2.when_pressed=race_down




led=[]
sleeptime=.01 

for i in range(0,10):
    led.append(LED(i+2))

while True:
    for i in range(0,10):
        print("{} on".format(i))
        led[i].on()
        sleep(sleeptime)
        print("  off")
        led[i].off()
        sleep(sleeptime)
    for i in range(9,-1,-1):
        print("{} on".format(i))
        led[i].on()
        sleep(sleeptime)
        print("  off")
        led[i].off()
        sleep(sleeptime)
