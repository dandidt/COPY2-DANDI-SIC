import RPi.GPIO as GPIO
from time import sleep
import requests
import time
import selenoid
import servo_jendela
import motordc_tutup

TOKEN = "BBFF-JjJulhhIUtkGKB24EU12eSkHpgDK8h"
DEVICE_LABEL = "zeslay"
VARIABLE_LABEL = "motordc"
VARIABLE_LABEL1 = "selenoid"
VARIABLE_LABEL2 = "jendela"

def get_button_status(variable_label):
    url = f"https://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_LABEL}/{variable_label}/"
    headers = {"X-Auth-Token": TOKEN}
    response = requests.get(url, headers=headers)
    data = response.json()
    value = data["last_value"]["value"]
    return value

try:
    while True:
        motor_button_status = get_button_status(VARIABLE_LABEL)
        solenoid_button_status = get_button_status(VARIABLE_LABEL1)
        jendela_button_status = get_button_status(VARIABLE_LABEL2)

        print("Motor Button Status:", motor_button_status)
        print("Solenoid Button Status:", solenoid_button_status)
        print("Jendela Button Status:", jendela_button_status)
        
        #Motor
        if motor_button_status == 1:
            motordc_tutup.tutup()
            
        elif motor_button_status == 0:
            motordc_tutup.berhenti()

        #Selenoid
        if solenoid_button_status == 1: 
            selenoid.buka()
        elif solenoid_button_status == 0:
            selenoid.tutup()
        
        #Jendela
        if jendela_button_status == 1:
            selenoid.buka()
            time.sleep(1)
            servo_jendela.tutup()
        elif jendela_button_status == 0:
            selenoid.buka()
            time.sleep(1)
            servo_jendela.buka()
            
except KeyboardInterrupt:
    # p.stop()
    print("Program dihentikan")
    GPIO.cleanup()
