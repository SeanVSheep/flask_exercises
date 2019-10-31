from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/f')
@app.route('/f/<temp>')
def fahrenheit(temp):
    return "Fahrenheit({:.2f}) to Celsius({:.2f})".format(float(temp), (float(temp) - 32) * 5 / 9)


@app.route('/c')
@app.route('/c/<temp>')
def celsius(temp):
    return "Celsius({:.2f}) to Fahrenheit({:.2f})".format(float(temp), float(temp) * 9.0 / 5 + 32)


if __name__ == '__main__':
    app.run()
