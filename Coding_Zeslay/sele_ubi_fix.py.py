import RPi.GPIO as GPIO
from ubidots import ApiClient
import time

api = ApiClient(token="BBFF-B6lKTsocBKoEP8700wlhujRmmLDtmi")
variable = api.get_variable("64f050d1a49ebd241836bd0a")

#setup selenoid
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pin_solenoid1 = 24
GPIO.setup(pin_solenoid1, GPIO.OUT)

#setup motordc

while True:
    last_value = variable.get_values(1)
    if last_value[0].get("value") == 1:
        GPIO.output(pin_solenoid1, GPIO.HIGH)
        print("on")
        # time.sleep(1)
    else:
        GPIO.output(pin_solenoid1, GPIO.LOW)
        print("off")

        # time.sleep(1)
        

