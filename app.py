from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f'hello {name}'


@app.route('/calculate celsius to fahrenteit')
@app.route('/celsius/<celsius>')
def celsius(celsius=" "):


def calculate_fahrenheit(fahrenheit):
    """Calculating fahrenheit to celsius"""
    fahrenheit_to_celsius = 5 / 9 * (fahrenheit - 32)
    return fahrenheit_to_celsius


def calculate_celsius(celsius):
    """Calculating celsius to fahrenheit"""
    celsius_to_fahrenheit = celsius * 9.0 / 5 + 32
    return celsius_to_fahrenheit


if __name__ == '__main__':
    app.run()
