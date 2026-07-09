# DevOps Engineer Assessment Project

## Overview

This project demonstrates a production-style deployment of two independent web applications on a single Linux server using modern DevOps practices.

The deployment includes:

* Docker containerization
* Nginx reverse proxy configuration
* SSL/TLS encryption using Let's Encrypt
* Automated SSL certificate renewal using Certbot
* Jenkins CI/CD pipeline automation
* API documentation using Swagger/OpenAPI
* Domain-based application routing
* Secure environment-based configuration management

---

# Applications Deployed

## 1. CRUD API Application

A FastAPI-based CRUD application providing user management APIs with database integration.

### Features

* REST API implementation
* User creation and retrieval
* User deletion
* Database connectivity
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

## Root Endpoint

URL:

```
https://crud-ishika.duckdns.org
```

Response:

```json
{
  "detail": "Not Found"
}
```

Note:

The root route (`/`) is intentionally not implemented.

The application health and API documentation can be accessed using:

* `/health` for service health verification
* `/docs` for Swagger API documentation

## Available API Endpoints

| Method | Endpoint           | Description                            |
| ------ | ------------------ | -------------------------------------- |
| GET    | `/health`          | Application and database health status |
| GET    | `/users`           | Retrieve all users                     |
| POST   | `/users`           | Create a new user                      |
| GET    | `/users/{user_id}` | Get user by ID                         |
| DELETE | `/users/{user_id}` | Delete user                            |

---

# 2. Multi-Auth Application

Authentication-based web application deployed independently with separate routing and database isolation.

## Production URL

```
https://auth-ishika.duckdns.org
```

---

# Architecture Overview

```text
                         Internet
                            |
                    DuckDNS Domains
                            |
                  Nginx Reverse Proxy
                       (HTTPS/SSL)
                            |
        -----------------------------------------
        |                                       |
crud-ishika.duckdns.org              auth-ishika.duckdns.org
        |                                       |
   FastAPI Application                 Multi-Auth Application
        |                                       |
 PostgreSQL Database                 PostgreSQL Database
```

Both applications run independently on the same server and are exposed through Nginx using separate domains to avoid port conflicts.

---

# Infrastructure & DevOps Implementation

## Containerization

Applications are deployed using Docker containers.

Implemented:

* Docker image creation
* Container networking
* Environment configuration
* Application isolation

---

# Nginx Reverse Proxy

Nginx acts as the entry point for all incoming traffic.

Responsibilities:

* Domain-based routing
* Reverse proxy configuration
* SSL termination
* Security header management
* Traffic forwarding to internal applications

Routing design:

```
crud-ishika.duckdns.org
          |
          |
       Nginx
          |
          |
     FastAPI Container


auth-ishika.duckdns.org
          |
          |
       Nginx
          |
          |
   Multi-Auth Container
```

---

# SSL Configuration

HTTPS is enabled using:

* Let's Encrypt certificates
* Certbot automation
* Automatic certificate renewal

Secured domains:

* https://crud-ishika.duckdns.org
* https://auth-ishika.duckdns.org

---

# Database Strategy

Both applications use independent databases to maintain application isolation.

## CRUD API Database

Dedicated database used for CRUD operations and user management.

## Multi-Auth Database

Separate database used by the authentication application.

Benefits of database separation:

* Prevents schema conflicts
* Improves security isolation
* Allows independent backup and scaling
* Reduces deployment dependency between applications

---

# Port List & Justification

| Port              | Purpose                               |
| ----------------- | ------------------------------------- |
| 22                | SSH server access                     |
| 80                | HTTP traffic and HTTPS redirect       |
| 443               | HTTPS traffic through Nginx           |
| 8081              | Jenkins CI/CD server                  |
| Application Ports | Internal container communication only |

Application ports are not publicly exposed and are accessed only through the Nginx reverse proxy.

---

# CI/CD Pipeline

Both applications use Jenkins-based CI/CD automation.

Pipeline workflow:

```text
Code Commit
      |
      |
GitHub Repository
      |
      |
Jenkins Webhook Trigger
      |
      |
Build
      |
      |
Test
      |
      |
Deploy
      |
      |
Post Deployment Health Check
      |
      |
Rollback on Failure
```

Pipeline implementation:

* Jenkinsfile-based pipelines
* Automated build process
* Automated deployment
* Health verification after deployment
* Rollback mechanism on failure

---

# Rollback Strategy

After every deployment, Jenkins performs application health verification.

Deployment is considered successful when:

* HTTP response status is successful
* Health endpoint returns a healthy response

If the health check fails after configured retries, Jenkins restores the previous stable version to maintain application availability.

---

# Security Implementation

Implemented security practices:

* HTTPS enabled
* SSL certificates automatically renewed
* Nginx reverse proxy protection
* Environment variables for sensitive configuration
* Container isolation
* No secrets committed to GitHub repositories

---

# IAM Security

A dedicated read-only IAM user was created for infrastructure verification.

Permissions are limited to required read operations:

* EC2 describe permissions
* RDS describe permissions
* CloudWatch/log read permissions

No:

* Administrative access
* Write permissions
* Root credentials

are provided.

---

# Deployment Validation

## CRUD API Root Endpoint

```
https://crud-ishika.duckdns.org
```

Expected response:

```json
{
 "detail": "Not Found"
}
```

This is expected because the root route is not defined.

---

## Health Check

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

---

## Swagger API Documentation

FastAPI provides interactive API documentation using Swagger UI.

Swagger URL:

```
https://crud-ishika.duckdns.org/docs
```

---

# Screenshots & Verification

## Swagger API Documentation

<img width="918" height="823" alt="Swagger API Documentation" src="https://github.com/user-attachments/assets/d08b614b-05d5-4540-b9e8-939beed68d3b" />

---

## Health Check Verification

<img width="167" height="87" alt="Health Check Response" src="https://github.com/user-attachments/assets/8e266501-cafc-4952-918a-0f714ed048e0" />

---

## Jenkins CI/CD Pipeline Execution Status

Both application pipelines are executed through Jenkins using Jenkinsfile-based automation.


<img width="1878" height="409" alt="image" src="https://github.com/user-attachments/assets/0c8e99fa-d941-4239-8eba-faba244c2968" />

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

* Jenkins
* Jenkinsfile
* Automated build, test and deployment workflow

## Server

* Cloud Linux Server

---

# Project Completion Summary

The complete production deployment includes:

✅ Two separate applications hosted on one server
✅ Nginx reverse proxy implementation
✅ HTTPS enabled using Let's Encrypt
✅ Docker-based deployment
✅ Swagger/OpenAPI documentation
✅ Health monitoring endpoints
✅ Jenkins CI/CD automation
✅ Database separation strategy
✅ Secure IAM access control
✅ Production URLs verified successfully

---

# Author

**Ishika Kamble**

DevOps Engineer | Cloud | CI/CD | Docker | Kubernetes | AWS

GitHub:

https://github.com/student-ishikakamble

LinkedIn:

https://www.linkedin.com/in/ishika-kamble-b794b0355
