from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load your saved pipeline (including preprocessor and model)
pipeline = joblib.load('models/dataset-1_model_rf.pkl')

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from the form
        satisfaction = float(request.form['satisfaction'])
        last_evaluation = float(request.form['last_evaluation'])
        n_projects = int(request.form['n_projects'])
        avg_monthly_hrs = int(request.form['avg_monthly_hrs'])
        tenure = int(request.form['tenure'])
        recently_promoted = request.form['recently_promoted']
        filed_complaint = request.form['filed_complaint']
        department = request.form['department']
        salary = request.form['salary']

        # Create a DataFrame with user input
        user_data = pd.DataFrame({
            'satisfaction': [satisfaction],
            'last_evaluation': [last_evaluation],
            'n_projects': [n_projects],
            'avg_monthly_hrs': [avg_monthly_hrs],
            'tenure': [tenure],
            'recently_promoted': [recently_promoted],
            'filed_complaint': [filed_complaint],
            'department': [department],
            'salary': [salary]
        })

        # Preprocess user input and make a prediction using the loaded pipeline
        prediction = pipeline.predict(user_data)

        # Determine the result message
        if prediction[0] == 1:
            result_message = "Employee may leave the organization"
        else:
            result_message = "Employee may stay with the organization"

        return render_template('index.html', result_message=result_message)

    return render_template('index.html', result_message=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
