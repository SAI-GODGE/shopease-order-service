# ShopEase Order Service

A containerized e-commerce order-tracking application demonstrating
Podman Containerfiles, Podman Compose, container networking, and
Podman Pods using Kubernetes YAML.

## Architecture

```text
                    Client
                      |
                :8080 / :8081
                      |
                      v
              +---------------+
              |     Nginx     |
              |    Gateway    |
              +-------+-------+
                      |
                    /api/*
                      |
                      v
              +---------------+
              | Flask +       |
              | Gunicorn API  |
              |    :5000      |
              +-------+-------+
                      |
                      v
              +---------------+
              | PostgreSQL 16 |
              |    :5432      |
              +---------------+
```
Components

| Component | Technology | Role |
|---|---|---|
| Gateway | Nginx | Reverse proxy / public entry point |
| API | Flask + Gunicorn | Create, list and update orders |
| Database | PostgreSQL 16 | Store order data |
