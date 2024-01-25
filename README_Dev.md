Certainly! Here's the rewritten README.md file with proper Markdown formatting:

```markdown
# Docker Setup for Project

This guide outlines the steps to set up Docker for this project.

## Prerequisites
- Ensure you have Docker installed on your system. If not, download and install it from the [official Docker website](https://www.docker.com/get-started).

## Steps

### 1. Navigate to Project Directory
- Change into the directory where your project is located.

### 2. Build Docker Image
- Use the following command to build a Docker image using the Dockerfile:

  ```bash
  docker build -t image_name:tag .
  ```

### 3. Run Docker Container
- Once the image is built successfully, run a Docker container based on that image:

  ```bash
  docker run -d --name container_name -p 8080:5000 image_name:tag
  ```

### 4. Access the Application
- The app can be accessed through the following URL: [http://localhost:8080/](http://localhost:8080/)

## Pushing the Image to Docker Hub

### 1. Create a Repository
- Create a repository in your Docker Hub account.

### 2. Login to Docker Hub
- Log in to your Docker Hub account using the following command:

  ```bash
  docker login -u user_name
  ```

### 3. Tag Your Docker Image
- Tag your Docker image with your Docker Hub username and a repository name:

  ```bash
  docker tag image_name:tag user_name/repository_name:tag
  ```

### 4. Push the Docker Image
- Push the Docker image to Docker Hub:

  ```bash
  docker push user_name/repository_name:v1
  ```

- Docker Hub Repository Link: [Employee Churn Prediction Flask App](https://hub.docker.com/r/shahinmahmud53/employee-churn-prediction-flask-app)
```
