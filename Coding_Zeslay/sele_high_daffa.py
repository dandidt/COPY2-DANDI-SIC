import RPi.GPIO as GPIO

def buka():
    GPIO.setmode(GPIO.BCM)

    pin_solenoid1 = 24

    GPIO.setwarnings(False)
    GPIO.setup(pin_solenoid1, GPIO.OUT)


    while True:
        GPIO.output(pin_solenoid1, GPIO.HIGH)

        break
buka()
#     buka()
