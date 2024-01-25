# Make sure you have Docker installed on your system. You can download and install Docker from the official website: https://www.docker.com/get-started
# Navigate to the project directory
# Build a Docker image using Dockerfile.

docker build -t image_name:tag .

# Once the image is built successfully, you can run a Docker container based on that image. 

docker run -d --name container_name -p 8080:5000 image_name:tag

# Run the app by navigating through the following url.

http://localhost:8080/

# Pushing the image to Docker Hub

Create a repository in your docker hub account. 

# Login to Docker Hub: Before pushing your image, you need to log in to your Docker Hub account using the docker login command.

docker login -u user_name

# Tag Your Docker Image: You need to tag your Docker image with your Docker Hub username and a repository name. 

docker tag image_name:tag user_name/repository_name:tag

# Push the Docker Image to Docker Hub:

docker push user_name/repository_name:v1

https://hub.docker.com/r/shahinmahmud53/employee-churn-prediction-flask-app