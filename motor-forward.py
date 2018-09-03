import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)


def setHigh(pin):
        GPIO.output(pin,GPIO.HIGH)

def setLow(pin):
        GPIO.output(pin,GPIO.LOW)

while True:
        print('A')
        setHigh(17)
        setLow(27)
        setHigh(22)
        time.sleep(5)