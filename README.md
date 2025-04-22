# 🛒 Django eCommerce Backend API

A fully functional backend for an eCommerce application built with Django & Django REST Framework.  
Includes user authentication, product and category management, and JWT-based security.

---

## 🚀 Features Implemented

- ✅ User Signup & Login (JWT)
- ✅ Auth-protected APIs
- ✅ Product CRUD with category linking
- ✅ Only logged-in users can add/update/delete
- ✅ Products linked to their creator (track who added what)
- ✅ "My Products" endpoint to get products by logged-in user
- ✅ Basic middleware logging and testing

---

## 🔐 Authentication

This project uses `SimpleJWT` for authentication.

### 🔑 Endpoints:
| Route | Method | Purpose |
|-------|--------|---------|
| `/auth/signUp/` | POST | Register new user |
| `/api/token/` | POST | Login (get access + refresh token) |
| `/api/token/refresh/` | POST | Get a new access token |

---

## 📦 Product API Routes

| Route | Method | Auth Required? | Description |
|-------|--------|----------------|-------------|
| `/product_api/get_products/` | GET | ❌ No | List all products |
| `/product_api/creating_product/` | POST | ✅ Yes | Add a product |
| `/product_api/update_product/<id>/` | PATCH | ✅ Yes | Update product |
| `/product_api/delete_product/<id>/` | DELETE | ✅ Yes | Delete product |
| `/product_api/get_my_product/` | GET | ✅ Yes | List logged-in user's products |

---

## 🗂 Category API Routes

| Route | Method | Auth Required? | Description |
|-------|--------|----------------|-------------|
| `/product_api/get_all_category/` | GET | ❌ No | View all categories |
| `/product_api/create_category/` | POST | ✅ Yes | Add a category |
| `/product_api/delete_category/<id>/` | DELETE | ✅ Yes | Delete a category |

---

## ⚙️ Tech Stack

- Python 3.x
- Django
- Django REST Framework
- SimpleJWT

---

## 🧪 Running Locally

```bash
git clone https://github.com/yourusername/ecommerce.git
cd ecommerce
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py runserver
