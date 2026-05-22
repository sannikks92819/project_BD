from fastapi import FastAPI
from app.api import categories, books

app = FastAPI(
    title="Book API",
    description="API для управления книгами и категориями",
    version="1.0.0"
)

# Подключаем роутеры
app.include_router(categories.router)
app.include_router(books.router)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Service is running"}

@app.get("/")
def root():
    return {"message": "Welcome to Book API", "docs": "/docs"}