import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(25, GPIO.OUT)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

buttonState = True

while True:
    buttonValue = GPIO.input(22)
    if buttonValue != buttonState:
        buttonState = buttonValue
        if buttonState:
            print("Button Pressed")
            GPIO.output(25, True)
            time.sleep(0.1)
        else:
            print("Button Released")
            GPIO.output(25, False)
            time.sleep(0.1)
    time.sleep(0.1)

