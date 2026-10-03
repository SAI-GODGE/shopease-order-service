<div align="center">

# 🚀 ShopEase Order Service

### Containerized E-Commerce Order Tracking with Podman

A hands-on DevOps project demonstrating how to build, containerize, and deploy a multi-container order service using **Podman, Podman Compose, Nginx, Flask, PostgreSQL, and Kubernetes YAML**.

<br>

![Podman](https://img.shields.io/badge/Podman-892CA0?style=for-the-badge&logo=podman&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-1.27-009639?style=for-the-badge&logo=nginx&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-RHEL%2FUbuntu-FCC624?style=for-the-badge&logo=linux&logoColor=black)

</div>

---

## 📌 Project Overview

**ShopEase Order Service** is a containerized e-commerce backend designed to demonstrate a practical DevOps deployment workflow.

The application consists of three components:

| Component | Technology | Responsibility |
|---|---|---|
| 🌐 Gateway | Nginx | Public entry point & reverse proxy |
| ⚙️ API | Flask + Gunicorn | REST API for order operations |
| 🗄️ Database | PostgreSQL 16 | Stores order information |

The project demonstrates how the **same container images** can be deployed using two different Podman execution models:

```text
Development  →  Podman Compose
Staging      →  Podman Pod + Kubernetes YAML
```
🏗️ Architecture
#chatgpt-mermaid-_r_59g_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-_r_59g_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_59g_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_59g_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-_r_59g_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-_r_59g_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-_r_59g_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-_r_59g_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-_r_59g_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-_r_59g_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-_r_59g_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-_r_59g_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_59g_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_59g_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-_r_59g_ p{margin:0;}#chatgpt-mermaid-_r_59g_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_59g_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-_r_59g_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_59g_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-_r_59g_ .label text,#chatgpt-mermaid-_r_59g_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_59g_ .node rect,#chatgpt-mermaid-_r_59g_ .node circle,#chatgpt-mermaid-_r_59g_ .node ellipse,#chatgpt-mermaid-_r_59g_ .node polygon,#chatgpt-mermaid-_r_59g_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-_r_59g_ .rough-node .label text,#chatgpt-mermaid-_r_59g_ .node .label text,#chatgpt-mermaid-_r_59g_ .image-shape .label,#chatgpt-mermaid-_r_59g_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-_r_59g_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-_r_59g_ .rough-node .label,#chatgpt-mermaid-_r_59g_ .node .label,#chatgpt-mermaid-_r_59g_ .image-shape .label,#chatgpt-mermaid-_r_59g_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-_r_59g_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-_r_59g_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_59g_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-_r_59g_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-_r_59g_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-_r_59g_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-_r_59g_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-_r_59g_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-_r_59g_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-_r_59g_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-_r_59g_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-_r_59g_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_59g_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-_r_59g_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-_r_59g_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-_r_59g_ .icon-shape,#chatgpt-mermaid-_r_59g_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-_r_59g_ .icon-shape p,#chatgpt-mermaid-_r_59g_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-_r_59g_ .icon-shape .label rect,#chatgpt-mermaid-_r_59g_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-_r_59g_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-_r_59g_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-_r_59g_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-_r_59g_ [data-look="neo"].node rect,#chatgpt-mermaid-_r_59g_ [data-look="neo"].cluster rect,#chatgpt-mermaid-_r_59g_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-_r_59g_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_59g_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-_r_59g_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-_r_59g_-gradient);stroke-width:1px;}#chatgpt-mermaid-_r_59g_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_59g_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-_r_59g_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-_r_59g_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_59g_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-_r_59g_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-_r_59g_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_59g_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-_r_59g_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_59g_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-_r_59g_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-_r_59g_ .node tspan[font-weight="normal"],#chatgpt-mermaid-_r_59g_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-_r_59g_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-_r_59g_ .node rect,#chatgpt-mermaid-_r_59g_ .node circle,#chatgpt-mermaid-_r_59g_ .node ellipse,#chatgpt-mermaid-_r_59g_ .node polygon,#chatgpt-mermaid-_r_59g_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-_r_59g_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-_r_59g_ .node.mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-_r_59g_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-_r_59g_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_59g_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}👤 Client🌐 Nginx GatewayPort 80⚙️ Flask APIGunicorn :5000🗄️ PostgreSQL 16:5432HTTP :8080 / :8081/api/*SQL




🔐 Network Flow
                    Public Access
                         │
                         ▼
                 ┌───────────────┐
                 │  Nginx        │
                 │   Gateway     │
                 │    :80        │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │ Flask API     │
                 │ Gunicorn      │
                 │    :5000      │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │ PostgreSQL    │
                 │    :5432      │
                 └───────────────┘

🔒 Only the Nginx gateway is exposed to the host.
The Flask API and PostgreSQL database are not directly published.

🔄 Deployment Workflow
        ┌─────────────────────┐
        │   Source Code       │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │ Build Container      │
        │ Images               │
        └──────────┬──────────┘
                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
 ┌────────────────┐  ┌─────────────────┐
 │ Development    │  │ Staging         │
 │ Podman Compose │  │ Podman Pod      │
 └───────┬────────┘  └────────┬────────┘
         │                    │
         ▼                    ▼
     :8080                :8081

🧩 Two Deployment Models
Environment	Deployment	Port	Networking
🧪 Development	Podman Compose	8080	Service-name DNS
🚀 Staging	Podman Pod + K8s YAML	8081	Shared localhost


🧠 Key Networking Concept
One of the main concepts demonstrated in this project is how container networking changes between Compose and Podman Pods.
Podman Compose
API → DB_HOST=db

Nginx → API_HOST=api

Containers communicate using their service names.
Podman Pod
API → DB_HOST=127.0.0.1

Nginx → API_HOST=127.0.0.1

Containers inside the same Pod share the same network namespace, allowing them to communicate through localhost.
             Podman Pod
        ┌───────────────────────┐
        │                       │
        │  Nginx                │
        │    │                  │
        │    ▼                  │
        │  Flask API            │
        │    │                  │
        │    ▼                  │
        │  PostgreSQL           │
        │                       │
        └───────────────────────┘

📁 Project Structure
shopease-orders/
│
├── 📂 app/
│   ├── Containerfile
│   ├── app.py
│   └── requirements.txt
│
├── 📂 db/
│   ├── Containerfile
│   └── init.sql
│
├── 📂 nginx/
│   ├── Containerfile
│   └── default.conf.template
│
├── 📂 kube/
│   └── order-pod.yaml
│
├── compose.yaml
└── README.md

🛠️ Technology Stack
Category	Technology
Container Engine	Podman
Container Orchestration	Podman Compose
Pod Deployment	podman kube play
Reverse Proxy	Nginx
Backend	Python Flask
Application Server	Gunicorn
Database	PostgreSQL 16
Configuration	Environment Variables
Deployment Definition	YAML
Container Build	Containerfile
API	REST


🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/<YOUR-USERNAME>/shopease-orders.git
cd shopease-orders

📦 Build Container Images
Build the three application images:
podman build -t localhost/shopease-order-db:1.0 ./db

podman build -t localhost/shopease-order-api:1.0 ./app

podman build -t localhost/shopease-gateway:1.0 ./nginx

Verify the images:
podman images

🧪 Development Deployment
The development environment uses Podman Compose.
Start the complete application:
podman-compose up -d --build

Check running containers:
podman-compose ps

Expected architecture:
Browser
   │
   ▼
localhost:8080
   │
   ▼
Nginx
   │
   ▼
Flask API
   │
   ▼
PostgreSQL

🔍 Verify the Application
Health Check
curl http://localhost:8080/api/health

Expected response:
{
  "database": "connected",
  "status": "ok"
}

List Orders
curl http://localhost:8080/api/orders

Get a Specific Order
curl http://localhost:8080/api/orders/1

➕ Create a New Order
curl -X POST http://localhost:8080/api/orders \
-H "Content-Type: application/json" \
-d '{
  "customer": "Rahul Patil",
  "item": "Laptop Stand",
  "quantity": 1
}'

🔄 Update Order Status
curl -X PATCH http://localhost:8080/api/orders/1 \
-H "Content-Type: application/json" \
-d '{
  "status": "DELIVERED"
}'

Supported order states:
PLACED
   ↓
PACKED
   ↓
SHIPPED
   ↓
DELIVERED

📊 API Endpoints
Method	Endpoint	Purpose
GET	/api/health	Check API & database health
GET	/api/orders	List all orders
GET	/api/orders/<id>	Get a specific order
POST	/api/orders	Create an order
PATCH	/api/orders/<id>	Update order status


🔐 Container Security
The API container follows a non-root execution model.
podman image inspect localhost/shopease-order-api:1.0 \
--format '{{.Config.User}}'

Expected:
1001

The Flask application runs as a dedicated non-root user instead of running as root.
🚀 Staging Deployment with Podman Pod
The same container images can be deployed as a single Pod using Kubernetes-compatible YAML.
Start the staging environment:
podman kube play kube/order-pod.yaml

Check the Pod:
podman pod ps

Check containers inside the Pod:
podman ps --pod --filter pod=shopease-orders

🌐 Test Staging Environment
The staging gateway runs on:
http://localhost:8081

Health Check
curl http://localhost:8081/api/health

List Orders
curl http://localhost:8081/api/orders

🗄️ Verify PostgreSQL
Access the PostgreSQL container:
podman exec -it shopease-orders-db \
psql -U shopease -d orders \
-c "SELECT * FROM orders;"

This verifies that the application is communicating with PostgreSQL successfully.
🔁 Replace the Pod
The staging deployment can be recreated from the YAML definition:
podman kube play --replace kube/order-pod.yaml

Remove the staging Pod:
podman kube down kube/order-pod.yaml

🧱 Container Design
Each application component has its own Containerfile.
┌──────────────────────────────┐
│ Nginx Container              │
│ Reverse Proxy                │
└──────────────────────────────┘

┌──────────────────────────────┐
│ Flask Container              │
│ Gunicorn + REST API          │
│ Non-root user                │
└──────────────────────────────┘

┌──────────────────────────────┐
│ PostgreSQL Container         │
│ Database + Initialization    │
└──────────────────────────────┘

⚙️ DevOps Practices Demonstrated
🔹 Containerization
Each application component is packaged into an independent container image.
🔹 Reverse Proxy
Nginx acts as the single public entry point.
🔹 Environment-Based Configuration
Database and API hosts are configured using environment variables instead of hardcoded networking.
🔹 Non-Root Container
The Flask API runs using UID 1001.
🔹 Gunicorn
The Flask application is served using Gunicorn with multiple workers.
🔹 Image Reusability
The same images are reused between development and staging.
🔹 Kubernetes-Compatible Deployment
The application can be deployed as a Pod using:
podman kube play

🧪 Useful Troubleshooting Commands
View all containers
podman ps -a

View logs
podman logs shopease-api

podman logs shopease-gateway

View Compose logs
podman-compose logs api

Inspect Pod
podman pod inspect shopease-orders

Inspect images
podman images

📸 Project Screenshots
Add your actual project screenshots here after uploading them to GitHub.

Application Health Check
/api/health

Order Listing
/api/orders

Podman Compose
podman-compose ps

Pod Deployment
podman pod ps

🎯 What I Learned
Through this project, I practiced:
- 🐳 Container image creation using Containerfiles
- 📦 Multi-container application deployment with Podman
- 🔗 Container-to-container networking
- 🌐 Nginx reverse proxy configuration
- ⚙️ Flask REST API development
- 🗄️ PostgreSQL containerization
- 🔐 Non-root container execution
- 🔧 Environment-based application configuration
- 🧩 Podman Compose
- ☸️ Kubernetes-compatible YAML
- 🚀 podman kube play
- 🔍 Application and container troubleshooting
- 🔄 Reusing the same images across deployment environments
💡 Important Project Concept
The main idea behind this project is:
Build once → Run in different environments

The application images remain the same while the runtime configuration changes depending on the deployment model.
                 SAME IMAGES
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
   Podman Compose          Podman Pod
   Development             Staging
       │                       │
       ▼                       ▼
    :8080                   :8081

This demonstrates an important DevOps principle of separating application images from runtime configuration.
🔮 Future Improvements
Possible extensions for this project:
- [ ] Add PostgreSQL persistent volumes
- [ ] Add automated CI/CD pipeline
- [ ] Push images to a container registry
- [ ] Add Prometheus monitoring
- [ ] Add Grafana dashboards
- [ ] Add centralized logging
- [ ] Add automated testing
- [ ] Add secrets management
- [ ] Deploy to Kubernetes/OpenShift
- [ ] Add HTTPS/TLS to the gateway
⭐ Project Highlights
✅ Multi-container architecture
✅ Nginx reverse proxy
✅ Flask REST API
✅ PostgreSQL database
✅ Podman Containerfiles
✅ Podman Compose deployment
✅ Podman Pod deployment
✅ Kubernetes-compatible YAML
✅ Environment-based configuration
✅ Non-root application container
✅ API & database verification

👨‍💻 Author
<div align="center">

Saiprasad Godge
Cloud & DevOps Enthusiast
Building hands-on projects around:
Linux • AWS • Podman • Docker • Kubernetes • Ansible • CI/CD

