
# Barkuni Corp DevOps Assessment

This repository contains a solution for the Barkuni Corp DevOps task, showcasing a RESTful Flask API deployed using Docker, Kubernetes, and Terraform.

---

## 🚀 Features

- Flask API with:
  - `/` — Welcome route
  - `/pods` — Lists pods from "kube-system"
- Dockerized and deployed to Kubernetes
- GitHub Actions CI/CD pipeline
- `boto3` script to launch EC2 in a specified subnet

---

## 📦 Local Deployment (Minikube)

Run this script to deploy locally:

```bash
chmod +x run_all.sh
./run_all.sh
```

Then access the service using the Minikube IP and port:

```bash
minikube service barkuni-api-service
```

---

## 🧪 Optional: EC2 Provisioning

Edit and run:

```bash
python scripts/create_ec2.py
```

---

## 🔧 CI/CD with GitHub Actions

- Builds and deploys automatically on push to `main`
- Requires GitHub secrets:
  - `DOCKER_USERNAME`
  - `DOCKER_PASSWORD`

---

## ✅ Submission

1. Kubernetes manifests ✅
2. GitHub repo ✅
3. Working demo (Minikube/port-forward or NodePort) ✅
4. boto3 EC2 script ✅
