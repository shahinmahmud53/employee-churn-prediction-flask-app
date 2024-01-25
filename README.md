# Employee Churn Prediction Flask App

## Development Environment

- **Operating System**: Windows 10
- **IDE**: Visual Studio Code (VSCode)

## Running the Project Locally (Without Docker)

Before running the project, ensure that you have Python 3.11.0 installed on your PC.

### Setting up your Environment

#### Create a virtual environment named 'myenv'

* python -m venv myenv *

#### Activate the virtual environment (Windows)

* myenv\Scripts\activate *

#### Upgrading Pip

* python -m pip install pip --upgrade *

#### Install dependencies

* pip install -r requirements.txt *

#### Run the app

* py app.py *


## Running the Project Locally (Docker)

### Make sure you have Docker installed on your system. You can download and install Docker from the official website: https://www.docker.com/get-started

#### Pulling the Docker image

* cd /path/to/employee-churn-prediction-flask-app *

* docker pull shahinmahmud53/employee-churn-prediction-flask-app:v1 *

#### Running a Docker Container

* docker run -d --name container_name -p 8080:5000 shahinmahmud53/employee-churn-prediction-flask-app:v1 *

Replace container_name with a suitable name for your Docker container.

Now, you can access the app in your web browser at http://localhost:8080.