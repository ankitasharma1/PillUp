from twilio.rest import TwilioRestClient
from Arduino import Arduino
import time


twilio_account_sid = "ACd7d94f4f33137408d9029b7856176847"
twilio_auth_token = 'b4f715089fd3ee4320375bdce1f88170'
twilio_number = '+12677133663'
client = TwilioRestClient(twilio_account_sid,twilio_auth_token)


def ButtonPill():

    board = Arduino(9600, "")
    i = 0
    Counter = 10
    CounterCopy = Counter

    while True:

        inp = board.analogRead(0)
        i = i + 1
        print "[" + str(i) + "]\t" + str(inp)
        if inp > 0:

            Counter = Counter - 1

            if Counter <= 2:

                message = client.messages.create(
                body="Hey there!\n" +
                "Looks like your medication needs to be restocked!\n" +
                "We have taken care of that for you! Ready to be picked up whenever you are ready :)", 
                to="+19737234645", 
                from_="+12677133663")

                message = client.messages.create(
                body="Hey there!\n" +
                "Looks like Ankita''s medication needs to be restocked!\n" +
                "We have taken informed her as well!", 
                to="+14702633590", 
                from_="+12677133663")
            
            elif Counter < (CounterCopy/2):

                message = client.messages.create(
                body="Hey there!\n" +
                "Looks like your doing well there friend!\n" +
                "Make sure your taking your medication on time!", 
                to="+19737234645", 
                from_="+12677133663")

        time.sleep(0.3)



if __name__ == "__main__":
    ButtonPill()
