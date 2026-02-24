# FastAPI Setup

## How to run the app

### 1) Open terminal in project folder

```powershell
cd C:/Users/Lenovo/Desktop/FastApi
```

### 2) Activate virtual environment (PowerShell)

```powershell
.\env\Scripts\Activate.ps1
```

### 3) Install dependencies

```powershell
python -m pip install -r requirements.txt
```

If `python` command does not work, use:

```powershell
C:/Users/Lenovo/Desktop/FastApi/env/Scripts/python.exe -m pip install -r requirements.txt
```

### 4) Run FastAPI server

```powershell
python -m uvicorn main:app --reload
```

If `python` command does not work, use:

```powershell
C:/Users/Lenovo/Desktop/FastApi/env/Scripts/python.exe -m uvicorn main:app --reload
```

### 5) Open in browser

- App: `http://127.0.0.1:8000/`
- Swagger docs: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Available endpoints

- `GET /`
- `GET /health`
