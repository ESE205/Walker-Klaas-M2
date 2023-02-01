import RPi.GPIO as GPIO
import sys
import time
import argparse
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
pin1=11
GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13,GPIO.IN)

parser=argparse.ArgumentParser(description='Data for this program.')
parser.add_argument('--r', action='store', type=float, default=1.0)
parser.add_argument('--n', action='store', type=int, default=5.0)
parser.add_argument('--debug', action='store_true')
args = parser.parse_args()
r=args.r
n=args.n
DEBUG=args.debug

with open ('data.txt','w') as data:
   ITER_COUNT=n
   BLINK_RATE=r
   while ITER_COUNT >  0: # Run ITER_COUNT times
      if (GPIO.input(13)):
         ITER_COUNT -= 1 # Decrement counter
         GPIO.output(pin1, GPIO.HIGH) # Turn on
         data.write(f'{time.time() :1.0f} LED is ON\n') 
         sleep(BLINK_RATE)                     # Sleep for 1 second
         GPIO.output(pin1, GPIO.LOW)  # Turn off
         data.write(f'{time.time() :1.0f} LED is OFF\n')
         sleep(BLINK_RATE)                       # Sleep for 1 second
         if DEBUG:
            print(f'{time.time() :1.0f}\t{ITER_COUNT} loops left\t Switch is on')
      else:
         ITER_COUNT -= 1
         GPIO.output(pin1, GPIO.LOW)
         data.write(f'{time.time() :1.0f} LED is OFF\n')
         if DEBUG:
            print(f'{time.time() :1.0f}\t{ITER_COUNT}\t Switch is off')
            sleep(BLINK_RATE)
            sleep(BLINK_RATE)



#   else:
#      while (True):
#         if(GPIO.input(13)):
#            GPIO.output(pin1, GPIO.HIGH) # Turn on
#            data.write(f'{time.time() :1.0f} LED is ON\n') 
#            sleep(1)                     # Sleep for 1 second
#            GPIO.output(pin1, GPIO.LOW)  # Turn off
#            data.write(f'{time.time() :1.0f} LED is OFF\n')
#            sleep(1)                     # Sleep for 1 second
#GPIO.cleanup()



#blinkRate = input("Blink Rate:")
#runLength = int(input("Run Length:"))
#while int(runLength)  > 0: #
#   runLength -= 1 # Decrement counter
#   GPIO.output(pin1, GPIO.HIGH) # Turn on
#   sleep(float(blinkRate))                     # Sleep for 1 second
#   GPIO.output(pin1, GPIO.LOW)  # Turn off
#   sleep(float(blinkRate))
#GPIO.cleanup()

