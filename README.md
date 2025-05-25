
# Barkuni Corp DevOps Assessment

This repository is a complete solution for Barkuni Corp’s DevOps evaluation scenario. It demonstrates proficiency in:

- ✅ Python (Flask-based RESTful API)
- ✅ Docker containerization
- ✅ Kubernetes manifests
- ✅ Terraform with AWS modules
- ✅ GitHub Actions CI/CD
- ✅ Local cluster deployment with Minikube
- ✅ Bonus: EC2 provisioning using boto3

---

## 📜 Scenario Description

Barkuni Corp wants to assess candidates for proficiency in Python, RESTful APIs, and containerized applications. You are tasked with:

- Designing, building, and testing a REST API backend service
- Deploying it to a Kubernetes cluster (Minikube or EKS)
- Implementing optional features: ALB, Route53 DNS, GitHub Actions pipeline, boto3 automation

---

## 🛠️ Tools & Technologies Used

- Python (Flask)
- Docker
- Kubernetes (Minikube-ready)
- Terraform (EKS-compatible)
- GitHub Actions
- boto3 for EC2 provisioning

---

## 🚀 Features

- `/` — Welcome route
- `/pods` — Lists pods from "kube-system" namespace
- Image built and deployed locally (avoids DockerHub pulls)

---

## 📦 Local Deployment (Minikube)

Run this to deploy locally:
```bash
chmod +x run_all.sh
./run_all.sh
```

Then access in browser:
```bash
minikube service barkuni-api-service
```

Or:
```bash
http://$(minikube ip):<NodePort>
```

---

## ☁️ Cloud Deployment (Optional)

You may provision EKS with Terraform modules (permissions permitting).

---

## 🔁 CI/CD Pipeline (GitHub Actions)

Push to `main` triggers:
- Docker build
- Kubernetes manifest apply

Configure GitHub Secrets:
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`

---

## 🧪 boto3 EC2 Launch Script

Run the EC2 provisioning script:
```bash
python scripts/create_ec2.py
```

This script supports:
- AMI ID
- Subnet ID
- Instance type (Linux/Windows)

---

## ✅ Submission Requirements

- Kubernetes manifests ✅
- GitHub repo with code ✅
- Local working deployment (Minikube) ✅
- boto3 provisioning script ✅
- GitHub Actions workflow ✅

---

## 📝 Notes

- ALB/Route53 skipped due to IAM restrictions
- Uses NodePort and local image loading into Minikube


---

## ⚠️ Limitations & Notes

- The ALB + Route53 configuration is included in the Terraform module and written correctly using AWS best practices.
- However, due to IAM permission limits on the user `devops2`, the ALB could not be created or tested.
- All local functionality (Minikube-based deployment, image loading, API responses) has been fully verified.
