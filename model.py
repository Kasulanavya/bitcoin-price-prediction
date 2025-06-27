import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

class BitcoinPredictor:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
        self.model = LinearRegression()
        self.prepare_data()

    def prepare_data(self):
        self.data = self.data[['Close']].dropna()
        self.data['Prediction'] = self.data[['Close']].shift(-1)
        self.data.dropna(inplace=True)

        self.X = np.array(self.data[['Close']])
        self.y = np.array(self.data['Prediction'])
        self.model.fit(self.X, self.y)

    def predict_price(self, current_price):
        return self.model.predict([[current_price]])[0]
    
    def plot_predictions(self):
        predicted = self.model.predict(self.X)
        plt.figure(figsize=(8, 4))
        plt.plot(self.y, label='Actual Prices', linewidth=2)
        plt.plot(predicted, label='Predicted Prices', linestyle='--')
        plt.title("Bitcoin Price Prediction")
        plt.xlabel("Days")
        plt.ylabel("Price ($)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
