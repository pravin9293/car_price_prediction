import pickle
import numpy as np
import pandas as pd
import config

class CarPricePrediction:

    def __init__(self,name,company,year,kms_driven,fuel_type):
        self.name = name
        self.company = company
        self.year = year
        self.kms_driven = kms_driven
        self.fuel_type = fuel_type
        print('name',self.name)

    def load_model(self):

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.linear_model = pickle.load(f)

    
    def get_car_price(self):

        self.load_model()

        test_array = np.array([self.name,self.company,self.year,self.kms_driven,self.fuel_type])
        print('test_array',test_array)

        price = self.linear_model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                              data=np.array([self.name,self.company,self.year,self.kms_driven,self.fuel_type]).reshape(1, 5)))

        return int(price[0])