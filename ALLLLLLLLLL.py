from gpiozero import DigitalInputDevice, DigitalOutputDevice, Buzzer
from time import time, sleep
import I2C_LCD_driver
import selenoid
import buzzer_on    
import touchsensor_tutup
import touchsensor_buka

col1 = DigitalOutputDevice(22)  
col2 = DigitalOutputDevice(13)
col3 = DigitalOutputDevice(19)
col4 = DigitalOutputDevice(26)
row1 = DigitalInputDevice(21, pull_up=None, active_state=True)
row2 = DigitalInputDevice(20, pull_up=None, active_state=True)
row3 = DigitalInputDevice(16, pull_up=None, active_state=True)
row4 = DigitalInputDevice(12, pull_up=None, active_state=True)

lcd = I2C_LCD_driver.lcd()

def scanCol(colNumber):
    if colNumber == 0:
        col1.on()
        col2.off()
        col3.off()
        col4.off()
    elif colNumber == 1:
        col1.off()
        col2.on()
        col3.off()
        col4.off()
    elif colNumber == 2:
        col1.off()
        col2.off()
        col3.on()
        col4.off()
    elif colNumber == 3:
        col1.off()
        col2.off()
        col3.off()
        col4.on()

def row1Pressed():
    global colNumber
    global keypadNumber
    global scanning
    if col1.value == 1:
        keypadNumber = 1
    elif col2.value == 1:
        keypadNumber = 2
    elif col3.value == 1:
        keypadNumber = 3
    elif col4.value == 1:
        keypadNumber = 10
    scanning = False

def row2Pressed():
    global colNumber
    global keypadNumber
    global scanning
    if col1.value == 1:
        keypadNumber = 4
    elif col2.value == 1:
        keypadNumber = 5
    elif col3.value == 1:
        keypadNumber = 6
    elif col4.value == 1:
        keypadNumber = 11
    scanning = False

def row3Pressed():
    global colNumber
    global keypadNumber
    global scanning
    if col1.value == 1:
        keypadNumber = 7
    elif col2.value == 1:
        keypadNumber = 8
    elif col3.value == 1:
        keypadNumber = 9
    elif col4.value == 1:
        keypadNumber = 12
    scanning = False
        
def row4Pressed():
    global colNumber
    global keypadNumber
    global scanning
    if col1.value == 1:
        keypadNumber = 14
    elif col2.value == 1:
        keypadNumber = 0
    elif col3.value == 1:
        keypadNumber = 15
    elif col4.value == 1:
        keypadNumber = 13
    scanning = False

def row1Released():
    global scanning
    scanning = True

def row2Released():
    global scanning
    scanning = True

def row3Released():
    global scanning
    scanning = True

def row4Released():
    global scanning
    scanning = True

row1.when_activated = row1Pressed
row2.when_activated = row2Pressed
row3.when_activated = row3Pressed
row4.when_activated = row4Pressed
row1.when_deactivated = row1Released
row2.when_deactivated = row2Released
row3.when_deactivated = row3Released
row4.when_deactivated = row4Released

currentMillis = 0
previousMillis = 0
interval = 10
colNumber = 0
keypadNumber = 20
scanning = True
passCount = 0
passTimeout = 0
password = "1234"
touchsensortutup = "1"
touchsensorbuka = "2"
passEnter = ""

lcd.lcd_display_string("Silakan masuk   ", 1, 0)
lcd.lcd_display_string("Password:   ", 2, 0)

try:
    while True:
        currentMillis = time() * 1000
        if currentMillis - previousMillis > interval and scanning == True:
            previousMillis = currentMillis
            
            scanCol(colNumber)
            
            colNumber = colNumber+1
            if colNumber == 4:
                colNumber = 0
            
            if passCount:
                passTimeout = passTimeout+1     
                if passTimeout > 200:
                    if passEnter == password:
                        lcd.lcd_display_string("Benar! Enter", 1, 0)
                        selenoid.buka()
                        
                    elif passEnter == touchsensortutup:
                        def run_touchsensor_program():
                            lcd.lcd_display_string("Berjalan...", 1, 0)     
                            touchsensor_buka.main()
                            
                        passEnter = True
                        touchsensortutup = True

                        if passEnter == touchsensortutup:
                            run_touchsensor_program()
                            print("Program selanjutnya dimulai")
                            passCount = 0
                            
                    elif passEnter == touchsensorbuka:
                        def run_touchsensor_program():
                            lcd.lcd_display_string("Berjalan...", 1, 0)     
                            touchsensor_tutup.main()
                            
                        passEnter = True
                        touchsensorbuka = True

                        if passEnter == touchsensorbuka:
                            run_touchsensor_program()
                            print("Program selanjutnya dimulai")
                            passCount = 0
                    
                    else:
                        lcd.lcd_display_string("Salah! Coba Lagi", 1, 0)
                        selenoid.tutup()
                        buzzer_on.main_buzzer()
                        
                    passEnter = ""
                    passCount = 0
                    lcd.lcd_display_string("       ", 2, 9)
                    lcd.lcd_display_string("Silakan masuk   ", 1, 0)
                    lcd.lcd_display_string("Password:   ", 2, 0)
                    
            if passCount == 1 and passTimeout == 1:
                lcd.lcd_display_string("Memindai...     ", 1, 0)
        
        if keypadNumber < 20:
            print(keypadNumber)
            if keypadNumber < 10 and passCount < 6:
                passEnter = passEnter + str(keypadNumber)
                lcd.lcd_display_string(passEnter, 2, 9)
                passCount = passCount+1
                passTimeout = 0
            keypadNumber = 20
except KeyboardInterrupt:
    lcd.lcd_clear()
