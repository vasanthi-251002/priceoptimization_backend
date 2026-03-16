### 1. Backend Setup (Django)

```bash
# Navigate to backend
cd price-optimization/backend

# Create a virtual environment
python -m venv venv

# Activate it
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Seed sample data (products + demo admin user)
python manage.py seed_data

# Start the server
python manage.py runserver
```

Backend runs at: **http://localhost:8000**

#### Demo Credentials (created by seed_data)
- Email: `admin@demo.com`
- Password: `Admin@1234`

---


```

Frontend runs at: **http://localhost:3000**

> The `"proxy": "http://localhost:8000"` in `package.json` automatically forwards all `/api/` requests to Django — no CORS issues during development.

---

### 3. PostgreSQL (Optional — Production)

To switch from SQLite to PostgreSQL:

1. Create a database:
```sql
CREATE DATABASE price_optimization_db;
```

2. In `backend/price_tool/settings.py`, comment out the SQLite block and uncomment the PostgreSQL block:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'price_optimization_db',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

3. Re-run migrations:
```bash
python manage.py migrate
python manage.py seed_data
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | Register new user |
| POST | `/api/auth/login/` | Login, returns JWT tokens |
| GET | `/api/auth/me/` | Get current user |
| POST | `/api/auth/token/refresh/` | Refresh access token |
| GET | `/api/products/` | List products (search, filter, paginate) |
| POST | `/api/products/` | Create product |
| GET | `/api/products/{id}/` | Retrieve product |
| PUT | `/api/products/{id}/` | Update product |
| DELETE | `/api/products/{id}/` | Delete product |
| GET | `/api/products/demand-forecast/` | Products + chart data |
| GET | `/api/products/pricing-optimization/` | Products + optimized prices |
| GET | `/api/products/stats/` | Dashboard summary stats |
| GET | `/api/categories/` | List all categories |

### Query Params for `/api/products/`
- `search=wireless` — full-text search on name/description
- `category=Electronics` — filter by category name
- `page=2` — pagination
- `ordering=-selling_price` — sort by any field

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 18, React Router v6, Chart.js, Axios |
| Backend | Django 4.2, Django REST Framework, SimpleJWT |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Auth | JWT (access + refresh tokens, auto-refresh on 401) |
| Styling | Custom CSS (dark theme matching BCG-X UI) |

---

## Features

- JWT Authentication (login, register, auto token refresh)
- Role-based users: Admin, Buyer, Supplier
- Full CRUD for products with validation
- Search by name/description, filter by category
- Paginated product table (10/page)
- Demand Forecast modal with Line chart (Chart.js)
- Pricing Optimization table with savings % calculation
- Dark theme UI matching the provided design spec
- Django Admin panel at `/admin/`

---

## Django Admin

```
URL:      http://localhost:8000/admin/
Email:    admin@demo.com
Password: Admin@1234
```
