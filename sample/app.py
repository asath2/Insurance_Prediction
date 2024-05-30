from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get age from form
        age = int(request.form['age'])
        
        # Prepare the input for the model
        input_data = pd.DataFrame([[age]], columns=['Age'])
        
        # Predict using the loaded model
        prediction = model.predict(input_data)[0]
        
        # Return the result
        return render_template('result.html', eligible=bool(prediction))
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
