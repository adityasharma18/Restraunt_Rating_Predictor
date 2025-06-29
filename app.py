from flask import Flask, render_template, request
import pickle
import pandas as pd

# Initialize Flask App
app = Flask(__name__)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Input from form
        votes = int(request.form['votes'])
        cost = float(request.form['cost'])

        # Make dataframe for model
        input_df = pd.DataFrame([[votes, cost]], columns=['votes', 'cost'])

        # Predict
        prediction = model.predict(input_df)[0]
        prediction = round(prediction, 1)

        # Clamp prediction between 0 and 5
        prediction = max(0.0, min(prediction, 5.0))


        return render_template('index.html', prediction_text=f"⭐ Predicted Rating: {prediction} / 5.0")

    except Exception as e:
        return render_template('index.html', prediction_text=f"❌ Error: {e}")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

