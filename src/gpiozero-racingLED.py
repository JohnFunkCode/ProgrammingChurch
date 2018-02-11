from gpiozero import LED
from time import sleep

sololed = LED(17)
for i in range(0,3):
    sololed.on()
    sleep(.5)
    sololed.off()
    sleep(.5)

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
