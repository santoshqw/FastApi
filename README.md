# Shopkeeper Backend (FastAPI)

This backend is designed for shopkeepers to manage daily business operations:
- stock/inventory information
- sales tracking
- profit and analytics
- shop-level reporting

## 1) Product Goal

Build a secure and simple API so a shop owner can:
- add and manage products
- track stock in and stock out
- record every sale
- see total sales, total cost, gross profit, and net profit
- monitor low-stock items

## 2) Current Status

Current codebase includes:
- FastAPI app bootstrap in `main.py`
- Basic user Pydantic model in `models/user.py`

Current endpoint:
- `GET /` returns home response

## 3) Recommended Backend Modules

Suggested structure for scaling this project:

```text
.
├── main.py
├── models/
│   ├── user.py
│   ├── product.py
│   ├── sale.py
│   └── inventory.py
├── routers/
│   ├── auth.py
│   ├── products.py
│   ├── sales.py
│   ├── inventory.py
│   └── reports.py
├── services/
│   ├── profit_service.py
│   └── inventory_service.py
├── db/
│   ├── base.py
│   ├── session.py
│   └── models/
└── schemas/
	├── user.py
	├── product.py
	├── sale.py
	└── report.py
```

## 4) Core Entities (Data Model)

### User
- id
- name
- email (unique)
- password_hash
- is_active
- created_at

### Product
- id
- name
- sku (unique)
- category
- unit
- purchase_price
- selling_price
- current_stock
- reorder_level
- is_active

### Sale
- id
- user_id
- customer_name (optional)
- total_amount
- total_cost
- gross_profit
- payment_method
- created_at

### SaleItem
- id
- sale_id
- product_id
- quantity
- unit_selling_price
- unit_cost_price
- line_total
- line_profit

### InventoryMovement
- id
- product_id
- movement_type (`IN`, `OUT`, `ADJUSTMENT`)
- quantity
- reason
- reference_id (sale/purchase/adjustment)
- created_at

### Expense (optional but recommended)
- id
- title
- amount
- expense_type (rent, salary, utility, etc.)
- created_at

## 5) Profit Formulas

- `line_total = quantity * unit_selling_price`
- `line_profit = (unit_selling_price - unit_cost_price) * quantity`
- `total_sales = sum(line_total)`
- `total_cost = sum(unit_cost_price * quantity)`
- `gross_profit = total_sales - total_cost`
- `net_profit = gross_profit - total_expenses`

## 6) API Design (Planned)

### Auth
- `POST /auth/register`
- `POST /auth/login`
- `GET /auth/me`

### Products
- `POST /products`
- `GET /products`
- `GET /products/{product_id}`
- `PUT /products/{product_id}`
- `DELETE /products/{product_id}`

### Inventory
- `POST /inventory/in` (stock purchase/addition)
- `POST /inventory/out` (manual stock out)
- `POST /inventory/adjust` (correction)
- `GET /inventory/low-stock`
- `GET /inventory/movements`

### Sales
- `POST /sales` (create sale with sale items)
- `GET /sales`
- `GET /sales/{sale_id}`
- `GET /sales/summary/daily`
- `GET /sales/summary/monthly`

### Reports
- `GET /reports/dashboard`
- `GET /reports/profit?from=YYYY-MM-DD&to=YYYY-MM-DD`
- `GET /reports/top-products`
- `GET /reports/slow-products`

## 7) Dashboard Metrics for Shopkeeper

- today_sales
- today_profit
- monthly_sales
- monthly_profit
- total_products
- out_of_stock_count
- low_stock_count
- top_selling_products

## 8) Recommended Stack

- FastAPI for API layer
- Pydantic for request/response validation
- SQLAlchemy + Alembic for DB and migrations
- PostgreSQL (recommended) or SQLite (for local)
- JWT authentication
- Uvicorn for local server

## 9) How to Run Locally

### 1) Open terminal in project folder

```powershell
cd C:/Users/Lenovo/Desktop/FastApi
```

### 2) Activate virtual environment

```powershell
.\env\Scripts\Activate.ps1
```

### 3) Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4) Start server

```powershell
python -m uvicorn main:app --reload
```

### 5) Open docs

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 10) Development Roadmap

1. Add database configuration and models.
2. Implement authentication (register/login/JWT).
3. Implement products CRUD.
4. Implement inventory movement APIs.
5. Implement sales transaction API with stock deduction.
6. Implement reports and profit analytics.
7. Add validation, logging, and tests.

## 11) Notes

- Keep business logic in service layer, not directly in route functions.
- Never store raw passwords; always store password hashes.
- Wrap sale creation in a DB transaction to avoid stock mismatch.
- Validate stock before confirming a sale.
