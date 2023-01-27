import RPi.GPIO as GPIO
import time
import sys
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

DEBUG = False
if '-debug' in sys.argv:
   DEBUG= True

pin1=11
pin2=13

GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin2, GPIO.OUT, initial=GPIO.LOW)




switchOptions=int(input("To 
if switchOptions==0:
   blinkRate = input("Blink Rate:")
   runLength = int(input("Run Length:"))
   while int(runLength)  > 0: #
      runLength -= 1 # Decrement counter
      GPIO.output(pin1, GPIO.HIGH) # Turn on
      sleep(float(blinkRate))                     # Sleep for 1 second
      GPIO.output(pin1, GPIO.LOW)  # Turn off
      sleep(float(blinkRate))

GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin2, GPIO.OUT, initial=GPIO.LOW)




#with open('file,txt','w') as f:

  # f.write(f'{int(time.time():1.0f}/t {0}\n'})

while int(runLength)  > 0: #
   runLength -= 1 # Decrement counter
   GPIO.output(pin1, GPIO.HIGH) # Turn on
   sleep(float(blinkRate))                     # Sleep for 1 second
   GPIO.output(pin1, GPIO.LOW)  # Turn off
   sleep(float(blinkRate))                     # Sleep for 1 second
GPIO.cleanup()
