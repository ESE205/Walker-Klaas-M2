import RPi.GPIO as GPIO
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
pin1=11
GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13,GPIO.IN)
while (True):
   if(GPIO.input(13)):
      GPIO.output(pin1,GPIO.LOW)
      sleep(.1)
      GPIO.output(pin1,GPIO.HIGH)
