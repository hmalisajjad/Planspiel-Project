# Reference from: https://github.com/bradnielsen2981/grovepi-flask

from flask import Flask, render_template, jsonify, request
import logging #allow loggings
import grove #imports the grove functionality that you define
import ipaddress #imports the display on I2C-2
from datetime import datetime

#uses JSONIFY to encode data structures in Strings. AJAX can then change it back..
#Global Variables
app = Flask(__name__)
log = app.logger #sets up a log -- to log call log.info('message')
#log.error("Testing") --use this to log an error

#request handlers ---------------------------------------------
@app.route('/')
def home():
    return render_template("index.html")

#start a light
@app.route('/startled', methods=['GET','POST'])
def startled():
    grove.turn_on_led_digitalport(4) #turn on led on d4
    return jsonify({ "message":"starting" }) #jsonify take any type and makes a JSON string

#stop a light
@app.route('/stopled', methods=['GET','POST'])
def stopled():
    grove.turn_off_led_digitalport(4) #turn off led on d4
    return jsonify({ "message":"stopping" })

#start a fan
@app.route('/startfan', methods=['GET','POST'])
def startfan():
    grove.turn_on_fan_digitalport(2) #turn on fan on d2
    return jsonify({ "message":"starting" }) #jsonify take any type and makes a JSON string

#stop a fan
@app.route('/stopfan', methods=['GET','POST'])
def stopfan():
    grove.turn_off_fan_digitalport(2) #turn off fan on d2
    return jsonify({ "message":"stopping" })

#start a buzzer
@app.route('/startbuzzer', methods=['GET','POST'])
def startbuzzer():
    grove.turn_on_buzzer_digitalport(5) #turn on buzzer on d5
    return jsonify({ "message":"starting" }) #jsonify take any type and makes a JSON string

#stop a buzzer
@app.route('/stopbuzzer', methods=['GET','POST'])
def stopbuzzer():
    grove.turn_off_buzzer_digitalport(5) #turn off buzzer on d5
    return jsonify({ "message":"stopping" })

#detect a motion
@app.route('/startmotion', methods=['GET','POST'])
def startmotion():
    grove.turn_on_motion_digitalport(6) #start motion on d6
    return jsonify({ "message":"starting" })

#editor
@app.route('/editor/', methods=['GET','POST'])
def editor():
    return render_template("editor.html")

#return light values
@app.route('/getlight', methods=['GET','POST'])
def getlight():
    light = grove.read_light_sensor_analogueport(1) #get light sensor from a1
    return jsonify({ "Light":light })

#return temp values
@app.route('/gettemphumidity', methods=['GET','POST'])
def gettemphumidity():
    [temp,humidity] = grove.read_temp_humidity_sensor_digitalport(3) #get temperature and humidity
    return jsonify({ "Temperature":temp, "Humidity":humidity })


#---------------------------------------------------------------
#Shutdown the web server
@app.route('/shutdown', methods=['GET','POST'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return jsonify({ "message":"shutting down" }) 

#Threaded mode is important if using shared resources e.g. sensor, each user request launches a thread.. 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=False)
