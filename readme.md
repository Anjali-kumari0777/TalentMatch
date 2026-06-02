# TalentMatch

TalentMatch is an AI-powered freelancer matching platform that helps clients find the most relevant freelancers based on project requirements using semantic search.

Instead of relying on keyword matching, TalentMatch uses embeddings and vector similarity search to identify freelancers whose skills and experience best match a project description.

---

## Features

* Create and manage freelancer profiles
* Store freelancer skills and experience in SQLite
* Generate semantic embeddings using Sentence Transformers
* Store embeddings in Qdrant Vector Database
* Perform semantic search on freelancer profiles
* Return top matching freelancers for a project description
* REST APIs built with FastAPI
* Pydantic request validation
* SQLAlchemy ORM integration

---

## Tech Stack

### Backend

* FastAPI
* Python
* SQLAlchemy
* Pydantic

### Database

* SQLite
* Qdrant Vector Database

### AI / Machine Learning

* Sentence Transformers
* all-MiniLM-L6-v2 Embedding Model

---

## Project Architecture

Client Project Requirement
↓
FastAPI API
↓
Sentence Transformer
↓
Generate Embedding
↓
Qdrant Vector Search
↓
Top Matching Freelancers

---

## Database Design

### Freelancers Table

| Field            | Type    |
| ---------------- | ------- |
| id               | Integer |
| name             | String  |
| bio              | String  |
| experience_years | Integer |
| hourly_rate      | Float   |

### Skills Table

| Field         | Type    |
| ------------- | ------- |
| id            | Integer |
| freelancer_id | Integer |
| skill_name    | String  |

---

## API Endpoints

### Create Freelancer

POST /freelancers/

Request

```json
{
  "name": "John Smith",
  "bio": "Backend Developer",
  "experience_years": 5,
  "hourly_rate": 40,
  "skills": [
    "Python",
    "FastAPI",
    "Docker"
  ]
}
```

Response

```json
{
  "message": "Freelancer created",
  "freelancer_id": 1
}
```

---

### Search Freelancers

POST /search/

Request

```json
{
  "project_description": "Need a Python FastAPI backend developer with PostgreSQL experience"
}
```

Response

```json
[
  {
    "name": "John Smith",
    "bio": "Backend Developer",
    "experience_years": 5,
    "hourly_rate": 40,
    "skills": [
      "Python",
      "FastAPI",
      "PostgreSQL"
    ],
    "score": 0.91
  }
]
```

---

## Data Generation

A synthetic dataset of more than 1000 freelancer profiles was generated using Faker and custom skill distributions.

Categories include:

* Backend Developers
* Frontend Developers
* Full Stack Developers
* Mobile Developers
* AI Engineers

---

## Semantic Search Workflow

1. Freelancer profiles are stored in SQLite.
2. Profile text is generated using skills, experience, and bio.
3. Sentence Transformers generate embeddings.
4. Embeddings are stored in Qdrant.
5. Project descriptions are converted into embeddings.
6. Qdrant performs vector similarity search.
7. Top matching freelancers are returned.

---

## Setup

### Clone Repository

```bash
git clone <repository-url>
cd TalentMatch
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
uvicorn app.main:app --reload
```

### Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Future Enhancements

* Gemini/OpenAI integration for match explanations
* Freelancer ranking based on price and experience
* Authentication and authorization
* Client project management
* Dashboard and analytics
* Frontend using React or Next.js
* Deployment on AWS

---

## Learning Outcomes

This project demonstrates:

* FastAPI backend development
* REST API design
* SQLAlchemy ORM
* SQLite database management
* Vector databases (Qdrant)
* Embedding generation
* Semantic search systems
* AI-powered recommendation engines
* End-to-end backend architecture
