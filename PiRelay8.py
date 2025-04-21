#!/usr/bin/python

# Library for PiRelay-6
# Developed by: SB Components
# Author: Satyam
# Project: PiRelay
# Python: 3.4.2

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


class Relay:
    """Class to handle Relays
    Arguments:
    relay = string Relay label (i.e. "RELAY1", "RELAY2", "RELAY3", "RELAY4",
    "RELAY5", "RELAY6", "RELAY7", "RELAY8")
    """
    relaypins = {
        "RELAY1": 29, "RELAY2": 31, "RELAY3": 33, "RELAY4": 36,
        "RELAY5": 35, "RELAY6": 38, "RELAY7": 40, "RELAY8": 37
                 }

    def __init__(self, relay):
        self.pin = self.relaypins[relay]
        self.relay = relay
        GPIO.setup(self.pin,GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def on(self):
        print(self.relay + " - ON")
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        print(self.relay + " - OFF")
        GPIO.output(self.pin, GPIO.LOW)
