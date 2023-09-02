import RPi.GPIO as GPIO
import time

# Inisialisasi GPIO
servo_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Konfigurasi PWM (Pulse Width Modulation)
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz (siklus 20 ms)

# Mekanisme pergerakan servo dari 20 derajat ke 100 derajat
def set_servo_position(angle):
    duty_cycle = (angle / 18) + 2
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)  # Beri waktu untuk servo mencapai posisi

try:
    pwm.start(0)  # Memulai PWM dengan duty cycle 0 (posisi awal)
    while True:
        set_servo_position(30)  # Posisi 20 derajat
        time.sleep(1)  # Jeda 1 detik
        set_servo_position(80)  # Posisi 100 derajat
        time.sleep(1)  # Jeda 1 detik

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
