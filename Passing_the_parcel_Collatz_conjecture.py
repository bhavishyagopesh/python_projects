#!/usr/bin/env python2

import zmq
import sys
import random

def server_setup():

    # ZeroMQ Context
    context = zmq.Context()

    # Define the socket using the "Context"
    sock = context.socket(zmq.REP)
    sock.bind("tcp://127.0.0.1:9003")#here comes the ip and port where message is to be sent

    #Server receiving messages
    while (True):
        message = sock.recv()
        if(message!=-1):
            return message

def reply_client(message):

    # ZeroMQ Context
    context = zmq.Context()

    # Define the socket using the "Context"
    sock = context.socket(zmq.REQ)
    sock.connect("tcp://127.0.0.1:9001")#here comes the ip and port from which message is to be Received

    # Send the message after operating over it
    var=int(message)
    finish=0
    if(var==1):
        #send and exit
        sock.send("1")
        finish=1

    #Applying Collatz Conjecture
    else:
        if(var%2==0):
            var_new=var/2
            sock.send("".join(str(var_new)))
        elif(var%2==1):
            var_new=(3*var+1)
            sock.send("".join(str(var_new)))
    return finish

#Function to handle dispatch of first message
def first_reply_client(message):

    # ZeroMQ Context
    context = zmq.Context()

    # Define the socket using the "Context"
    sock = context.socket(zmq.REQ)
    sock.connect("tcp://127.0.0.1:9001")#here comes the ip and port from which message is to be Received

    # Send the message after operating over it
    var=int(message)
    finish=0
    if(var==1):
        #send and exit
        sock.send("1")
        finish=1

    else:
        sock.send("".join(str(var)))

    return finish

#main
def main():

    if sys.argv[len(sys.argv)-1]=="start":
        #start the game by generating a random number
        message = random.randrange(1001,10000001)

        finish = first_reply_client(str(message))
        cnt=0
        message= str(message)
        print "Starting_Number: " + message
        while True:

            if finish==1:
                sys.exit()
            else:
                message = server_setup()
                print "Received: "+message

                if cnt ==1:
                    sys.exit()

                finish =reply_client(message)

                if(message=="1"):
                    print "Sent: " + message
                elif(int(message)%2==0):
                    print "Sent: " + str(int(message)/2)
                    if(str(int(message)/2)=="1"):
                        cnt=1
                elif(int(message)%2==1):
                    print "Sent: " + str(3*int(message)+1)

    else:
        finish=0
        cnt=0
        while True:

            if finish==1:
                sys.exit()
            else:
                message = server_setup()
                print "Received: "+message
                if cnt ==1:
                    sys.exit()

                finish=reply_client(message)
                if(message=="1"):
                    print "Sent: " + message
                elif(int(message)%2==0):
                    print "Sent: " + str(int(message)/2)
                    if(str(int(message)/2)=="1"):
                        cnt=1
                elif(int(message)%2==1):
                    print "Sent: " + str(3*int(message)+1)

if __name__ == '__main__':
    main()

#END_OF_SOURCE_CODE
