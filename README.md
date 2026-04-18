# Inventory Service API

A RESTful backend API for managing inventory items, built using FastAPI and PostgreSQL with JWT-based authentication.

---

## 🚀 Live Demo
https://web-production-70eb8.up.railway.app/docs

---

## 🧠 Features

- User registration and login (JWT authentication)
- Protected API endpoints
- Create, read, update, and delete inventory items
- Low stock detection endpoint
- PostgreSQL database integration
- Deployed on Railway

---

## 🛠 Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- Uvicorn
- Railway (deployment)

---

## 📌 API Endpoints

### Auth
- POST `/register` — Register new user
- POST `/login` — Login and receive token

### Inventory
- GET `/items/` — Get all items
- POST `/items/` — Create item
- PUT `/items/{item_id}` — Update quantity
- DELETE `/items/{item_id}` — Delete item
- GET `/items/low-stock/` — Get low stock items

---

## ⚙️ Running Locally

```bash
git clone https://github.com/ashar-naveed/inventory-service-api
cd inventory-service-api
pip install -r requirements.txt
uvicorn main:app --reload
