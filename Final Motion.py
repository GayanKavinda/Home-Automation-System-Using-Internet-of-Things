import RPi.GPIO as GPIO
import time

PIR = 23
Relay = 16
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(PIR, GPIO.IN) #PIR
GPIO.setup(Relay, GPIO.OUT) #BUzzer


try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(PIR):
            GPIO.output(Relay, True)
            time.sleep(1) #Buzzer turns on for 0.5 sec
            GPIO.output(Relay, False)
            print("Motion Detected...")
            time.sleep(5) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()   #Time delay of 1 second