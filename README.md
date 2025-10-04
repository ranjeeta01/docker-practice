# 🐳 Docker Practice

This repository is a simple hands-on project to practice the basics of Docker — from building an image to running a containerized web application.

## 🚀 Project Overview
This project covers the following steps:

1. **Create a simple web application**  
   Build a minimal web app (for example, Node.js or Python Flask) to serve as the containerized application.

2. **Write a Dockerfile**  
   Define the environment and dependencies for the web app using a `Dockerfile`.

3. **Build the Docker image**
   ```bash
   # From the directory with your Dockerfile
   docker build -t Dockerfile.
   ```
   This command creates a Docker image from the Dockerfile and tags it as `simple-webapp`.

4. **Rename the image and add a tag**
   ```bash
   # Using the image ID
   docker tag <image-id> simple-webapp:v1

   # Or tag by existing name
   docker tag simple-webapp opt/simple-webapp:v1
   ```
   Replace `<image-id>` with the actual ID shown by `docker images`.

5. **Run the Docker container**
   ```bash
   docker run -d -p 8080:8080 --name simple-webapp_container mywebapp:v1
   ```
   This runs the container in detached mode and maps container port `8080` to host port `8080`.

6. **Verify the app**
   Open your browser and visit:
   ```
   http://localhost:8080
   ```
   You should see your web application running inside Docker.

## 🔍 Useful commands
- List images: `docker images`
- List running containers: `docker ps`
- View container logs: `docker logs <container-name-or-id>`
- Stop & remove a container:
  ```bash
  docker stop simple-webapp_container
  docker rm simple-webapp_container
  ```

Happy Coding!!
