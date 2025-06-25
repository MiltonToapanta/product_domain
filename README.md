# 🛒 Product Domain

This multirepo is responsible for managing products in the system. It supports basic CRUD operations and is built using **Flask**, **SQLAlchemy**, **Marshmallow**, and **PostgreSQL**, designed to work as part of a microservices architecture.

---

## 🚀 Features

- Create, Read, Update, and Delete products
- Search products by name
- JSON serialization using Marshmallow
- Auto table creation on service start
- CORS enabled for cross-origin access

---

## 🧱 Tech Stack

- Python 3.12
- Flask
- Flask-SQLAlchemy
- Flask-Marshmallow
- PostgreSQL
- Docker
- dotenv for environment management

---

## 📁 Project Structure

```bash
product_add_service/
├── models/
│ └── product.py
├── routes/
│ └── product_routes.py
├── schemas/
│ └── product_schema.py
├── init.py
├── config.py
├── run.py
├── requirements.txt
```

## ⚙️ Environment Variables

Create a `.env` file or pass variables:

- `DATABASE_UR` `postgresql://user:password@db_host:db_port/database
`
- `PORT` `5000`

## 🛠️ API Endpoints
#### ✅ Create Product

POST `/api/products/create`
```json
{
  "nombre": "Milk",
  "descripcion": "1L bottle",
  "precio": 1.99,
  "foto": "https://example.com/image.jpg",
  "stock": true,
  "categoria": "Dairy",
  "especie": 1
}
```
#### 🔁 Update Product

PUT `/api/products/update/<product_id>`

```json
{
  "nombre": "Updated Milk",
  "descripcion": "1L fresh bottle",
  "precio": 2.49,
  "foto": "https://example.com/updated-image.jpg",
  "stock": true,
  "categoria": "Dairy",
  "especie": 1
}
```
#### ❌ Delete Product
DELETE `/api/products/delete/<product_id>`
```json
No body required.
```

#### 📄 List All Products
GET `/api/products/all`

#### 🔍 Search by Name
GET `/api/products/search?nombre=milk`

## 📦 Requirements

Install dependencies:
```bash
pip install -r requirements.txt
```

## 👨‍💻 Author

Developed by Milton Toapanta