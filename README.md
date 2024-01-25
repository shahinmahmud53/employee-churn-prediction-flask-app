# Employee Churn Prediction Flask App

## Development Environment

- **Operating System**: Windows 10
- **IDE**: Visual Studio Code (VSCode)

## Running the Project Locally

### Without Docker

Ensure you have Python 3.11.0 installed on your PC before proceeding.

#### Setting Up Your Environment

1. **Create a Virtual Environment**
   ```bash
   python -m venv myenv
   ```

2. **Activate the Virtual Environment (Windows)**
   ```bash
   myenv\Scripts\activate
   ```

3. **Upgrade Pip**
   ```bash
   python -m pip install --upgrade pip
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the App**
   ```bash
   py app.py
   ```

### With Docker

#### Prerequisites
- Make sure Docker is installed on your system. Download it from the [official Docker website](https://www.docker.com/get-started).

#### Running the Docker Version

1. **Navigate to the Project Directory**
   ```bash
   cd /path/to/employee-churn-prediction-flask-app
   ```

2. **Pull the Docker Image**
   ```bash
   docker pull shahinmahmud53/employee-churn-prediction-flask-app:v1
   ```

3. **Run a Docker Container**
   Replace `container_name` with a suitable name for your Docker container.
   ```bash
   docker run -d --name container_name -p 8080:5000 shahinmahmud53/employee-churn-prediction-flask-app:v1
   ```

Now, you can access the app in your web browser at [http://localhost:8080](http://localhost:8080).