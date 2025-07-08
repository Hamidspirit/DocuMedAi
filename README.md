# DocuMedAi 

**DocuMedAI** is an AI-powered medical document analysis web app. It allows users to upload medical PDF reports, and the system extracts and analyzes relevant information using OCR and NLP techniques. Designed for patients and healthcare providers to quickly understand medical content and connect with the right specialists.

---

## 🚀 Features

- 🧠 AI/NLP to extract symptoms, conditions, and medications from PDFs
- 📄 OCR from scanned medical documents
- 🌍 Suggests nearby specialists based on condition
- 👨⚕️Secure login, upload, and report storage
- 📊 Visual insights for easier report understanding

---

## 🏗️ Architecture

- **Python Microservice** – FastAPI-based OCR + NLP engine
- **C# Web API** – ASP.NET Core backend for auth, user management, and report storage
- **Frontend (React or Blazor)** – Optional UI to view and interact with reports
- **Database** – PostgreSQL (for user + report storage)
- **Dockerized** – Fully containerized with `docker-compose`

---

## 📁 Repository Structure

| Folder              | Description                          |
|---------------------|--------------------------------------|
| `ml-service-python/`| Python FastAPI microservice          |
| `backend-dotnet/`   | C# ASP.NET Core backend              |
| `frontend/`         | React or Blazor-based frontend       |
| `docker/`           | Dockerfiles and docker-compose setup |
| `docs/`             | Design docs and API specs            |

---

## 🛠️ Running Locally (Coming Soon)

1. Clone the repo:
   ```bash
   git clone https://github.com/Hamidspirit/documedai.git
   cd documedai

## 🧪 Project Status

| Component         | Status         |
| ----------------- | -------------- |
| Python ML Service | 🟡 In Progress |
| C# Web API        | 🔲 Not Started |
| Frontend          | 🔲 Not Started |


