
#!/bin/bash

set -e

echo "🚀 Starting local deployment of Barkuni DevOps Task..."

# Step 1: Build Docker image
echo "📦 Building Docker image..."
cd api
docker build -t barkuni-api:latest .
cd ..

# Step 2: Load image into Minikube (if applicable)
if command -v minikube &> /dev/null; then
  echo "📦 Loading Docker image into Minikube..."
  minikube image load barkuni-api:latest
fi

# Step 3: Deploy to Kubernetes
echo "🚀 Applying Kubernetes manifests..."
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Step 4: Wait and get service info
echo "⏳ Waiting for service to be assigned an external IP (or NodePort)..."
kubectl get svc barkuni-api-service --watch
