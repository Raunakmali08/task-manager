# Task Manager with Jenkins CI/CD

A simple Task Manager web application built with Flask and Python, featuring a fully automated CI/CD pipeline using Jenkins and Docker.

> **Note:** The main focus of this project is NOT the app itself — it's the DevOps pipeline that automatically builds, tests, and deploys it on every GitHub push.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Application | Flask (Python) |
| Database | SQLite |
| Containerization | Docker |
| CI/CD | Jenkins |
| Source Control | GitHub |
| Testing | Pytest |
| Environment | WSL2 (Ubuntu) |

---

## Project Structure
```
Task-Manager/
└── neon-zenith/
    ├── app.py               # Flask application
    ├── requirements.txt     # Python dependencies
    ├── Dockerfile           # Container configuration
    ├── Jenkinsfile          # CI/CD pipeline definition
    ├── tasks.db             # SQLite database (auto-created)
    ├── templates/
    │   └── index.html       # Frontend UI
    └── tests/
        └── test_app.py      # Pytest test suite
```

---

## CI/CD Pipeline

Every push to the `main` branch triggers the Jenkins pipeline automatically:
```
GitHub Push
     ↓
Stage 1: Clone      — Pull latest code from GitHub
     ↓
Stage 2: Build      — Build Docker image from Dockerfile
     ↓
Stage 3: Test       — Run pytest test suite (4 tests)
     ↓
Stage 4: Deploy     — Stop old container, start new one on port 5000
```

---

## How to Run Locally

### Prerequisites
- Docker installed
- Jenkins running in Docker
- WSL2 (Ubuntu)

### 1. Clone the repo
```bash
git clone https://github.com/Raunakmali08/task-manager.git
cd task-manager
```

### 2. Run Jenkins
```bash
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts
```

### 3. Access Jenkins
Open `http://localhost:8080` and configure a Pipeline job pointing to this repo.

### 4. Build and Deploy
Click **Build Now** in Jenkins — the app will be live at `http://localhost:5000`

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Frontend UI |
| GET | /api/tasks | Get all tasks |
| POST | /api/tasks | Create a task |
| PUT | /api/tasks/:id | Update a task |
| DELETE | /api/tasks/:id | Delete a task |

---

## Author

**Raunak Mali** — Cloud/DevOps Engineer  
GitHub: [@Raunakmali08](https://github.com/Raunakmali08)  
Instagram: [@raunakoncloud](https://instagram.com/raunakoncloud)
