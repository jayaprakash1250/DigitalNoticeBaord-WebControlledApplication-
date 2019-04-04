from flask import Flask
from flask import render_template, request
app = Flask(__name__)

import RPi.GPIO as GPIO
import LiquidCrystalPi
import time as time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LCD = LiquidCrystalPi.LCD(29, 31, 33, 35, 37, 38)

LCD.begin(16,2)

time.sleep(0.5)
LCD.write("      VVIT     ")

LCD.nextline()

time.sleep(0.5)
LCD.write(" E-Notice Board")

@app.route("/")
def index():
    return render_template('web.html')
@app.route("/change", methods=['POST'])
def change():
 if request.method == 'POST':
    # Getting the value from the webpage
   data1 = request.form['lcd']
   LCD.clear()
   LCD.write(data1)
 return render_template('web.html', value=data1)
if __name__ == "__main__":
    app.debug = True
    app.run('192.168.43.110', port=8080,debug=True)
