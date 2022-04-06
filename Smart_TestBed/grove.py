''' This file will provide an interface to your GrovePi code. The functions should accept the port, so to make them port independent. '''
# Reference from: https://github.com/bradnielsen2981/grovepi-flask
import grovepi
import time
import logging

log = logging.getLogger('app')

# This function will return the current light reading from the desired ANALOG port A0, A1 etc
def read_light_sensor_analogueport(port):
    light_sensor = port
    grovepi.pinMode(light_sensor,"INPUT")
    sensor_value = None
    try:
        sensor_value = grovepi.analogRead(light_sensor) # Get sensor value
    except IOError: #this doesnt appear to work
        log.error("Error in reading the light sensor")
    return sensor_value

#Turn on the buzzer
def turn_on_buzzer_digitalport(port):
    buzzer = port
    grovepi.pinMode(buzzer,"OUTPUT")
    grovepi.digitalWrite(buzzer,255)
    return

#Turn off the buzzer
def turn_off_buzzer_digitalport(port):
    buzzer = port
    grovepi.pinMode(buzzer,"OUTPUT")
    grovepi.digitalWrite(buzzer,0)
    return
#Turn on the led
def turn_on_led_digitalport(port):
    led = port
    grovepi.pinMode(led,"OUTPUT")
    grovepi.digitalWrite(led,255)
    return

#Turn off the led
def turn_off_led_digitalport(port):
    led = port
    grovepi.pinMode(led,"OUTPUT")
    grovepi.digitalWrite(led,0)
    return
#Turn on the fan
def turn_on_fan_digitalport(port):
    fan = port
    grovepi.pinMode(fan,"OUTPUT")
    grovepi.digitalWrite(fan,255)
    return

#Turn off the fan
def turn_off_fan_digitalport(port):
    fan = port
    grovepi.pinMode(fan,"OUTPUT")
    grovepi.digitalWrite(fan,0)
    return

#read temp and humidity
def read_temp_humidity_sensor_digitalport(port):
    tempsensor = port
    grovepi.pinMode(tempsensor,"INPUT")
    temp_humidity_list = None
    try:
        temp_humidity_list = grovepi.dht(port,0) #0 - type blue sensor
    except IOError: #this doesnt appear to work
        log.error("Error in reading the temp and humidity sensor")
    return temp_humidity_list

#--------------------------------------------------------------------

