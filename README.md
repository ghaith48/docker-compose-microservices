# 🚀 Docker Compose Microservices Platform

A production-style microservices platform built to demonstrate modern **DevOps practices** including containerization, reverse proxying, CI/CD automation, and service orchestration.

This project simulates a real-world backend architecture used in cloud-native environments.

---

## 🧩 Architecture Overview

Client
↓
Nginx (Reverse Proxy)
↓
FastAPI Backend (Dockerized)

All services are connected through a private Docker network and exposed only via Nginx.

---

## 🛠 Technology Stack

| Layer | Technology |
|------|-----------|
| Backend API | FastAPI (Python) |
| Containerization | Docker |
| Orchestration | Docker Compose |
| Reverse Proxy | Nginx |
| CI/CD | GitHub Actions |
| Image Registry | GitHub Container Registry (GHCR) |

---

## 📁 Project Structure

```
docker-compose-microservices/
├── backend/
│ ├── app/
│ │ └── main.py
│ ├── Dockerfile
│ └── requirements.txt
├── nginx/
│ └── nginx.conf
├── docker-compose.yml
├── .env.example
```

---

## 🚀 Running the Project Locally

Make sure Docker and Docker Compose v2 are installed.

```bash
docker compose up -d --build

Access the application:

API: http://localhost

Swagger UI: http://localhost/docs
```

# 👤 Author



Ghaith Takla.

DevOps Engineer | Linux | Cloud | CI/CD.
