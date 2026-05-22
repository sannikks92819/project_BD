from app.db.db import SessionLocal, engine
from app.db import models, crud

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:

    cat1 = crud.create_category(db, "Программирование")
    cat2 = crud.create_category(db, "Алгоритмы")
    

    crud.create_book(db, "Python для начинающих", "Книга для изучения Python", 1500, cat1.id)
    crud.create_book(db, "Django на примерах", "Практическое руководство по Django", 2000, cat1.id)
    crud.create_book(db, "Основы JavaScript", "Введение в JavaScript", 1200, cat1.id)
    

    crud.create_book(db, "Алгоритмы и структуры данных", "Классический учебник", 2500, cat2.id)
    crud.create_book(db, "Грокаем алгоритмы", "Алгоритмы для новичков", 1800, cat2.id)
    
    print("✅ Категории и книги успешно добавлены!")
    
finally:
    db.close()