# Importpi
from flask import Flask, render_template

app = Flask(__name__)


#def result_calculate(distance, gas, consumption):
# Zmienne umożliwiające obliczenie poboru energii przez urządzenia
 #   if distance == "150 km lub mniej":
  #      distance = 150
   # elif distance == "500 km":
    #    distance = 500
   # elif distance == "1000 km lub więcej":
    #    distance = 1000
        
    #if gas == "Benzyna":
      #  gas = 2392
    #elif gas == "Diesel":
      #  gas = 2650
    #elif gas == "Hybryd":
     #   gas = 2200
    
    #if consumption == "5L/100km lub więcej":
     #   consumption = 0.05
    #elif consumption == "ok. 8L/100km":
      #  consumption = 0.08
    #elif consumption == "10L/100km lub więcej":
     #   consumption = 0.1

   # return (distance * consumption * gas)/1000

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