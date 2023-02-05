from flask import Flask , request , jsonify, render_template
from utils import CarPricePrediction
import traceback
import config

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/carprice', methods = ['GET','POST'])
def carprice():
    try :
        if request.method == "GET":

            data = request.args.get
            
            name = data('name')
            company = data('company')
            year = int(data('year'))
            kms_driven = int(data('kms_driven'))
            fuel_type = data('fuel_type')

            print(name,company,year,kms_driven,fuel_type)

            print('Data:',data)

            carprice = CarPricePrediction(name,company,year,kms_driven,fuel_type)
            predicted_price = carprice.get_car_price()

            # return jsonify({'Predicted Car Price':f'{predicted_price}'})
            return render_template('index.html',prediction = predicted_price)
        
        else:
            data = request.form.get
            
            name = data('name')
            company = data('company')
            year = int(data('year'))
            kms_driven = int(data('kms_driven'))
            fuel_type = data('fuel_type')

            print(name,company,year,kms_driven,fuel_type)

            print('Data:',data)

            carprice = CarPricePrediction(name,company,year,kms_driven,fuel_type)
            predicted_price = carprice.get_car_price()

            return render_template('index.html',prediction = predicted_price)
            

    except:
        print(traceback.print_exc())
        return  jsonify({"Message" : "Unsuccessful"})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=config.PORT_NUMBER,debug=False)


