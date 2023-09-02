import RPi.GPIO as GPIO

def buka():
    GPIO.setmode(GPIO.BCM)

    pin_solenoid1 = 24

    GPIO.setup(pin_solenoid1, GPIO.OUT)

    while True:
        GPIO.output(pin_solenoid1, GPIO.HIGH)

        break
    
def tutup():
    GPIO.setmode(GPIO.BCM)

    pin_solenoid1 = 24

    GPIO.setup(pin_solenoid1, GPIO.OUT)

    while True:
        GPIO.output(pin_solenoid1, GPIO.LOW)

        break
    
# def ubidot():
#     open = buka()
#     # close = tutup()
    
#     return open
