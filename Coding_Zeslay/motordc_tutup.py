import RPi.GPIO as GPIO
from time import sleep

in1 = 6
in2 = 5
en = 27
temp1 = 1 

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p = GPIO.PWM(en, 22)

def berhenti():
  GPIO.output(in1, GPIO.LOW)
  GPIO.output(in2, GPIO.LOW)  
def tutup():
    # try:
        # while True: 
    p.stop()
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    p.start(26) 
    print("Motor putar berlawanan jarum jam")
    sleep(0.5)

    p.stop()

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    p.start(0)

    # break
            # break
    # except KeyboardInterrupt:
        # pass
    # finally:
        # p.stop()
        # GPIO.cleanup()
def buka():
    # try:
        # while True: 
    p.stop()

    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    p.start(26)
    print("Motor putar searah jarum jam")
    sleep(0.5)
            
    p.stop()

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    p.start(0)
if __name__ == "__main__":
    tutup()

