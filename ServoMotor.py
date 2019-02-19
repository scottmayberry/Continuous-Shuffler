class ServoMotor:
    count = 0

    def __init__(self, pwmPin = 3, hz = 50, minDuty = 2, currentAngle = 90):
        self.servoPWM = GPIO.PWM(pwmPin, hz)
        self.pwmPin = pwmPin
        self.hz = hz
        self.minDuty = minDuty
        self.maxDuty = minDuty + 10
        self.angle = currentAngle
        self.duty = 0
        count = count + 1
        self.numberInit = count
        startMotor()
        atexit.register(self.cleanup)

    def cleanup(self):
        self.servoPWM.stop()
        GPIO.cleanup()
        print("Cleaning up ServoMotor #" + self.numberInit + " at pin #" + self.pwmPin)

    def startMotor(self):
        self.servoPWM.start(0)

    def setAngle(self, angle, waitTime = 1): #moves servo to requested angle. Timer.sleep needs to be refined
        self.angle = angle
        self.duty = self.angle/18 + self.minDuty
        GPIO.output(self.pwmPin, True)#turns on GPIO pin
        servoPWM.ChangeDutyCycle(self.duty)
        time.sleep(waitTime)
        GPIO.output(self.pwmPin, False) #turns off GPIO pin
        servoPWM.ChangeDutyCycle(0)

    def holdAngle(self, angle):
        self.angle = angle
        self.duty = self.angle/18 + self.minDuty
        GPIO.output(self.pwmPin, True)#turns on GPIO pin
        servoPWM.ChangeDutyCycle(self.duty)

    def getPWMPin(self):
        return self.pwmPin
    def getDutyCycle(self):
        return self.duty
    def getAngle(self):
        return self.angle
    def getServoCount():
        return count
