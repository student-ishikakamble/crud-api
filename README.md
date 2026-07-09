# DevOps Technical Assessment: Multi-Application CI/CD Deployment with AWS, Jenkins, Docker and Nginx

## Project Overview

This project was developed as part of a DevOps Technical Assessment to demonstrate production-grade infrastructure design, CI/CD automation, reverse proxy configuration, application isolation, security practices, and deployment automation.

The environment hosts two independent applications on a single server while maintaining complete deployment and database separation.

### Applications

#### Application 1 — CRUD API

A custom CRUD API built specifically for this assessment.

Features:

* REST API implementation
* PostgreSQL database integration
* Dockerized deployment
* Health monitoring endpoint
* Jenkins CI/CD pipeline
* Automated deployment

Repository:
`student-ishikakamble/crud-api`

---

#### Application 2 — Multi-Auth

An existing MERN authentication application deployed from the provided repository.

Features:

* React frontend
* Express backend
* Prisma ORM
* PostgreSQL database
* Dockerized deployment
* Jenkins CI/CD pipeline
* Automated Prisma migrations

Repository:
Fork of the provided Multi-Auth project.

---

# Architecture Overview

```text
                           Internet
                               │
                               ▼
                    Nginx Reverse Proxy
                               │
         ┌─────────────────────┴─────────────────────┐
         │                                           │
         ▼                                           ▼

crud-ishika.duckdns.org                 auth-ishika.duckdns.org
        │                                         │
        ▼                                         ▼

CRUD API Container                     Multi-Auth Container
Port 8000                              Port 5000
        │                                         │
        ▼                                         ▼

PostgreSQL Database                    PostgreSQL Database
```

The reverse proxy layer ensures both applications can coexist on a single server without port conflicts while remaining publicly accessible through independent domains.

---

# Infrastructure Components

| Component             | Technology Used |
| --------------------- | --------------- |
| Cloud Provider        | AWS EC2         |
| Reverse Proxy         | Nginx           |
| CI/CD Platform        | Jenkins         |
| Container Runtime     | Docker          |
| Database              | PostgreSQL      |
| SSL Certificates      | Let's Encrypt   |
| Domain Provider       | DuckDNS         |
| Authentication DB ORM | Prisma          |
| CRUD API Framework    | FastAPI         |

---

# Public Endpoints

## CRUD API

Production URL:

https://crud-ishika.duckdns.org

Health Check:

https://crud-ishika.duckdns.org/health

---

## Multi-Auth Application

Production URL:

https://auth-ishika.duckdns.org

---

# Reverse Proxy Design

Both applications run on the same EC2 instance.

Internal application ports:

| Application | Internal Port |
| ----------- | ------------- |
| CRUD API    | 8000          |
| Multi-Auth  | 5000          |

External traffic enters through Nginx on ports 80 and 443.

Nginx routes requests based on the incoming hostname:

* requests for `crud-ishika.duckdns.org` are forwarded to port `8000`
* requests for `auth-ishika.duckdns.org` are forwarded to port `5000`

This prevents port conflicts and allows multiple applications to share a single server.

---

# Database Strategy

The assessment allowed either:

* Separate PostgreSQL instances
* One PostgreSQL instance with multiple databases

The chosen strategy was:

## Dedicated database per application

### CRUD API Database

Used exclusively by the CRUD application.

### Multi-Auth Database

Used exclusively by the Multi-Auth application.

Advantages:

* Strong logical separation
* Easier backups and restores
* Reduced accidental cross-application access
* Independent schema management

---

# CI/CD Design

## CRUD API Pipeline

Pipeline Stages:

1. Source checkout
2. Docker build
3. Container deployment
4. Health check validation

Health Check Endpoint:

```text
/health
```

Failure Criteria:

* HTTP status not equal to 200
* Database connection failure
* Application startup failure

Rollback Strategy:

If the health endpoint fails after deployment, the pipeline restores the last known working container image.

---

## Multi-Auth Pipeline

Pipeline Stages:

1. Pull latest source code
2. Install dependencies
3. Build React frontend
4. Execute Prisma migrations
5. Restart application containers
6. Execute health validation

Migration Command:

```text
npx prisma migrate deploy
```

Failure Handling:

If migrations fail:

* deployment stops immediately
* application restart is prevented
* existing production version continues serving traffic

This avoids running an application against an incompatible schema.

---

# Jenkins Configuration

Jenkins runs on a non-default port as required by the assessment.

Jenkins URL:

```text
http://65.0.18.126:8081
```

Configured Jobs:

1. crud-api-pipeline
2. devops-assignment-pipeline
3. Multi-Auth-Pipeline

All pipelines are defined using Jenkinsfiles stored in source control.

No deployment logic exists only inside Jenkins UI.

---

# Jenkins Access Control

Two user roles were created:

## Administrator

Permissions:

* Full administrative access
* Pipeline management
* Credential management

## Assessment Reviewer

Permissions:

* Read access only
* View jobs
* View build history
* View workspaces

Reviewer accounts cannot modify jobs or infrastructure resources.

---

# IAM Access Strategy

A dedicated read-only IAM policy was created for reviewers.

Allowed capabilities include:

* Describe EC2 instances
* Describe RDS resources
* Read CloudWatch metrics
* Read CloudWatch logs

Administrative actions were intentionally excluded.

The default AWS managed ReadOnlyAccess policy was not used to avoid granting unnecessary permissions.

---

# Secrets Management

Sensitive information was never committed to Git.

Examples include:

* Database passwords
* AWS credentials
* Application secrets
* API keys
* Jenkins credentials

Secrets are provided through:

* Environment variables
* Jenkins Credentials Store
* Runtime configuration files

No secrets exist inside repository history or Docker image layers.

---

# Open Ports and Justification

| Port | Purpose                       |
| ---- | ----------------------------- |
| 22   | SSH administration            |
| 80   | HTTP traffic                  |
| 443  | HTTPS traffic                 |
| 8081 | Jenkins access                |
| 5000 | Internal Multi-Auth container |
| 8000 | Internal CRUD API container   |

Only required ports were exposed.

---

# SSL Configuration

TLS certificates were provisioned using Let's Encrypt and Certbot.

Enabled Domains:

* https://crud-ishika.duckdns.org
* https://auth-ishika.duckdns.org

Certificates renew automatically using Certbot scheduled tasks.

---

# Security Controls

Implemented controls include:

* HTTPS enabled
* Reverse proxy isolation
* Least privilege IAM access
* Jenkins role separation
* Secrets stored outside Git
* Dedicated databases
* Docker container isolation

---

# Instance Sizing Rationale

A lightweight EC2 instance was selected because:

* workloads are low traffic
* applications are containerized
* PostgreSQL usage is moderate
* Jenkins workloads are intermittent

This balances operational cost with performance requirements.

---

# Future Improvements

Potential production improvements include:

* Blue-Green deployments
* Kubernetes orchestration
* Automated backups
* Centralized logging
* Prometheus monitoring
* Grafana dashboards
* Web Application Firewall
* Auto-scaling

---

# Conclusion

This project demonstrates the deployment and operation of multiple production-style applications on a shared infrastructure while maintaining isolation, security, automation, and reproducibility.

The focus of the implementation was not only successful deployment but also operational reasoning, security boundaries, and maintainable infrastructure practices.
