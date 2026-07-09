# DevOps Engineer Assessment Project

## Overview

This project demonstrates a production-style deployment of two independent web applications on a single Linux server using modern DevOps practices.

The deployment includes:

* Docker containerization
* Nginx reverse proxy configuration
* SSL/TLS encryption using Let's Encrypt
* Automated certificate renewal using Certbot
* CI/CD pipeline integration
* API documentation with Swagger/OpenAPI
* Production-ready domain-based routing

---

# Applications Deployed

## 1. CRUD API Application

A FastAPI-based CRUD application providing user management APIs.

### Features

* REST API implementation
* User creation and retrieval
* User deletion
* Health monitoring endpoint
* Swagger API documentation
* OpenAPI specification

## Production URLs

| Service               | URL                                          |
| --------------------- | -------------------------------------------- |
| API Base URL          | https://crud-ishika.duckdns.org              |
| Health Check          | https://crud-ishika.duckdns.org/health       |
| Swagger Documentation | https://crud-ishika.duckdns.org/docs         |
| OpenAPI Specification | https://crud-ishika.duckdns.org/openapi.json |


oot Endpoint:
https://crud-ishika.duckdns.org

Response:
{"detail":"Not Found"}

Note:
The root route is intentionally not implemented.
Use /docs for Swagger documentation and /health for service health check.

### Available API Endpoints

| Method | Endpoint           | Description               |
| ------ | ------------------ | ------------------------- |
| GET    | `/health`          | Application health status |
| GET    | `/users`           | Retrieve all users        |
| POST   | `/users`           | Create a new user         |
| GET    | `/users/{user_id}` | Get user by ID            |
| DELETE | `/users/{user_id}` | Delete user               |

---

# 2. Multi-Auth Application

Authentication-based web application deployed separately with independent routing.

## Production URL

```
https://auth-ishika.duckdns.org
```

---

# Architecture

```
                    Internet
                       |
                       |
                 DuckDNS Domains
                       |
        --------------------------------
        |                              |
crud-ishika.duckdns.org       auth-ishika.duckdns.org
        |                              |
        |                              |
        ----------- Nginx Reverse Proxy -----------
                         |
              ------------------------
              |                      |
        FastAPI Container      Auth Application
              |
          Database Layer


```

---

# Infrastructure & DevOps Implementation

## Containerization

Applications are deployed using Docker containers.

Implemented:

* Docker images
* Container networking
* Environment configuration
* Service isolation

## Reverse Proxy

Nginx is configured as the entry point for both applications.

Responsibilities:

* Domain-based routing
* Request forwarding
* Security headers
* SSL termination

## SSL Configuration

HTTPS is enabled using:

* Let's Encrypt certificates
* Certbot automation
* Automatic certificate renewal

Secured domains:

* https://crud-ishika.duckdns.org
* https://auth-ishika.duckdns.org

---

# CI/CD Pipeline

The project includes automated deployment workflow.

Pipeline stages:

```
Code Commit
     |
     |
GitHub Repository
     |
     |
CI Pipeline Trigger
     |
     |
Build Docker Image
     |
     |
Run Validation
     |
     |
Deploy Application
```

---

# Deployment Validation

## CRUD API

### Root Endpoint

```
https://crud-ishika.duckdns.org
```

Response:

```json
{
 "detail": "Not Found"
}
```

This is expected because the application does not define a root (`/`) route.

### Health Check

URL:

```
https://crud-ishika.duckdns.org/health
```

Expected response:

```json
{
 "status": "healthy"
}
```

### Swagger UI

Available at:

```
https://crud-ishika.duckdns.org/docs
```

---

# Security Implementation

Implemented security practices:

* HTTPS enabled
* SSL certificates managed automatically
* Reverse proxy protection using Nginx
* Environment variables for configuration
* Container isolation

---

# Technologies Used

## Backend

* FastAPI
* Python
* REST APIs

## DevOps

* Docker
* Docker Compose
* Nginx
* Linux
* Certbot
* Let's Encrypt

## CI/CD

* GitHub Actions

## Server

* Cloud Linux Server

---

# Project Completion Summary

The complete production deployment includes:

✅ Two separate applications hosted on a single server
✅ Domain-based routing using Nginx
✅ HTTPS enabled with Let's Encrypt SSL
✅ Docker-based deployment
✅ API documentation enabled
✅ Health monitoring endpoints configured
✅ CI/CD workflow implemented
✅ Production URLs verified successfully

---

# Author

**Ishika Kamble**

DevOps Engineer | Cloud | CI/CD | Docker | Kubernetes | AWS

GitHub:
https://github.com/student-ishikakamble

LinkedIn:
www.linkedin.com/in/ishika-kamble-b794b0355
