from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/roll-dice')
def roll_dice():
    number = random.randint(1, 6)
    return '<h3>The dice roll returns ' + str(number) + '.</h3>'