import RPi.GPIO as GPIO
import time

servo_pin = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50) 

def set_servo_position(angle):
    duty_cycle = (angle / 18) + 2
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)
    
def buka():
    try:
        pwm.start(0)
        while True:
            set_servo_position(100) 
            break

    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
        
def tutup():
    try:
        pwm.start(0)
        while True:
            set_servo_position(20)
            break

    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
if __name__ == "__main__":
    buka()
    tutup()


