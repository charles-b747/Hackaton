from flask import Flask, render_template

app = Flask(__name__)


def result_calculate(distance, gas, consumption):
    if distance == 1:
        distance = 150
    elif distance == 2:
        distance = 500
    elif distance == 3:
        distance = 1000

    if gas == 1:
        gas = 2200
    elif gas == 2:
        gas = 2392
    elif gas == 3:
        gas = 2650
    elif gas == 4:
        gas = 18

    if consumption == 1:
        consumption = 0.05
    elif consumption == 2:
        consumption = 0.08
    elif consumption == 3:
        consumption = 0.10
    elif consumption == 4:
        consumption = 0.25*10

    print(distance,gas,consumption)
    return (distance * consumption * gas)/1000



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<distance>')
def gas(distance):
    return render_template('gas.html', distance=distance)


@app.route('/<distance>/<gas>')
def consumption(distance, gas):
    return render_template('consumption.html', distance = distance, gas = gas)


@app.route('/<distance>/<gas>/<consumption>')
def end(distance, gas, consumption):
    return render_template('end.html', result=result_calculate(int(distance),int(gas), int(consumption)))


app.run(debug=True)