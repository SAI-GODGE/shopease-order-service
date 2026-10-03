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
## Components

| Component | Technology | Role |
|---|---|---|
| Gateway | Nginx | Reverse proxy / public entry point |
| API | Flask + Gunicorn | Create, list and update orders |
| Database | PostgreSQL 16 | Store order data |

## Project Structure
```text
shopease-orders/
├── app/
│   ├── Containerfile
│   ├── app.py
│   └── requirements.txt
│
├── db/
│   ├── Containerfile
│   └── init.sql
│
├── nginx/
│   ├── Containerfile
│   └── default.conf.template
│
├── kube/
│   └── order-pod.yaml
│
├── compose.yaml
├── .gitignore
└── README.md
```
## Technologies
- Podman
- Podman Compose
- Kubernetes YAML
- Python
- Flask
- Gunicorn
- PostgreSQL 16
- Nginx
- Linux
- REST API

## 1. Build the Images
From the project root:
```text
podman build -t localhost/shopease-order-db:1.0 ./db

podman build -t localhost/shopease-order-api:1.0 ./app

podman build -t localhost/shopease-gateway:1.0 ./nginx
```
Check the images:
```text
podman images | grep shopease
```
Verify that the API image runs as a non-root user:
```text
podman image inspect localhost/shopease-order-api:1.0 --format '{{.Config.User}}'
```
Expected:
```text
1001
```
## 2. Development with Podman Compose
Start the application:
```text
podman-compose up -d --build
```
Check the services:
```text
podman-compose ps
```
View API logs:
```text
podman-compose logs api
```
Health Check
```text
curl http://localhost:8080/api/health
```
List Orders
```text
curl http://localhost:8080/api/orders
```
Get a Specific Order
```text
curl http://localhost:8080/api/orders/1
```
Create an Order
```text
curl -X POST http://localhost:8080/api/orders -H "Content-Type: application/json" -d '{"customer":"Rahul Mehta","item":"Laptop Stand","quantity":1}'
```
Update Order Status
```text
curl -X PATCH http://localhost:8080/api/orders/4 -H "Content-Type: application/json" -d '{"status":"SHIPPED"}'
```
## 3. Container Exposure
Only the Nginx gateway is exposed to the host.
Check the gateway:
```text
podman port shopease-gateway
```
Expected:
```text
80/tcp -> 0.0.0.0:8080
```
Check the API:
```text
podman port shopease-api
```
The API has no host port mapping.
## 4. Staging with Podman Pod
Stop the Compose deployment:
```text
podman-compose down
```
Deploy the Pod:
```text
podman kube play kube/order-pod.yaml
```
Check the Pod:
```text
podman pod ps
```
Check containers inside the Pod:
```text
podman ps --pod --filter pod=shopease-orders
```
Staging Health Check
```text
curl http://localhost:8081/api/health
```
Staging Orders
```text
curl http://localhost:8081/api/orders
```
## 5. Pod Logs
API logs:
```text
podman logs shopease-orders-api
```
Database logs:
```text
podman logs shopease-orders-db
```
## 6. Verify PostgreSQL
```text
podman exec -it shopease-orders-db psql -U shopease -d orders -c "SELECT * FROM orders;"
```
## 7. Networking Difference
### Podman Compose
The API communicates with PostgreSQL using the Compose service name:
```text
DB_HOST=db
```
Nginx communicates with the API using:
```text
API_HOST=api
```
### Podman Pod
All three containers run inside the same Pod and share the network namespace.
Therefore:
```text
DB_HOST=127.0.0.1
API_HOST=127.0.0.1
```
This allows the application configuration to remain flexible between the two deployment models.
## 8. Same Images, Two Deployment Models
The same images are used in both environments:
```text
                 Same Images
                     |
          +----------+----------+
          |                     |
          v                     v
   Podman Compose          Podman Pod
    Development             Staging
       :8080                   :8081
```
Only the runtime configuration changes.
## 9. Roll Out a Change
After modifying the Pod YAML:
```text
podman kube play --replace kube/order-pod.yaml
```
## 10. Cleanup
Remove the staging Pod:
```text
podman kube down kube/order-pod.yaml
```
## Key Learnings
- Building container images with Containerfiles
- Running multi-container applications with Podman Compose
- Using Nginx as a reverse proxy
- Connecting Flask with PostgreSQL
- Container-to-container networking
- Running containers inside a Pod
- Using Kubernetes YAML with Podman
- Reusing the same images across deployment models
- Running the API container as a non-root user
- Exposing only the gateway to the host
