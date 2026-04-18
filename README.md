# Inventory Service API

A backend REST API built using FastAPI and PostgreSQL for managing inventory.

## Features

- Create items
- View all items
- Update item quantity
- Delete items
- Identify low-stock items

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run the server:
   python -m uvicorn main:app --reload

3. Open API docs:
   http://127.0.0.1:8000/docs

## Example Endpoints

- POST /items/
- GET /items/
- PUT /items/{item_id}
- DELETE /items/{item_id}
- GET /items/low-stock/
