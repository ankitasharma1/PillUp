from twilio.rest import TwilioRestClient
from Arduino import Arduino
import time

twilio_account_sid = "ACd7d94f4f33137408d9029b7856176847"
twilio_auth_token = 'b4f715089fd3ee4320375bdce1f88170'
twilio_number = '+12677133663'
client = TwilioRestClient(twilio_account_sid,twilio_auth_token)

def Lighting():
    currPin = 0
    board = Arduino(9600, "")
    board.pinMode(0, "OUTPUT")
    i = 0
    while True:
        #board.analogWrite(0,65)
        i = i + 1
        print "[" + str(i) + "]\t" 
        #print board.digitalRead(led_pin)  # confirm HIGH (1)
        time.sleep(0.1)


def Button():
    currPin = 0
    board = Arduino(9600, "")
    board.pinMode(8, "INPUT")
    i = 0
    while True:
        inp = board.analogRead(0)
        i = i + 1
        print "[" + str(i) + "]\t" + str(inp)

        #print board.digitalRead(led_pin)  # confirm HIGH (1)
        time.sleep(0.1)


def ButtonTry():
    currPin = 0
    board = Arduino(9600, "")
    board.pinMode(8, "INPUT")
    i = 0
    Counter = 7
    while True:
        inp = board.analogRead(0)
        i = i + 1
        print "[" + str(i) + "]\t" + str(inp)
        if inp > 0:
            Counter = Counter - 1
            if Counter <= 1:
                message = client.messages.create(body="'Hey there! Looks like your medication needs to be restocked! We have taken care of that for you! Ready to be picked up whenever you are ready :)", 
                to="+19737234645", 
                from_="+12677133663")
                #print message.sid
                #Counter = 7
            elif Counter < (7 / 2):
                message = client.messages.create(body="'Hey there! Looks like your doing okay there friend! Make sure your taking your medication on time!", 
                to="+19737234645", 
                from_="+12677133663")
        else:
           print "YOU ARE GOOD TO GO"
        #print board.digitalRead(led_pin)  # confirm HIGH (1)
        time.sleep(0.2)


def AccelRead():
    board = Arduino(9600, "")
    board.pinMode(13, "OUTPUT")

    cX = 0
    cY = 0
    cZ = 0

    while True:
        analogX = board.analogRead(2)
        analogY = board.analogRead(1)
        analogZ = board.analogRead(0)

        if abs(analogX - cX) > 5:
            #abs(analogX - cX) > 5 | abs(analogY - cY) > 5 | 
            print "X:" + str(analogX) + "Y:" + str(analogY) +"Z:" + str(analogZ)
            cX = analogX
            cY = analogY
            #print "X:" + str(analogX)
            cX = analogX
            
        #board.digitalWrite(13, "HIGH")
        #print board.digitalRead(led_pin)  # confirm HIGH (1)
        time.sleep(0.01)

def Blink(led_pin, baud, port=""):
    board = Arduino(baud, port=port)
    board.pinMode(led_pin, "OUTPUT")
    while True:

        board.digitalWrite(led_pin, "HIGH")
        #print board.digitalRead(led_pin)  # confirm HIGH (1)
        time.sleep(1)


def softBlink(led_pin, baud, port=""):
    """
    Fades an LED off and on, using
    Arduino's analogWrite (PWM) function
    """
    board = Arduino(baud, port=port)
    i = 0
    while True:
        i += 1
        k = i % 510
        if k % 5 == 0:
            if k > 255:
                k = 510 - k
            board.analogWrite(led_pin, k)


def adjustBrightness(pot_pin, led_pin, baud, port=""):
    """
    Adjusts brightness of an LED using a
    potentiometer.
    """
    board = Arduino(baud, port=port)
    while True:
        time.sleep(0.01)
        val = board.analogRead(pot_pin) / 4
        print val
        board.analogWrite(led_pin, val)


def PingSonar(pw_pin, baud, port=""):
    """
    Gets distance measurement from Ping)))
    ultrasonic rangefinder connected to pw_pin
    """
    board = Arduino(baud, port=port)
    pingPin = pw_pin
    while True:
        duration = board.pulseIn(pingPin, "HIGH")
        inches = duration / 72. / 2.
        # cent = duration / 29. / 2.
        print inches, "inches"
        time.sleep(0.1)


def LCD(tx, baud, ssbaud, message, port=""):
    """
    Prints to two-line LCD connected to
    pin tx
    """
    board = Arduino(baud, port=port)
    board.SoftwareSerial.begin(0, tx, ssbaud)
    while True:
        board.SoftwareSerial.write(" test ")

if __name__ == "__main__":
    ButtonTry()
