import RPi.GPIO as GPIO
from time import sleep
import requests
import time

in1 = 6
in2 = 5
en = 27
pin_solenoid1 = 24
pintu_pin = 25
jendela_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.setup(pintu_pin, GPIO.OUT)
GPIO.setup(jendela_pin, GPIO.OUT)
p = GPIO.PWM(en, 22)  # PWM dengan frekuensi 1000 Hz

#Pagar
def buka_pagar():
    p.start(26)  # PWM dengan duty cycle 50%
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    print("Membuka pagar")
    sleep(0.5)
    p.stop()

def tutup_pagar():
    p.start(26)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    print("Menutup pagar")
    sleep(0.5)
    p.stop()
    
def mati_pagar ():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in1, GPIO.LOW)
    print("Motor Mati")

#Pengunci
def buka_selenoid():
    GPIO.setup(pin_solenoid1, GPIO.OUT)
    GPIO.output(pin_solenoid1, GPIO.HIGH)
    print("Membuka solenoid")

def tutup_selenoid():
    GPIO.setup(pin_solenoid1, GPIO.OUT)
    GPIO.output(pin_solenoid1, GPIO.LOW)
    print("Menutup solenoid")
    
#Pintu
pwm = GPIO.PWM(pintu_pin, 50) 

def set_pintu_position(angle):
    duty_cycle = (angle / 18) + 2
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)

def buka_pintu():
    pwm.start(0)
    set_pintu_position(100) 
    print("Pintu Terbuka") 
        
def set_pintu_position(angle):
    duty_cycle = (angle / 18) + 2
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)
        
def tutup_pintu():
    pwm.start(0)
    set_pintu_position(20)
    print("Pintu Tertutup")

#Jendela
pwm = GPIO.PWM(jendela_pin, 50)
   
def set_servo_position(angle):
    duty_cycle = (angle / 18) + 2
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)   

def buka_jendela(): #Buka
    pwm.start(0)
    set_servo_position(80)
    print("Jendela Terbuka")
        
def set_servo_position(angle):
    duty_cycle = (angle / 18) + 2
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)
        
def tutup_jendela(): #Tutup
    pwm.start(0)
    set_servo_position(30)
    print("jendela Tertutup")
    
TOKEN = "BBFF-JjJulhhIUtkGKB24EU12eSkHpgDK8h"
DEVICE_LABEL = "zeslay"
VARIABLE_LABEL = "motordc"
VARIABLE_LABEL1 = "selenoid"
VARIABLE_LABEL2 = "pintu"
VARIABLE_LABEL3 = "jendela"

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
        pintu_button_status = get_button_status(VARIABLE_LABEL2)
        jendela_button_status = get_button_status(VARIABLE_LABEL3)

        print("Motor Button Status:", motor_button_status)
        print("Solenoid Button Status:", solenoid_button_status)
        print("Pintu Button Status:", pintu_button_status)
        print("Jendela Button Status:", jendela_button_status)
        
        #Motot
        if motor_button_status == 1:
            buka_pagar()
            tutup_pagar()
        elif motor_button_status == 0:
            mati_pagar()

        #Selenoid
        if solenoid_button_status == 1: 
            buka_selenoid()
        elif solenoid_button_status == 0:
            tutup_selenoid()
        
        
        #Pintu  
        if pintu_button_status == 1:
            buka_selenoid()
            time.sleep(2)
            tutup_pintu()
            time.sleep(2)
            tutup_selenoid()
        elif pintu_button_status == 0:
            buka_selenoid()
            time.sleep(2)
            buka_pintu()
            time.sleep(2)
            tutup_selenoid()
        
        #Jendela
        if jendela_button_status == 1:
            buka_selenoid()
            time.sleep(2)
            tutup_jendela()
            time.sleep(2)
            tutup_selenoid()
        elif jendela_button_status == 0:
            buka_selenoid()
            time.sleep(2)
            buka_jendela()
            time.sleep(2)
            tutup_selenoid()

except KeyboardInterrupt:
    p.stop()
    print("Program dihentikan")
    GPIO.cleanup()
