import RPi.GPIO as GPIO
import time

buzzer_pin = 4

melody = [
    (1000, 275), (0, 300), (600, 250), (0, 600),
    (1000, 275), (0, 300), (600, 250), (0, 600),
    (1000, 275), (0, 300), (600, 250), (0, 600),
]

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzer_pin, GPIO.OUT)
    global p
    p = GPIO.PWM(buzzer_pin, 10000)  # Frekuensi PWM 1000 Hz (sesuaikan jika diperlukan)
    p.start(0)  # Memulai PWM dengan duty cycle 0 (mati)

def buzzer_on():
    p.ChangeDutyCycle(50)  # Mengatur duty cycle ke 50% (bunyi)

def buzzer_off():
    p.ChangeDutyCycle(0)  # Mengatur duty cycle ke 0 (tidak bunyi)

def play_melody():
    for note, duration in melody:
        if note != 0:
            buzzer_on()
            p.ChangeFrequency(note)
            time.sleep(duration / 1000.0)
        else:
            buzzer_off()
            time.sleep(duration / 1000.0)

def main_buzzer():
    setup()
    while True:  # Loop berulang kali
        play_melody()
        time.sleep(1) 
        p.stop() # Jeda 1 detik sebelum memainkan ulang melodi
        break
    
    # except KeyboardInterrupt:
    #     p.stop()
    #     GPIO.cleanup()

# if __name__ == "__main__":
#     main_buzzer()
