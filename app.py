import tkinter as tk
from model import BitcoinPredictor

predictor = BitcoinPredictor("bitcoin.csv")

def predict():
    try:
        current_price = float(entry.get())
        prediction = predictor.predict_price(current_price)
        result_label.config(text=f"Predicted Next Day Price: ${prediction:.2f}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

def show_graph():
    predictor.plot_predictions()

# Create GUI window
app = tk.Tk()
app.title("Bitcoin Price Predictor")
app.geometry("400x250")

tk.Label(app, text="Enter Current BTC Price ($):").pack(pady=10)
entry = tk.Entry(app)
entry.pack()

tk.Button(app, text="Predict", command=predict).pack(pady=10)
result_label = tk.Label(app, text="")
result_label.pack(pady=5)

tk.Button(app, text="Show Prediction Graph", command=show_graph).pack(pady=10)

app.mainloop()
