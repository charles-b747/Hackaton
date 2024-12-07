# Importpi
from flask import Flask, render_template

app = Flask(__name__)


def result_calculate(distance, gas, consumption):
# Zmienne umożliwiające obliczenie poboru energii przez urządzenia
    home_coef = 100
    light_coef = 0.04
    consumptions_coef = 5   
    return distance * home_coef + gas * light_coef + consumption * consumptions_coef 

# Pierwsza strona
@app.route('/')
def index():
    return render_template('index.html')

# Druga strona
@app.route('/<distance>')
def gas(distance):
    return render_template('gas.html', distance=distance)

# Trzecia strona
@app.route('/<distance>/<gas>')
def consumption(distance, gas):
    return render_template('consumption.html', distance = distance, gas = gas)

# Obliczenia
@app.route('/<distance>/<gas>/<consumption>')
def end(distance, gas, consumption):
    return render_template('end.html', result=result_calculate(int(distance),int(gas), int(consumption)))


app.run(debug=True)