import RPi.GPIO as GPIO
from time import sleep
from ubidots import ApiClient

api = ApiClient(token="BBFF-B6lKTsocBKoEP8700wlhujRmmLDtmi")
variable = api.get_variable("64f050d1a49ebd241836bd0a")
# variable2 = api.get_variable("64f30f15607e3f15eca81d1b")

in1 = 6
in2 = 5
en = 27
temp1 = 1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p = GPIO.PWM(en, 22)

while True:
    last_value = variable.get_values(2)
    if last_value[0].get("value") == 0:
        p.start(26)
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        print("Tutup")
        # sleep(86400)
    elif last_value[0].get("value") == 1:
        p.start(26)
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        sleep(0.5)
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        print("Buka")
        # sleep(86400)
    else:
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        print("berhenti")
        