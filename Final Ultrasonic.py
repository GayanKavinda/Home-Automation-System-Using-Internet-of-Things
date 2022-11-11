import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
TRIG = 18
ECHO = 24
Buff = 4

GPIO.setwarnings(False)
GPIO.setup(TRIG ,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(Buff ,GPIO.OUT)

GPIO.output(TRIG, False)
print("Starting.....")
time.sleep(2)

while True:
   GPIO.output(TRIG, True)
   time.sleep(0.00001)
   GPIO.output(TRIG, False)

   while GPIO.input(ECHO)== 0:
      pulse_start = time.time()

   while GPIO.input(ECHO)== 1:
      pulse_stop = time.time()

   pulse_time = pulse_stop - pulse_start

   distance = (pulse_time * 34300) / 2
   print(round(distance));

   time.sleep(1)
   
   if distance < 7:
       print("Water will overflow")
       GPIO.output(Buff, True);
       time.sleep(0.5)
       GPIO.output(Buff, False);
       time.sleep(0.5)
       GPIO.output(Buff, True);
       time.sleep(0.5)
       GPIO.output(Buff, False);
       time.sleep(0.5)
   else:
       GPIO.output(Buff, False);

