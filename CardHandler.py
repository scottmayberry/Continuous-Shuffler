import RPi.GPIO as GPIO
from ServoMotor import ServoMotor
import time
import atexit

GPIO.setmode(GPIO.BOARD)
#motor pin for left motor
motorLeft = 16
#motor pin for right motor
motorRight = 18
#motor pin for mid motor
motorMid = 15;
#motor pin for raising and lowering
motorRaise = 13;
#enables all motors for control
MotorEnable = 22

servo = ServoMotor(3, 50, 2, 90) #servo at pin 3

GPIO.setup(motorLeft,GPIO.OUT)
GPIO.setup(motorRight,GPIO.OUT)
GPIO.setup(motorEnable,GPIO.OUT)
#https://cms-assets.tutsplus.com/uploads/users/228/posts/20051/image/2%20motors%20full.png
#for wiring diagram

def toggleMotor(enable = not bool(GPIO.input(motorEnable))):
    if enable:
        GPIO.output(motorEnable, GPIO.HIGH)
    else:
        GPIO.output(motorEnable, GPIO.LOW)

def beginShuffleCards(sleepTime = 0):
    GPIO.output(motorLeft, GPIO.HIGH)
    GPIO.output(motorRight, GPIO.HIGH)
    if sleepTime > 0:
        time.sleep(sleepTime)

def endShuffleCards(sleepTime = 0):
    GPIO.output(motorLeft, GPIO.HIGH)
    GPIO.output(motorRight, GPIO.LOW)
    if sleepTime > 0:
        time.sleep(sleepTime)

def raiseBed(sleepTime = 0):
    pass

def lowerBed(arg):
    pass

def clearBedLeft(arg):
    pass

def clearBedRight(arg):
    pass