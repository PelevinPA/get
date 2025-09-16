import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [16,12,25,17,27,23,22,24]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
up = 9
GPIO.setup(up, GPIO.IN)
down = 10
GPIO.setup(down, GPIO.IN)
while True:
    if (GPIO.input(up) and GPIO.input(down)):
        GPIO.output(leds, 1)
    else:
        GPIO.output(leds, 0)