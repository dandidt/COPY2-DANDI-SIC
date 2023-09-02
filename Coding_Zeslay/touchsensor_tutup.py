import time
import RPi.GPIO as GPIO
import servo_jendela
import servo_pintu
import selenoid

touch_pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(touch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def touch_det(pin):
    touch = GPIO.input(pin)
    return touch

def main():
    try:
        start_time = time.time()
        while time.time() - start_time < 3:
            if touch_det(touch_pin):    
                print('[' + time.ctime() + '] - ' + 'Touch Detected')
                # selenoid.buka()
                # time.sleep(2)
                # servo_jendela.tutup()
                servo_pintu.tutup()
                time.sleep(1)
                selenoid.tutup()
            time.sleep(1)  
            
    except KeyboardInterrupt:
        print('Interrupted!')
        GPIO.cleanup()

if __name__ == "__main__":
    main()
    