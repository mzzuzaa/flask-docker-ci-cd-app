# 🐳 Flask Docker CI/CD App

A simple **To-Do web application** demonstrating:

- ✅ Flask for backend
- ✅ PostgreSQL for database
- ✅ Redis for page view counting
- ✅ Docker & Docker Compose for containerization
- ✅ GitHub Actions for automated CI/CD

---
## 🗂 Project Structure

flask-docker-ci-cd-app/
│
├── app/ # Flask app (main.py, requirements.txt, Dockerfile)
├── .github/workflows/ # GitHub Actions CI config
├── docker-compose.yml # Compose config for web, db, redis
├── .env.example # Environment variables template
└── README.md # Project documentation

## 🚀 Features

- Add and view tasks via API
- Redis counts how many times the home page is visited
- Containers automatically connect via Docker Compose
- Project auto-tested and built via GitHub Actions workflow

---
![CI](https://github.com/mzzuzaa/flask-docker-ci-cd-app/actions/workflows/main.yml/badge.svg)


## 🛠 Technologies Used

| Technology       | Purpose                        |
|------------------|--------------------------------|
| Flask            | Web framework                  |
| PostgreSQL       | Relational database            |
| Redis            | View counter (extra feature)   |
| Docker           | Containerization               |
| GitHub Actions   | CI/CD pipeline                 |

---

## 🧪 API Endpoints

### `POST /tasks`
Add a new task  
**Request body:**
GET /tasks
Retrieve all tasks
Response:
```json
{
  "content": "Buy milk"
}
[
  {
    "id": 1,
    "content": "Buy milk"
  }
]
git clone https://github.com/mzzuzaa/flask-docker-ci-cd-app.git
cd flask-docker-ci-cd-app
cp .env.example .env
docker-compose up --build
Then visit: http://localhost:5000
🔧 CI/CD

GitHub Actions automatically runs tests and builds the Docker image on every push.

