## Dev environment: Windows 10, VSCode

# To run the project in localhost (without Docker)

# Make sure you have the Python 3.11.0 installed on your PC

# Install and activate virtual environment

python -m venv myenv

myenv/Scripts/activate

# Upgrade pip installer

python -m pip install pip --upgrade

# Install python packages:

pip install -r requirements.txt

# Run the app

py app.py

# To run the project in localhost (Docker)

# Make sure you have Docker installed on your system. You can download and install Docker from the official website: https://www.docker.com/get-started
# Navigate to the project directory

docker pull shahinmahmud53/employee-churn-prediction-flask-app:v1

docker run -d --name container_name -p 8080:5000 shahinmahmud53/employee-churn-prediction-flask-app:v1