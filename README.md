# ML-K8s-Fastapi

A basic Iris flower classifier API built with Scikit-learn and FastAPI, designed for deployment to Kubernetes.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Clone the Repository](#clone-the-repository)
  - [Build the Docker Image](#build-the-docker-image)
  - [Run Locally with Docker](#run-locally-with-docker)
  - [Deploy to Kubernetes](#deploy-to-kubernetes)
- [API Endpoints](#api-endpoints)
  - [POST /predict](#post-predict)
- [Project Structure](#project-structure)
- [Makefile Commands](#makefile-commands)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project demonstrates how to build a machine learning model (Iris flower classification) and expose it as a REST API using FastAPI. The application is containerized using Docker and can be deployed to a Kubernetes cluster.

## Features

- Iris flower species prediction based on sepal and petal measurements.
- RESTful API for easy integration.
- Dockerized for consistent environments and deployment.
- Kubernetes-ready with deployment and service manifests.
- Makefile for streamlined build, run, and deployment tasks.

## Tech Stack

- **Python**: Core programming language.
- **FastAPI**: High-performance web framework for building APIs.
- **Scikit-learn**: Machine learning library for the Iris model.
- **Joblib**: For saving and loading the trained Scikit-learn model.
- **Uvicorn**: ASGI server for running FastAPI.
- **Poetry**: Dependency management and packaging.
- **Docker**: Containerization.
- **Kubernetes (Minikube)**: Container orchestration for deployment.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/) (or any Kubernetes cluster)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [Make](https://www.gnu.org/software/make/) (optional, for using Makefile commands)
- [Git](https://git-scm.com/downloads)

## Getting Started

### Clone the Repository

```bash
git clone <your-repository-url>
cd ML-K8s-Fastapi
```

### Build the Docker Image

You can build the Docker image using the provided Makefile or directly with Docker.

**Using Makefile:**
```bash
make build
```

**Using Docker:**
```bash
docker build -t your-dockerhub-username/ml-k8s-fastapi:latest .
```
*(Replace `your-dockerhub-username` with your Docker Hub username or preferred image name).*

### Run Locally with Docker

**Using Makefile:**
```bash
make run
```
This will typically start the container on `http://localhost:9000` (or the port specified in the Makefile).

**Using Docker:**
```bash
docker run -d --name ml-k8s-fastapi-container -p 9000:5000 your-dockerhub-username/ml-k8s-fastapi:latest
```
*(The internal container port is `5000`. You can map it to any host port, here `9000` is used).*

Access the API at `http://localhost:9000/docs` for the Swagger UI.

### Deploy to Kubernetes

1.  **Start Minikube** (if not already running):
    ```bash
    minikube start
    ```

2.  **Apply Kubernetes Manifests:**
    The `deployment.yaml` and `service.yaml` files are located in the `k8s/` directory.

    **Using Makefile:**
    ```bash
    make deploy
    ```

    **Using kubectl:**
    ```bash
    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml
    ```

3.  **Access the Service:**
    Get the service URL.

    **Using Makefile:**
    ```bash
    make url
    ```

    **Using kubectl:**
    ```bash
    minikube service ml-k8s-fastapi-service --url
    ```
    This will provide a URL (e.g., `http://<minikube-ip>:<node-port>`). Access the Swagger UI at `http://<minikube-ip>:<node-port>/docs`.

## API Endpoints

### POST /predict

Predicts the Iris flower species.

-   **URL:** `/predict`
-   **Method:** `POST`
-   **Request Body (JSON):**
    ```json
    {
      "sepal_length": 5.1,
      "sepal_width": 3.5,
      "petal_length": 1.4,
      "petal_width": 0.2
    }
    ```
-   **Success Response (200 OK):**
    ```json
    {
      "prediction": 0 
    }
    ```
    *(Where `0` might represent 'Iris Setosa', `1` 'Iris Versicolour', and `2` 'Iris Virginica' - this depends on your model's class encoding. You might want to return the class name directly for better usability.)*

## Project Structure

```
ML-K8s-Fastapi/
├── .gitignore
├── Dockerfile
├── Makefile
├── README.md
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── pyproject.toml
└── src/
    ├── __init__.py
    ├── main.py     # FastAPI application
    └── model.py    # Model training and saving script (if separate)
```

## Makefile Commands

-   `make build`: Builds the Docker image and pushes it (if configured).
-   `make run`: Runs the Docker container locally.
-   `make deploy`: Deploys the application to Minikube.
-   `make clean`: Removes the Docker image, stops and deletes the Docker container, and deletes Kubernetes resources.
-   `make url`: Fetches and prints the service URL from Minikube.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## License

Distributed under the MIT License. See `LICENSE` file for more information (you'll need to create this file if you want one).