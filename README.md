# Sample API Application

A simple Flask application that runs on port 80 and returns sample API responses.

## Requirements

- Python 3.x
- pip (Python package installer)

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

### Direct Python Execution
Since the application runs on port 80, you'll need to use sudo (on Unix-based systems):

```bash
sudo python app.py
```

Or run on a different port using the PORT environment variable:

```bash
PORT=8080 python app.py
```

### Using Docker
Build the Docker image:
```bash
docker build -t sample-api .
```

Run the container:
```bash
docker run -p 80:80 sample-api
```

Or run on a different port:
```bash
docker run -p 8080:80 sample-api
```

### Using Kubernetes
The application can be deployed to Kubernetes using the provided configuration files in the `k8s` directory.

1. First, build the Docker image (if not already built):
```bash
docker build -t sample-api .
```

2. Apply the Kubernetes configurations:
```bash
kubectl apply -f k8s/
```

This will create:
- A Deployment with 3 replicas
- A HorizontalPodAutoscaler (HPA) that scales based on CPU utilization (target: 60%)
- A NodePort Service exposing the application on port 30080

You can access the application at: http://localhost:30080

To check the status of your deployment:
```bash
kubectl get deployments
kubectl get pods
kubectl get hpa
kubectl get services
```

The HPA will automatically scale the pods between 3 and 10 replicas based on CPU utilization, maintaining an average CPU utilization of 60%.

## API Endpoints

- GET `/`: Returns a sample JSON response with some dummy data
- Any other path will return a 404 error with a JSON error message

## Sample Response

```json
{
    "message": "Welcome to Sample API",
    "status": "success",
    "data": {
        "items": [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
            {"id": 3, "name": "Item 3"}
        ]
    }
}
