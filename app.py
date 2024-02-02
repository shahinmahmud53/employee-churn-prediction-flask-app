from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load your saved pipeline (including preprocessor and model)
pipeline = joblib.load('models/dataset-2_model_lr.pkl')

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from the form
        EnvironmentSatisfaction = int(request.form['EnvironmentSatisfaction'])
        JobInvolvement = int(request.form['JobInvolvement'])
        JobLevel = int(request.form['JobLevel'])
        JobSatisfaction = int(request.form['JobSatisfaction'])
        OverTime = int(request.form['OverTime'])  # Assuming OverTime is a binary field (1 for Yes, 0 for No)
        BusinessTravel = request.form['BusinessTravel']
        EducationField = request.form['EducationField']
        JobRole = request.form['JobRole']
        MaritalStatus = request.form['MaritalStatus']

        # Create a DataFrame with user input
        user_data = pd.DataFrame({
            'EnvironmentSatisfaction': [EnvironmentSatisfaction],
            'JobInvolvement': [JobInvolvement],
            'JobLevel': [JobLevel],
            'JobSatisfaction': [JobSatisfaction],
            'OverTime': [OverTime],
            'BusinessTravel': [BusinessTravel],
            'EducationField': [EducationField],
            'JobRole': [JobRole],
            'MaritalStatus': [MaritalStatus]
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
